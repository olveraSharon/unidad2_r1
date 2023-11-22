#Autor: Sharon Michelle Olvera Ibarra
#Descripción:Esta API es para obtener tasas de cambio entre
# diferentes monedas Usando una moneda de origen y una moneda de destino 
#y presenta esta información al usuario.
#Fecha: 19/11/2023
import requests
import urllib.parse

exchange_rate_api_url = "https://v6.exchangerate-api.com/v6/4f89a896263cd3ac81f04c04/latest/"
api_key = "4f89a896263cd3ac81f04c04"

while True:
    orig_currency = input("Moneda de origen (Ejemplo USD): ")
    if orig_currency == "quit" or orig_currency == "q":
        break
    dest_currency = input("Moneda de destino (Ejemplo EUR): ")
    if dest_currency == "quit" or dest_currency == "q":
        print("Hasta Luego")
        break

    api_url = f"{exchange_rate_api_url}{orig_currency}"
    params = {"apikey": api_key}

    url = api_url + "?" + urllib.parse.urlencode(params)
    print("URL: " + url)

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["result"] == "success":
            conversion_rate = data["conversion_rates"].get(dest_currency)

            if conversion_rate:
                print(f"1 {orig_currency} = {conversion_rate} {dest_currency}")
            else:
                print(f"No se encontró la tasa de cambio para {dest_currency}")
        else:
            print(f"Error en la solicitud: {data['error-type']}")
    else:
        print(f"Error en la solicitud. Código de estado: {response.status_code}")