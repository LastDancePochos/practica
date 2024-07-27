import json
import requests

def get_xr():
    url = 'https://api.bluelytics.com.ar/v2/latest'
    r = requests.get(url)
    data=json.loads(r.text)
    cotizacion = data['oficial']['value_sell']
    return cotizacion