import os
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, DATA, ALL
from werkzeug.utils import secure_filename
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
#from flask import UploadSet, configure_uploads, IMAGES, DATA, ALL


app = Flask(__name__)

files = UploadSet('files', ALL)

app.config['UPLOADED_FILES_DEST'] = 'static/img'
configure_uploads(app, files)

@app.route('/uploade', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'file' in request.files:
        filename = files.save(request.files['file'])
        return filename
    return render_template('uploaded.html')


if __name__ == '__main__':
	app.run(debug=True)