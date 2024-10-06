
# ML-Project-House-Prediction

This project is built to learn how to deploy a machine learning model and understand how one-hot encoding works. The model is designed to predict house prices in Mumbai based on various features such as BHK, area, locality, region, type of property, and more. The project also demonstrates the entire machine learning workflow from data preprocessing to model selection and deployment using Flask.

## Features

- **Data Preprocessing**: Handling missing values, outlier removal using IQR and Z-scores, and scaling features.
- **Categorical Encoding**: Implementation of target encoding and one-hot encoding to convert categorical variables into numerical format.
- **Model Selection**: Hyperparameter tuning using `GridSearchCV` for Linear Regression, Decision Tree, and Support Vector Regression (SVR) models.
- **Deployment**: The best-performing model is deployed using a Flask web application, allowing users to input data and receive house price predictions.

## Getting Started

### Prerequisites

- **Python 3.10.x**
- **pip**: Python package installer

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ML-Project-House-Prediction.git
   cd ML-Project-House-Prediction
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv myEnv
   ```

3. **Activate the virtual environment**:
   - **Linux/Mac**:
     ```bash
     source myEnv/bin/activate
     ```
   - **Windows**:
     ```bash
     myEnv\Scripts\activate
     ```

4. **Install the required packages**:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

### Running the Project

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Access the web application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Input Data**:
   Enter the required details such as BHK, area, locality, region, etc., and click on the "Predict Price" button. The application will return the predicted price of the house based on the input features.

## Project Structure

```plaintext
ML-Project-House-Prediction/
│
├── app.py                     # Main Flask application
├── templates/
│   └── form.html              # HTML form for user input
├── static/
│   └── styles.css             # CSS file for styling (optional)
├── models/
│   ├── best_model_regression.pkl       # Trained model
│   ├── min_max_scaler.pkl              # Scaler object
│   ├── locality_encoding_map.pkl       # Encoding maps
│   ├── region_encoding_map.pkl         # Encoding maps
│   ├── unique_values_locality.json     # JSON file for locality dropdown
│   └── unique_values_region.json       # JSON file for region dropdown
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation (this file)
```

## Model Training

The model training involves several steps, including data preprocessing, scaling, encoding, and model selection. The training process is detailed in the Jupyter notebook provided within the project.

- **Data Preprocessing**:
  - Conversion of price units (Lakh and Crore) to INR.
  - Outlier removal using IQR and Z-scores.
  - Categorical encoding using target encoding and one-hot encoding.

- **Model Selection**:
  - Hyperparameter tuning using `GridSearchCV` for three different models: Linear Regression, Decision Tree Regressor, and Support Vector Regression (SVR).
  - The best model is selected based on cross-validation scores and is saved as a `.pkl` file for deployment.

## Deployment

The trained model is deployed using a Flask web application. The application allows users to input features of a house and receive a predicted price.

## Contributing

Contributions are welcome! If you have any ideas, feel free to fork the repository and submit a pull request.

## Acknowledgements

- Special thanks to [Viraj Pitale](https://www.kaggle.com/code/virajpitale/mumbai-house-price-prediction/notebook) for providing inspiration and insights through the Kaggle notebook.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Workings

- **Data Loading**:

The dataset containing Mumbai house prices is loaded into the system using pandas to perform various operations.
- **Data Preprocessing**:

Prices are converted to a standard INR format (Lakhs and Crores are converted into numerical values).
Outliers in numerical columns (such as area and price) are removed using the IQR method and Z-score filtering to ensure the data is clean.
Categorical variables like locality and region are grouped based on frequency to handle low-count categories efficiently.
- **Feature Engineering**:

Target encoding is applied to locality and region features by calculating the mean price for each group.
One-hot encoding is used for categorical features such as status, age, and type to transform them into binary values suitable for the model.
- **Model Training**:

Three models (Linear Regression, Decision Tree Regressor, and Support Vector Regression) are tested using GridSearchCV to find the best hyperparameters.
The Decision Tree Regressor (DTR) is selected as the best model based on the highest cross-validation score.
The trained model and preprocessing steps (like scaling and encoding) are saved for later use.
- **Model Deployment**:

The model is deployed via a Flask web application, where users can input property details (BHK, area, locality, region, etc.) through a form.
Upon receiving user input, the backend applies the same preprocessing steps (scaling and encoding) before feeding the data into the trained DTR model.
- **Prediction**:

The trained Decision Tree Regressor model predicts the house price based on the processed input.
The result is displayed to the user as a predicted house price in INR.
- **User Interface**:

A simple form-based frontend (HTML/CSS) allows users to input property details.
The Flask app processes the data, predicts the house price, and displays the result on the webpage.
