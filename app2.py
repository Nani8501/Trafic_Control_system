from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from CannyEdgeDetector import CannyEdgeDetector
import cv2
import os
import numpy as np
from control import applyCanny
import matplotlib.image as mpimg  # Import mpimg module
import matplotlib.pyplot as plt  # Import matplotlib's pyplot module
from control import pixelcount, timeAllocation
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Define the allowed file extensions

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)
@app.route('/static/gray/<filename>')
def uploaded_file1(filename):
    return send_from_directory('static/gray', filename)
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_traffic_image', methods=['POST'])
def upload_traffic_image():
    try:
        if 'traffic_image' not in request.files:
            return jsonify({'status': 'error','message': 'No file part'})
        
        traffic_image = request.files['traffic_image']
        
        if traffic_image.filename == '':
            return jsonify({'status': 'error', 'message': 'No selected file'})
        
        if traffic_image and allowed_file(traffic_image.filename):
            filename = secure_filename(traffic_image.filename)
            filepath = os.path.join("static\\gray", filename)
            traffic_image.save(filepath)
            return render_template('index.html', filename=filename)
        else:
            return jsonify({'status': 'error', 'message': 'Failed to upload image'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
@app.route('/applyCanny', methods=['POST'])
def apply_canny():
    try:
        filename = request.form.get('filename')
        if filename:
            imgs = []
            
            img = plt.imread(filename)
            real_processed_filename = "gray/"+filename
            print("File Name is:",real_processed_filename)
            img_gray = rgb2gray(img)
            imgs.append(img_gray)
            edge = CannyEdgeDetector(imgs, sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.20, weak_pixel=100)
            imgs = edge.detect()
            for i, img in enumerate(imgs):
                if img.shape[0] == 3:
                    img = img.transpose(1,2,0)
            cv2.imwrite("static/gray/test.png", img)
            cv2.imwrite("static/gray/processed_file.png", img)
            processed_filename = 'gray/test.png'

            real_reference_filename = 'gray/refrence.png'
            img = plt.imread('static/gray/refrence.png')
            img_gray = rgb2gray(img)
            imgs.append(img_gray)
            edge = CannyEdgeDetector(imgs, sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.20, weak_pixel=100)
            imgs = edge.detect()
            for i, img in enumerate(imgs):
                if img.shape[0] == 3:
                    img = img.transpose(1,2,0)
            cv2.imwrite("static/gray/reference.png", img)
            cv2.imwrite("static/gray/reference_file.png", img)
            reference_filename = 'gray/reference_file.png'
            return render_template('index.html',processed_filename=processed_filename,real_processed_filename=real_processed_filename, reference_filename=reference_filename,real_reference_filename=real_reference_filename)
            # return jsonify({'processed_filename': processed_filename, 'reference_filename': reference_filename})
        else:
            return jsonify({'message': 'No filename provided'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/time_allocation', methods=['POST'])
def time_allocation():
    try:
        sample_pixels, reference_pixels = pixelcount()
        green_signal_time = timeAllocation(sample_pixels, reference_pixels)
        return render_template('index.html', green_signal_time=green_signal_time)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
