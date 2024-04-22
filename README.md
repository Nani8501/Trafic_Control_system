# Traffic Signal Optimization using Canny Edge Detection

## Project Overview
This project, led by [Jagadeesh kokkula](https://github.com/nani8501), is a major endeavor aimed at optimizing traffic signal timing based on real-time traffic conditions. Leveraging the principles of image processing and machine learning, the project utilizes the Canny Edge Detection algorithm to analyze traffic density from camera feeds. By dynamically adjusting green signal times at traffic signals, the project aims to improve traffic flow and reduce congestion in urban areas.

## Project Details
### Dataset
The project utilizes real-time traffic images obtained from camera feeds. These images serve as input for the Canny Edge Detection algorithm to detect traffic density.

### Algorithm
The core algorithm used in this project is the Canny Edge Detection algorithm, implemented in Python. The algorithm includes Gaussian smoothing, gradient calculation, non-maximum suppression, thresholding, and hysteresis to accurately detect edges in traffic images.

### Components
- **CannyEdgeDetector.py**: Python class implementing the Canny Edge Detection algorithm.
- **app.py**: Flask web application for interacting with the Canny Edge Detector.
- **control.py**: Module for controlling traffic signal timing based on detected traffic density.
- **utils.py**: Utility functions for data preprocessing and model building.
- **requirements.txt**: List of dependencies for installing required libraries.

### Usage
1. **Setup**: Clone the repository and install dependencies using `pip install -r requirements.txt`.
2. **Running the Application**: Start the Flask web application by running `app.py`.
3. **Uploading Traffic Images**: Upload traffic images through the web interface.
4. **Traffic Density Analysis**: Processed images with detected edges will be displayed, along with traffic density analysis.
5. **Optimizing Traffic Signals**: Based on traffic density analysis, the application recommends optimal green signal times for traffic signals.

### Model Architecture
The project doesn't use a traditional machine learning model. Instead, it employs image processing techniques for traffic density analysis.

### Results
The effectiveness of the traffic signal optimization can be observed through real-time traffic flow improvements and reduced congestion at intersections.

## Project Duration
The project was initiated in December 2023 and successfully completed by Feb 2024.

## Personal Information
- **Name**: Jagadeesh Kokkula
- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/jagadeeshkokkula/)
- **GitHub**: [Your GitHub Profile](https://github.com/Nani8501)

## Contribution
Contributions to the project are welcome! If you have any suggestions for improvements or find any issues, please create an issue or submit a pull request on GitHub.

## Acknowledgements
Special thanks to contributors and maintainers of open-source libraries and frameworks used in this project. Their efforts have been instrumental in the success of this endeavor.
