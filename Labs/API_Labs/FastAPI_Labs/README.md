This lab demonstrates how to train a machine learning model, save it to a file, and serve it as a REST API. The lab uses the Scikit-Learn Wine dataset to train a basic classification model, which is then serialized and hosted using FastAPI.

Project Components
Model Training: A script that loads the dataset, trains a Logistic Regression model, and saves it using joblib (Pickle).
FastAPI Application: A web server that loads the pickled model and exposes a /predict endpoint to classify new data.
Data Validation: Uses Pydantic to ensure all incoming API requests contain the correct 13 features required by the model.

Prerequisites
Install the required Python packages before running the project:

Requirements
pip install fastapi uvicorn scikit-learn pydantic joblib numpy

Running the Lab
1. Train the Model
First, run the training script to generate the wine_model.pkl file.

Bash
python train.py

2. Start the API Server
Launch the FastAPI application using Uvicorn.

Bash
uvicorn main:app --reload

Testing the API
Once the server is running, you can test the model directly in your browser.
Navigate to http://127.0.0.1:8000/docs.

Open the /predict POST route.

Click "Try it out" and paste a JSON payload with the wine features.
Click "Execute" to see the model's predicted class in the response.

![alt text](Labs\API_Labs\FastAPI_Labs\assets\image.png)