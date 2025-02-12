import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return

    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"Previsão do tempo para {city}:")
    print(f"Condição: {weather}")
    print(f"Temperatura: {temperature}°C")
    print(f"Humidade: {humidity}%")
    print(f"Velocidade do vento: {wind_speed} m/s")

if __name__ == "__main__":
    api_key = "e63ed761e47f5da4d7b610bb5bd83397"
    city = input("Digite o nome da cidade: ")
    get_weather(api_key, city)

