import httpx
import json

url: str = "https://power.larc.nasa.gov/api/temporal/daily/point"

parameters = ["ALLSKY_SFC_SW_DWN",
              "CLRSKY_SFC_SW_DWN",
              "ALLSKY_KT",
              "CLOUD_AMT",
              "AOD_55",
              "T2M",
              "T2M_MAX",
              "RH2M",
              "WS10M",
              "PRECTOTCORR"]

param: dict = {
    "start": 20050101,
    "end": 20260131,
    "latitude": 25.3463,
    "longitude": 55.4209, 
    "community": "re",
    "parameters": ",".join(parameters)
}

response = httpx.get(url, params = param)
data = response.json()

with open("data/raw/big_sample_data.json", "w") as files:
    json.dump(data, files, indent = 4)

"""pretty_print = json.dumps(data,indent = 4)
print(pretty_print) """