from flask import Flask
import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! \n'

@app.route('/name')
def nam():
    return 'Taru nam su che? \n'

@app.route('/index')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)