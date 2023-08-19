from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import numpy as np
from pycaret.classification import *
import pickle
import os



app = Flask(__name__)

script_dir = os.path.dirname(os.path.abspath(os.getcwd()))

model_dir = os.path.join(script_dir, 'models')

# model_path = os.path.join(model_dir, '/cv_issue-pipeline.pkl')

# medical_model_file = r"C:\Users\Zhang Xiang\Desktop\Year 3\Sem 1\IT3385 Machine Learning Operations - 2\Assignment\MLOPS_ASSIGNMENT_GROUP2_TEAM6\models\cv_issue-pipeline.pkl"


@app.route('/')
def home():
    return render_template('home.html')


# @app.route('/medical_result')
# def medical_result():
#     prediction = request.args.get('prediction')
#     print(prediction)
#     return render_template('medical_result.html', prediction=prediction)
    


@app.route('/medical_predict', methods=['GET', 'POST'])
def medical_predict():
    
    # with open(medical_model_file, 'rb') as f:
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
        # pipeline = pickle.load(open(medical_model_file, 'rb'))
        
        pipeline = load_model(os.path.join(model_dir, 'cv_issue-pipeline'))
        print(pipeline)
        # model = pickle.load(f)
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
        
        prediction_label = predict_model(pipeline, data=df)['prediction_label'][0]
        print(prediction_label)

        return render_template('medical_result.html', prediction=prediction_label)

    return render_template('medical_predict.html')


if __name__ == '__main__':
    app.run(debug=True)