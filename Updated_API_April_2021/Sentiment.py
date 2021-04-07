import os
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, DATA, ALL
from werkzeug.utils import secure_filename
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from textblob import TextBlob



def sentiment_polarity(text):

    return TextBlob(text).sentiment.polarity


def sentiment_subjectivity(text):

    return TextBlob(text).sentiment.subjectivity



def wordcount(text):

    return len(text.split())




print(str(wordcount("this is text")))

