import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = "sua_chave_api_aqui"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", data['message'])
            return

        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result_label.config(text=f"Previsão do tempo para {city}:\n"
                            f"Condição: {weather}\n"
                            f"Temperatura: {temperature}°C\n"
                            f"Humidade: {humidity}%\n"
                            f"Velocidade do vento: {wind_speed} m/s")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Previsão do Tempo")
root.geometry("400x300")

city_label = tk.Label(root, text="Digite o nome da cidade:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Buscar", command=get_weather)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=20)

root.mainloop()

