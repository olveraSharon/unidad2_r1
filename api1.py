import urllib.parse
import requests

while True:
    city_name = input("City_name: ")
    if city_name == "salir" or city_name == "s":
        break
    country_code = input("countrycode: ")
    if country_code == "salir" or country_code == "s":
        break

    main_api = "https://api.weatherbit.io/v2.0/current?"
    key = "0c9ea60028cc404bbadadfd41c8c98c1"

    url = main_api + urllib.parse.urlencode({"key": key, "city": city_name, "country": country_code})
    print("URL: " + url)

    try:
        # Realiza la solicitud a la API y obtiene la respuesta en formato JSON
        json_data = requests.get(url).json()

        # Verifica si la solicitud fue exitosa
        if "data" in json_data and len(json_data["data"]) > 0:
            weather_data = json_data["data"][0]

            # Muestra la información relevante
            print("\nWeather information:")
            print(f"Temperature: {weather_data['temp']}°C")
            print(f"Description: {weather_data['weather']['description']}")
            print(f"Humidity: {weather_data['rh']}%")
            print(f"Wind Speed: {weather_data['wind_spd']} m/s")
    except Exception as e:
        print("Error:", e)
