import requests

def getRequest(url):
    json_data = requests.get(url)

    if json_data.status_code == 404:
        return {'success': False}

    dict_data = json_data.json()
    return dict_data