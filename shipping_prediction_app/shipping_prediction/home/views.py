from django.shortcuts import render

# Create your views here.
import joblib
import numpy as np
from django.shortcuts import render
from sklearn.preprocessing import LabelEncoder

from shipping_prediction.home.forms import ShippingPredictionForm

# Load the pre-trained model
model = joblib.load('shipping_prediction/home/model_gr.pkl')
scaler = joblib.load('shipping_prediction/home/scaler.pkl')

def preprocess_features(form_data):
    # Initialize LabelEncoders for categorical features
    encoders = {}

    # Transform categorical features
    features = []
    for field, value in form_data.items():
        if field in ['delivery_status', 'shipping_mode', 'order_region', 'order_state', 'order_city', 'order_country', 'customer_city', 'customer_country']:  # Add other categorical fields here
            if field not in encoders:
                encoders[field] = LabelEncoder()
                encoders[field].fit([value])  # Fit encoder on the fly
            features.append(encoders[field].transform([value])[0])
        else:
            features.append(value)

    return np.array(features).reshape(1, -1)

def predict_shipping_days(request):
    if request.method == 'POST':
        form = ShippingPredictionForm(request.POST)
        if form.is_valid():
            # Preprocess the features
            features = preprocess_features(form.cleaned_data)

            # Scale the features using the same scaler used during model training
            features_scaled = scaler.transform(features)

            # Perform the prediction
            prediction = round(model.predict(features_scaled)[0])

            return render(request, 'result.html', {'prediction': prediction})
    else:
        form = ShippingPredictionForm()

    return render(request, 'predict.html', {'form': form})

def home(request):
    return render(request, 'home_page.html')