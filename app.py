from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import json
import pandas as pd

app = Flask(__name__)

# Load model and preprocessing objects
model = joblib.load('models/decisiontree_regressor_regression_model.pkl')
scaler = joblib.load('models/min_max_scaler.pkl')

with open('models/locality_encoding_map.pkl', 'rb') as f:
    locality_map = joblib.load(f)

with open('models/region_encoding_map.pkl', 'rb') as f:
    region_map = joblib.load(f)

# Load JSON data for dropdowns
with open('models/unique_values_locality.json', 'r') as f:
    localities = json.load(f)

with open('models/unique_values_region.json', 'r') as f:
    regions = json.load(f)

@app.route('/')
def index():
    return render_template('form.html', localities=localities, regions=regions)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    bhk = int(request.form['bhk'])
    area = float(request.form['area'])
    locality = request.form['locality']
    region = request.form['region']
    age = request.form['age']
    status = request.form['status']
    type_ = request.form['type']

    # Encode categorical variables
    locality_encoded = locality_map.get(locality, 0)
    region_encoded = region_map.get(region, 0)

    # Prepare data for prediction
    data = {
        'bhk': bhk,
        'area': area,
        'locality_target_encoded': locality_encoded,
        'region_target_encoded': region_encoded,
        f'type_{type_}': 1,
        f'status_{status}': 1,
        f'age_{age}': 1
    }

    # Create DataFrame and fill missing columns with 0
    input_df = pd.DataFrame([data])
    
    # Ensure all expected columns are present in input_df
    all_columns = model.feature_names_in_
    for col in all_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder the columns to match the order of columns used during fitting
    input_df = input_df[all_columns]

    # Scale only the 'bhk' and 'area' columns
    input_df[['bhk', 'area']] = scaler.transform(input_df[['bhk', 'area']])

    # Print to verify the DataFrame structure
    print("Final Input DataFrame columns:", input_df.columns)

    # Predict the price
    prediction = model.predict(input_df)

    return jsonify({'predicted_price': f'INR {prediction[0]:,.2f}'})

if __name__ == '__main__':
    app.run(debug=True)
