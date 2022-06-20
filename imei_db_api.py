import requests
import os
from pprint import pprint


db_url = "https://imeidb.xyz/api/imei/"


api_token = os.environ.get("api_key")
header = {"X-Api-Key": api_token,
          "Content-Type": "application/json"}

imei = "350299947364810"
response = requests.get(db_url+imei, headers=header)
pprint(response.json())
data = response.json()
phone_model = data["data"]["device_spec"]["aliases"][0]

