import requests
import json

def api_data(request):
    data = json.loads(requests.get('https://www.mindicador.cl/api').text)
    return {'indicators': data}