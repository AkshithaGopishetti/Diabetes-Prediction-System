# Disease Prediction System Using Machine Learning

## Overview

This project is a Machine Learning-based Disease Prediction System that predicts whether a patient is likely to have diabetes based on medical parameters. The system is trained using the Pima Indians Diabetes Dataset and uses a Random Forest Classifier for prediction.

## Objectives

- Predict the likelihood of diabetes from patient health data.
- Analyze medical features affecting disease prediction.
- Evaluate model performance using machine learning metrics.
- Provide predictions for new patient data entered by users.

## Dataset

Dataset: Pima Indians Diabetes Dataset

Features:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

Target:
- Outcome (0 = No Diabetes, 1 = Diabetes)

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Train-Test Split
4. Model Training
5. Model Evaluation
6. Disease Prediction
7. Result Visualization

## Algorithm Used

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

## Performance Metrics

- Accuracy: 72.08%
- Classification Report
- Confusion Matrix

## Project Structure

DiseasePrediction/

├── diabetes.csv

├── disease_prediction.py

├── graph.py

├── screenshots/

│ ├── accuracy_graph.png

│ └── prediction_output.png

└── README.md

## Screenshots

### Accuracy Comparison Graph

The project includes a graphical comparison of model performance.

### Disease Prediction Output

The system accepts patient details and predicts whether diabetes is detected.

## Sample Prediction

Input:

Pregnancies: 6

Glucose: 148

Blood Pressure: 72

Skin Thickness: 35

Insulin: 0

BMI: 33.6

Diabetes Pedigree Function: 0.627

Age: 50

Output:

Prediction: Diabetes Detected

## Future Enhancements

- Compare multiple machine learning algorithms.
- Build a graphical user interface using Tkinter.
- Deploy as a web application.
- Extend support for multiple diseases.

## Author

Akshitha Gopishetti

B.Tech Computer Science Engineering

Gokaraju Lailavathi Engineering College

GitHub: AkshithaGopishetti