import requests
import os


def imei_finder(imei):
    db_url = "https://imeidb.xyz/api/imei/"
    api_token = os.environ.get("api_key")
    header = {"X-Api-Key": api_token,
              "Content-Type": "application/json"}

    imei = str(imei)
    response = requests.get(db_url+imei, headers=header)
    data = response.json()
    try:
        phone_model = data["model"]
        phone_brand = data["brand"]
    except KeyError:
        phone_model = "N/A"
        phone_brand = "N/A"

    return [phone_model, phone_brand]

