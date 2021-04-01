from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class TextModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    words = db.Column(db.Integer, nullable=False)
    characters = db.Column(db.Integer, nullable=False)
    font = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    numbers = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Text(filename={filename}, words={words}, characters={characters}, font= {font},language={language}, numbers={numbers})"



text_put_args = reqparse.RequestParser()
text_put_args.add_argument("filename", type=str, help="Name of the file",required=True)
text_put_args.add_argument("words", type=int, help="number of words",required=True)
text_put_args.add_argument("characters", type=int, help="number of characters", required=True)
text_put_args.add_argument("font", type=str, help="written font", required = True)
text_put_args.add_argument("language", type=str, help="language", required=True)
text_put_args.add_argument("numbers", type=int, help="numbers required", required=True)

text_update_args = reqparse.RequestParser()
text_update_args.add_argument("filename", type=str, help="Name of the file")
text_update_args.add_argument("words", type=int, help="number of words")
text_update_args.add_argument("characters", type=int, help="number of characters")
text_update_args.add_argument("font", type=str, help="written font")
text_update_args.add_argument("language", type=str, help="language")
text_update_args.add_argument("numbers", type=int, help="numbers required")


resource_fields = {
    'id': fields.Integer,
    'filename': fields.String,
    'words': fields.Integer,
    'characters': fields.Integer,
    'numbers': fields.Integer,
    'font': fields.String,
    'language': fields.String
}

class Text(Resource):
    @marshal_with(resource_fields)
    def get(self,text_id):
        result = TextModel.query.filter_by(id = text_id).first()
        if not result:
            abort(404, message="Text ID not found")
        return result

    @marshal_with(resource_fields)
    def put(self,text_id):
        args = text_put_args.parse_args()
        result = TextModel.query.filter_by(id = text_id).first()
        if result:
            abort(409, message="Text already in database")

        Text = TextModel(id=text_id,filename= args['filename'], words=args['words'], characters=args['characters'], numbers=args['numbers'], font=args['font'], language=args['language'])
        db.session.add(Text)
        db.session.commit()
        return Text, 201
        
    @marshal_with(resource_fields)
    def patch(self, text_id):
        args = text_update_args.parse_args()
        result = TextModel.query.filter_by(id = text_id).first()
        if not result:
            abort(404,message="doesn't exist, cannot update")

        if args['filename']:
            result.filename = args['filename']
        if args['words']:
            result.words = args['words']
        if args['characters']:
            result.characters = args['characters']
        if args['numbers']:
            result.numbers = args['numbers']
        if args['language']:
            result.language = args['language']
        if args['font']:
            result.font = args['font']
        
        db.session.commit()
        return result


    @marshal_with(resource_fields)
    def delete(self,text_id):
        result = TextModel.query.filter_by(id=text_id).first()
        if not result:
            abort(404, message="Could not find that id")

            
        db.session.delete(result)
        db.session.commit()



api.add_resource(Text, "/text/<int:text_id>")
if __name__ == "__main__":
    app.run(debug=True)