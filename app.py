import flask
from flask import Flask, redirect, render_template, request, flash, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "raw/"
INPUT_NAME = "file_in"
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html", input_name = INPUT_NAME)

@app.route("/process-file", methods=["POST"])
def process_file():
    if request.method == 'POST':
        if INPUT_NAME not in request.files:
            return redirect('/fail-input')    # no file
        file = request.files[INPUT_NAME]
        if file.filename == '':
            return redirect('/fail-input')
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/success') 
    return redirect('/')

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/fail-input")
def fail():
    return ("fail")