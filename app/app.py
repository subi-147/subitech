from flask import Flask, render_template, request
import numpy as np
import requests
import config
import joblib

# Custom functions for calculations
def weather_fetch(city_name):
    api_key = config.weather_api_key
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}"

    try:
        response = requests.get(complete_url)
        data = response.json()
        if data.get("cod") != 200:
            print("Weather API Error:", data)
            return None, None
        temp = round((data["main"]["temp"] - 273.15), 2)
        humidity = data["main"]["humidity"]
        return temp, humidity
    except Exception as e:
        print(f"Weather fetch exception: {e}")
        return None, None

# Load ML models
crop_recommendation_model = joblib.load(
    'C:/Users/varun/OneDrive/Desktop/Complete Project/app/models/RandomForest.pkl'
)
model = joblib.load(
    'C:/Users/varun/OneDrive/Desktop/Complete Project/app/models/classifier.pkl'
)
ferti = joblib.load(
    'C:/Users/varun/OneDrive/Desktop/Complete Project/app/models/fertilizer.pkl'
)

# Flask App
app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html', title='Harvestor - Home')

@app.route('/crop-recommend')
def crop_recommend():
    return render_template('crop.html', title='Harvestor - Crop Recommendation')

@app.route('/Fertilizer')
def fertilizer_recommendation():
    return render_template('fertilizer.html', title='Harvestor - Fertilizer Suggestion')

@app.route('/about')
def about():
    return render_template('about.html', title='Harvestor - About')

# Crop prediction route
@app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Harvestor - Crop Recommendation'

    if request.method == 'POST':
        try:
            N = int(request.form['nitrogen'])
            P = int(request.form['phosphorous'])
            K = int(request.form['pottasium'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])
            city = request.form.get("city")

            temperature, humidity = weather_fetch(city)
            if temperature is None or humidity is None:
                return render_template('try_again.html', title=title)

            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            prediction = crop_recommendation_model.predict(data)[0]

            return render_template('crop-result.html', prediction=prediction, title=title)

        except Exception as e:
            print(f"Prediction error: {e}")
            return render_template('try_again.html', title=title)

# Fertilizer recommendation route
@app.route('/fertilizer-predict', methods=['POST'])
def fert_recommend():
    title = 'Harvestor - Fertilizer Suggestion'

    if request.method == 'POST':
        try:
            inputs = [
                int(request.form.get('temp')),
                int(request.form.get('humid')),
                int(request.form.get('mois')),
                int(request.form.get('soil')),
                int(request.form.get('crop')),
                int(request.form.get('nitro')),
                int(request.form.get('pota')),
                int(request.form.get('phos'))
            ]

            result = ferti.classes_[model.predict([inputs])[0]]
            return render_template('fertilizer-result.html', x=result, title=title)

        except Exception as e:
            print(f"Fertilizer prediction error: {e}")
            return render_template('try_again.html', title=title)

# Run Flask
if __name__ == "__main__":
    app.run(debug=True)
