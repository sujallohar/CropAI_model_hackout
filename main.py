from src.data_preprocessing import create_data_generators
from src.model import build_model, train_model
from src.predict import load_trained_model, predict
from src.weather_analysis import analyze_weather_conditions, recommend_crop_protection
import requests

def get_weather_data(lat, lon, date, api_key):
    """Fetches current weather data for a given location using WeatherAPI.

    Args:
        lat: Latitude of the location.
        lon: Longitude of the location.
        date: Date for which weather data is required (YYYY-MM-DD).
        api_key: API key for WeatherAPI.

    Returns:
        A dictionary containing weather data.
    """
    url = "https://weatherapi-com.p.rapidapi.com/history.json"
    querystring = {"q": f"{lat},{lon}", "dt": date}
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    if 'forecast' in data and 'forecastday' in data['forecast']:
        return data['forecast']['forecastday'][0]['day']
    else:
        return None  # Handle the case where no data is returned

if __name__ == "__main__":
    # Load and preprocess the data
    train_dir = '/Users/sujalpanchal/Desktop/hackathon/weather_prediction/dataset/train'
    validation_dir = '/Users/sujalpanchal/Desktop/hackathon/weather_prediction/dataset/validation'
    test_dir = '/Users/sujalpanchal/Desktop/hackathon/weather_prediction/dataset/test'
    train_generator, validation_generator, test_generator = create_data_generators(train_dir, validation_dir, test_dir)

    # Build and train the model
    model = build_model(num_classes=len(train_generator.class_indices))
    train_model(model, train_generator, validation_generator)

    # Load the trained model and make predictions
    model = load_trained_model()
    image_path = '/Users/sujalpanchal/Downloads/OIP.GcVVJVPJGzp4u6TIl66SPgHaE8.jpeg'
    prediction = predict(image_path, model)
    print(f'Predicted weather condition: {prediction}')

    # Weather analysis
    api_key_path = '/Users/sujalpanchal/Desktop/hackathon/api_key.txt'
    with open(api_key_path, 'r') as f:
        api_key = f.read().strip()
    lat, lon = 37.7749, -122.4194  # Example coordinates
    date = "2024-08-09"

    weather_data = get_weather_data(lat, lon, date, api_key)
    if weather_data is not None:
        threats = analyze_weather_conditions(weather_data)
        recommendations = recommend_crop_protection(threats, "tomato")
        print(recommendations)
    else:
        print("No weather data available for the given location and date.")