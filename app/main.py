from pycaret.regression import *
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, url_for, redirect
from pycaret.classification import *
import pickle
import joblib
from pathlib import Path
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(file_), 'templates'))

# model_path = r'models\resale_price_pipeline_zx'

import os

# script_dir = os.path.dirname(__file__)
# model_path = os.path.join(script_dir, 'models', 'resale_price_pipeline_zx')
# print(model_path)

# # Load the entire pipeline from the saved pickle file using pycaret's load_model
# loaded_pipeline = load_model(model_path)
# print(loaded_pipeline)

# medical_model_file = r"C:\Users\Zhang Xiang\Desktop\Year 3\Sem 1\IT3385 Machine Learning Operations - 2\Assignment\MLOPS_ASSIGNMENT_GROUP2_TEAM6\models\cv_issue-pipeline.pkl"

# script_dir = os.path.dirname(os.path.abspath(os.getcwd()))

# model_dir = os.path.join(script_dir, 'models')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/parik')
def parik():
    return render_template('parik_hdb.html')

@app.route('/submit')
def submit():
    original_resale_price = request.args.get('original_resale_price')
    return render_template('submit.html', data=float(original_resale_price))



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    # Get form data
    floor_area_sqm = request.form['floor_area_sqm']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    cbd_dist = request.form['cbd_dist']
    min_dist_mrt = request.form['min_dist_mrt']
    remaining_lease = request.form['remaining_lease']
    flat_type = request.form['flat_type']
    storey_range = request.form['storey_range']
    flat_model = request.form['flat_model']
    region = request.form['region']

    # Convert the form data to a dictionary
    input_data = {
        'floor_area_sqm': float(floor_area_sqm),
        'latitude': float(latitude),
        'longitude': float(longitude),
        'cbd_dist': float(cbd_dist),
        'min_dist_mrt': float(min_dist_mrt),
        'remaining_lease': float(remaining_lease),
        'flat_type': flat_type,
        'storey_range': storey_range,
        'flat_model': flat_model,
        'region': region,
    }

    # Convert the input_data dictionary to a DataFrame
    input_df = pd.DataFrame([input_data])

    pipeline = load_model('resale_price_pipeline_zx')
    print(pipeline)
    
    # Use the loaded pipeline to make predictions using the predict_model function
    pred_df = predict_model(pipeline, data=input_df)

    # Extract the prediction value from the DataFrame (assuming the column name is "Label")
    prediction_value = pred_df['prediction_label'][0]  # Get the first prediction value
    original_resale_price = np.exp(prediction_value)

    return redirect(url_for('submit', original_resale_price=original_resale_price))
# @app.route('/medical_result')
# def medical_result():
#     prediction = request.args.get('prediction')
#     print(prediction)
#     return render_template('medical_result.html', prediction=prediction)
    


    


@app.route('/medical_predict', methods=['GET', 'POST'])
def medical_predict():
    # models_dir = os.path.join(os.getcwd(), 'models')
    


    if request.method == "POST":
        print("Keys in request.form:", list(request.form.keys()))
        print("Keys in request.form:", list(request.form.values()))
        
        age = int(request.form['age'])
        gender = str(request.form['gender'])

        chest_pain = str(request.form['chest_pain'])

        resting_BP = float(request.form['resting_BP'])
        cholesterol = float(request.form['cholesterol'])
        fasting_BS = int(request.form['fasting_BS'])
        resting_ECG = str(request.form['resting_ECG'])
        max_HR = float(request.form['max_HR'])
        exercise_angina = str(request.form['exercise_angina'])
        old_peak = float(request.form['old_peak'])
        st_slope = str(request.form['ST_slope'])

        # data = [[age, gender, chest_pain, resting_BP, cholesterol, fasting_BS,
        #     resting_ECG, max_HR, exercise_angina, old_peak, st_slope]]
        # print(data)


        pipeline = load_model("cv_issue-pipeline_testing")
        print(pipeline)

        data = {
        'age': age,
        'gender':gender,
        'chest_pain':chest_pain,
        'resting_BP':resting_BP,
        'cholesterol':cholesterol,
        'fasting_BS':fasting_BS,
        'resting_ECG':resting_ECG,
        'max_HR':max_HR,
        'exercise_angina':exercise_angina,
        'old_peak':old_peak,
        'ST_slope': st_slope,
    }
        print(data)
        # classes = model.classes_
        # setup(data=data)
        # Make predictions using the pipeline
        # predicted_label = predict_model(model, data=data)['Label'][0]
        # cols =  ['age', 'gender', 'chest_pain', 'resting_BP', 'cholesterol', 'fasting_BS', 'resting_ECG', 'max_HR', 'exercise_angina', 'old_peak', 'ST_slope']
        # records = [[65, 'M', 'ATA', 23.0, 23.0, 0, 'ST', 43.0, 'Y', 23.0, 'TA']]

        df = pd.DataFrame(data, index=[0])

        predict = predict_model(pipeline, data=df)
        
        prediction_label = predict['prediction_label'][0]
        print(prediction_label)

        prediction_prob = predict['prediction_score'][0] * 100

        return render_template('medical_predict.html', prediction=prediction_label, score = prediction_prob)

    return render_template('medical_predict.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(3000), debug=True)
    
