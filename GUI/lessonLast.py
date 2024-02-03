import requests

url = 'https://blynk.cloud/external/api/get?token=emVG_7OpSVh0rsC0GrOmsXTGAF3-T7TK&v0&v1'

response = requests.get(url)
if response.status_code == 200:
    all_data = response.json()
    print(all_data['v0'])
    print(all_data['v1'])
