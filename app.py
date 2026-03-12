from flask import Flask, request, jsonify
from flask import Flask
import joblib
import pandas as pd
app = Flask(__name__)
# Load the trained linear regression model
model = joblib.load('linear_regression_model.joblib')

# Create a list of column names from the X DataFrame for consistent input
trained_columns = X.columns.tolist()

print("Model loaded successfully.")
print("Trained columns created successfully.")


@app.route('/predict', methods=['POST'])
def predict():
    if not request.json:
        return jsonify({'error': 'Invalid JSON data in request body'}), 400

    raw_data = request.json

    try:
        predicted_price = predict_house_price(raw_data)
        return jsonify({'predicted_price': predicted_price}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# To run the Flask app (for local testing):
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

print("Flask app and '/predict' endpoint defined. Use `app.run()` to start the server.")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
