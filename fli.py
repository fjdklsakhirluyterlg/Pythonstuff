
import requests

params = {
  'access_key': '358a253f737ee28824a5817c33661a92'
}

api_result = requests.get('http://api.aviationstack.com/v1/aircraft_types', params)

api_response = api_result.json()

print(api_response)


