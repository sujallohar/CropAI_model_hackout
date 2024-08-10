import requests
import json
import datetime as dt

def analyze_weather_conditions(weather_data):
    threats = []
    temperature = weather_data['temp']
    humidity = weather_data['humidity']
    rain = weather_data['rain']
    wind_speed = weather_data.get('wind_speed', 0)
    uv_index = weather_data.get('uvi', 0)
    
    if rain == 0 and humidity < 30:
        threats.append("Drought risk")
    if humidity > 70 and temperature > 25:
        threats.append("Pests")
    if temperature in range(45, 53) and humidity >= 70:
        threats.append("Heatwave risk")
    if temperature < 5:
        threats.append("Frost risk")
    elif temperature > 35:
        threats.append("Heat stress")
    if humidity > 80:
        threats.append("Fungal disease risk")
    if rain > 50:
        threats.append("Waterlogging risk")
    if wind_speed > 20:
        threats.append("Strong wind risk")
    if uv_index > 7:
        threats.append("High UV risk")

    return threats

def recommend_crop_protection(threats, crop_type):
    recommendations = []
    
    if "Frost risk" in threats:
        recommendations.append("Cover crops with frost protection cloth")
    if "Heat stress" in threats:
        recommendations.append("Provide shade or irrigation")
    if "Fungal disease risk" in threats:
        recommendations.append("Use resistant varieties or apply fungicides")
    if "Pests" in threats:
        recommendations.append("Identify the pest and apply appropriate pesticide or biocontrol methods")
        recommendations.append("Consider crop rotation and companion planting to deter pests")
    if "Waterlogging risk" in threats:
        recommendations.append("Provide proper watering practices")
    if "Strong wind risk" in threats:
        recommendations.append("Install windbreaks or support structures for crops")
    if "High UV risk" in threats:
        recommendations.append("Reduce sun exposure and consider UV-resistant crop varieties or shade cloth")
    if "Drought risk" in threats:
        recommendations.append("Provide appropriate irrigation practices such as water conservation, use efficient irrigation")
        recommendations.append("Consider drought-tolerant varieties or use drought-resistant crops")
    if "Heatwave risk" in threats:
        recommendations.append("Increase your irrigation frequency and apply mulch to retain soil moisture")

    return recommendations

def get_weather_data(lat, lon, date, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
    params = {
        "lat": lat,
        "lon": lon,
        "dt": int(dt.datetime.strptime(date, "%Y-%m-%d").timestamp()),
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    if 'current' in data:
        return data['current']
    elif 'hourly' in data:
        return data['hourly'][0]
    else:
        return None
