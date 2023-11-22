#Autor: Sharon Michelle Olvera Ibarra
#Descripción:Esta API proporciona información 
#sobre objetos que se acercan o pasan cerca de la órbita de 
#la Tierra, también conocidos como objetos cercanos a la Tierra (NEO).
#Fecha: 19/11/2023

import requests
import urllib.parse

feed_url = "https://api.nasa.gov/neo/rest/v1/feed"
api_key = "oQtvMndWyWU3zs956e0IwJCwb1zfDd0dOsgHjJVl"

date_ranges = {
    "1": {"start_date": "2015-09-07", "end_date": "2015-09-08"},
    "2": {"start_date": "2015-09-06", "end_date": "2015-09-07"},
}

while True:
    user_input = input("Enter date range code (1, 2, etc.) or type 'salir' or 's' to exit: ")

    if user_input.lower() in ["salir", "s"]:
        print("Hasta luego.")
        break

    if user_input in date_ranges:
        selected_range = date_ranges[user_input]

        url_params = {
            "start_date": selected_range["start_date"],
            "end_date": selected_range["end_date"],
            "api_key": api_key
        }
        api_url = f"{feed_url}?{urllib.parse.urlencode(url_params)}"

        print(f"\nNASA API URL: {api_url}")
        
        response = requests.get(api_url)

        if response.status_code == 200:
            neo_data = response.json()

            for date, neo_list in neo_data["near_earth_objects"].items():
                print(f"\nNear-Earth Objects on {date}:\n")
                for neo in neo_list:
                    print(f"NEO ID: {neo['id']}")
                    print(f"NEO Reference ID: {neo['neo_reference_id']}")
                    print(f"NEO Name: {neo['name']}")
                    print(f"Absolute Magnitude (H): {neo['absolute_magnitude_h']}")

                    diameter_min = neo['estimated_diameter']['kilometers']['estimated_diameter_min']
                    diameter_max = neo['estimated_diameter']['kilometers']['estimated_diameter_max']
                    print(f"Estimated Diameter (km): Min - {diameter_min}, Max - {diameter_max}")
                    print("=============================================")
        else:
            print(f"Error: Unable to retrieve NEO feed. Please check the dates and try again.")
    else:
        print("Invalid code. Please enter a valid code or type 'salir' or 's' to exit.")





