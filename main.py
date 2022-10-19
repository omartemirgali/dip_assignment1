from fileinput import filename
import os, re
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from filters.functions import blur_image, sepia, warm, cold

app = Flask(__name__)

app.secret_key = "somesecretkey"
app.config['UPLOAD_PATH'] = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):   
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Image successfully uploaded')
        return render_template('home.html', filename=filename)
    else: 
        flash('Image extension should be png, jpg, jpeg or gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/filter/<filename>')
def filter1(filename):
    blur_image(app.config['UPLOAD_PATH'] + filename)
    return filename

@app.route('/sepia/<filename>')
def filter2(filename):
    sepia(app.config['UPLOAD_PATH'] + filename)
    return filename

@app.route('/warm/<filename>')
def filter3(filename):
    warm(app.config['UPLOAD_PATH'] + filename)
    return filename

@app.route('/cold/<filename>')
def filter4(filename):
    cold(app.config['UPLOAD_PATH'] + filename)
    return filename


if __name__ == '__main__':
    app.run()