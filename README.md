# CropAI_model_hackout
Crop Weather Prediction and Protection System

Overview
This repository contains a comprehensive solution designed to assist farmers in predicting weather conditions suitable for their crops by analyzing images taken from their phones. The system leverages machine learning to predict potential crop threats based on weather data and provides recommendations to mitigate these risks. The project is developed using TensorFlow for image classification and a weather API for real-time weather data analysis.

Features
Image-Based Crop Weather Prediction: Analyze images of crops to predict weather conditions and potential threats using a trained deep learning model.
Weather Data Integration: Fetches real-time and historical weather data using WeatherAPI to assess risks like drought, frost, heatwaves, and more.
Threat Analysis: Identifies potential crop threats based on weather conditions, including drought risk, pest infestations, and fungal diseases.
Recommendation Engine: Provides actionable recommendations for crop protection based on identified threats.
Project Structure
src/: Contains the core modules for data preprocessing, model training, prediction, and weather analysis.
data_preprocessing.py: Handles the creation of data generators for training, validation, and testing.
model.py: Contains functions to build, compile, and train the TensorFlow model.
predict.py: Facilitates the loading of the trained model and making predictions on new images.
weather_analysis.py: Analyzes weather data and provides crop protection recommendations.
dataset/: Placeholder for training, validation, and testing image datasets organized by weather conditions (e.g., dew, fog, frost, etc.).
requirements.txt: Lists the Python dependencies required to run the project.
README.md: Provides an overview and instructions for the project.
install_dependencies.py: Script to install the necessary Python packages.
