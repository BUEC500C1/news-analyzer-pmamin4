from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databae.db'
db = SQLAlchemy(app)

class NewsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    articlename = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable = False)
    Author = db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"News(articlename = {articlename}, publisher = {publisher}, date = {date}, Author = {Author})"




news_put_args = reqparse.RequestParser()
news_put_args.add_argument("articlename", type=str,help ="article name?",required = True)
news_put_args.add_argument("publisher", type=str,help ="article publisher?",required = True)
news_put_args.add_argument("date", type=str,help ="article date?",required = True)
news_put_args.add_argument("Author", type=str,help ="article Author?",required = True)

news_update_args = reqparse.RequestParser()
news_update_args.add_argument("articlename", type=str,help ="article name?")
news_update_args.add_argument("publisher", type=str,help ="article publisher?")
news_update_args.add_argument("date", type=str,help ="article date?")
news_update_args.add_argument("Author", type=str,help ="article Author?")

resource_fields = {
    'id' : fields.String,
    'publisher' : fields.String,
    'date': fields.String,
    'Author' : fields.String

}




class News(Resource):
    @marshal_with(resource_fields)
    def get(self, news_id):
        result = NewsModel.query.filter_by(id=news_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, news_id):
        args = news_put_args.parse_args()
        news = NewsModel(id=news_id, articlename =args['articlename'], publisher = args['publisher'], date = args['date'], Author = args['Author'] )
        db.session.add(news)
        db.session.commit()
        return news, 201

    @marshal_with(resource_fields)
    def patch(self, news_id):
        args = news_update_args.parse_args()
        result = NewsModel.query.filter_by(id=news_id).first()
        if not result:
            abort(404, message="unupdateble")
        if args['articlename']:
            result.articlename = args['articlename']
        if args['publisher']:
            result.publisher = args['publisher']
        if args['date']:
            result.date = args['date']
        if args['Author']:
            result.Author = args['Author']

        db.session.commit()
        return result
        
    @marshal_with(resource_fields)
    def delete(self,news_id):
        result = NewsModel.query.filter_by(id=news_id).first()
        if not result:
            abort(404, message="Could not find that id")

            
        db.session.delete(result)
        db.session.commit()




api.add_resource(News, "/news/<int:news_id>")

if __name__ == "__main__":

    app.run(debug=True)
