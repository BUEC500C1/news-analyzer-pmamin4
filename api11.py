from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class UploadModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(16), nullable=False)
    filetype = db.Column(db.String(7), nullable=False)
    owner = db.Column(db.String(20),nullable=False)
    editor = db.Column(db.String(20),nullable=False)
    viewer = db.Column(db.String(20),nullable=False)
  

    def __repr__(self):
        return f"File(filename = {filename}, filetype = {filetype})"

db.create_all()


file_put_args = reqparse.RequestParser()
file_put_args.add_argument("filename", type=str, help= "name of the file is required", required=True)
file_put_args.add_argument("filetype", type=str, help = "type/form of the file", required=True)
file_put_args.add_argument("owner", type=str, help = "owner of the file", required=True)
file_put_args.add_argument("editor", type=str, help = "editor of the file", required=True)
file_put_args.add_argument("viewer", type=str, help = "viewer of the file", required=True)


file_update_args =reqparse.RequestParser()
file_update_args.add_argument("filename", type=str, help= "name of the file is required")
file_update_args.add_argument("filetype", type=str, help = "type/form of the file")
file_update_args.add_argument("owner", type=str, help = "owner of the file")
file_update_args.add_argument("editor", type=str, help = "editor of the file")
file_update_args.add_argument("viewer", type=str, help = "viewer of the file", required=True)




resource_fields = {

    'id': fields.Integer,
    'filename': fields.String,
    'filetype': fields.String,
    'owner' : fields.String,
    'editor': fields.String,
    'viewer' : fields.String,
    
}

class Upload(Resource):
    @marshal_with(resource_fields)
    def get(self, file):
        result = UploadModel.query.filter_by(id=file).first()
        if not result:
            abort(404, message="Could not find that id")
        return result

    @marshal_with(resource_fields)
    def put(self, file):
        args = file_put_args.parse_args()
        result = UploadModel.query.filter_by(id = file).first()
        if result:
            abort(409, message= "file is taken")
        upload = UploadModel(id=file, filename = args['filename'], filetype= args['filetype'], owner=args['owner'], editor=args['editor'], viewer =args['viewer'])
        db.session.add(upload)
        db.session.commit()
        return upload, 201

    @marshal_with(resource_fields)    
    def patch(self,file):
        args = file_update_args.parse_args()
        result = UploadModel.query.filter_by(id = file).first()
        if not result:
            abort(404, message= "file doesn't exist")
        if args["filename"]:
            result.filename = args['filename']
        if args["filetype"]:
            result.filetype = args['filetype']
        if args["owner"]:
            result.owner = args['owner']
        if args["editor"]:
            result.editor = args['editor']
        if args["viewer"]:
            result.viewer = args['viewer']

       
        db.session.commit()

        return result

    @marshal_with(resource_fields)
    def delete(self,file):
        result = UploadModel.query.filter_by(id=file).first()
        if not result:
            abort(404, message="Could not find that id")

            
        db.session.delete(result)
        db.session.commit()


api.add_resource(Upload, "/file/<string:file>")

if __name__ == "__main__":
    app.run(debug=True)