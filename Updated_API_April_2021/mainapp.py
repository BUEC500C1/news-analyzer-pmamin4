import os
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, DATA, ALL
from werkzeug.utils import secure_filename
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from textblob import TextBlob
from NLP import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

db = SQLAlchemy(app)

class Files_Uploaded(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
    polarity = db.Column(db.String(300))
    subjectivity = db.Column(db.String(300))


@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputfile']
    newFile = Files_Uploaded(name=file.filename, data=file.read(), polarity=TextBlob(file.read().decode('UTF-8')).sentiment.polarity, subjectivity=TextBlob(file.read().decode('UTF-8')).sentiment.subjectivity)
    db.session.add(newFile)
    db.session.commit()
    return 'The file  ' + file.filename + " has benn succesfully uploaded!"


@app.route('/language', methods=['POST', 'GET'])
def nelp():
    return render_template('nlp.html')


@app.route('/nlp', methods = ['POST'])
def sentiment():
    text_ent = request.form['text'] 
    written_text = str(text_ent)
    polarity = sentiment_polarity(written_text)
    subjectivity = sentiment_subjectivity(written_text)


    return written_text + '\n' +  "\npolarity: " + str(polarity) + '\n' + " \nsubjectivity: " + str(subjectivity) + " word count: " + str(wordcount(written_text.split()))
    


if __name__ == '__main__':
	app.run(debug=True)