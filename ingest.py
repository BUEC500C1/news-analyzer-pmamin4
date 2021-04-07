import os
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, DATA, ALL
from werkzeug.utils import secure_filename
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from textblob import TextBlob
from Sentiment import *
from pynytimes import NYTAPI
import requests


nyt = NYTAPI("tWDmZDuJxz9fAjqkJsp6orA6DOKuhKJ6", parse_dates=True)

most_viewed = nyt.most_viewed(days = 1)

for i in most_viewed:
    print(i)