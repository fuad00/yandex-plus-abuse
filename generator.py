import re
import jwt
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

def generate_coupon():
    # Stage 1
    r = requests.get('https://flocktory.com/interchange/login?ssid=3606&bid=5525', verify=False)
    url_with_token = r.history[0].headers['location']
    urltoken = re.search(r'interchange/(.*?)\?utm_campaign', url_with_token).group(1)

    # Stage 2
    r = requests.get(f'https://flocktory.com/interchange/{urltoken}/?utm_campaign=exchange&utm_source=platformaofd.ru&utm_medium=referral', verify=False)
    authjwttoken = "eyJ" + re.search(r'eyJ(.*?)","requestedOfferId', r.text).group(1)


    # Stage 3
    json_data = {'email': '','campaign-id': '611614','campaign-site-id': '3654','site-id': '3606','login-data': authjwttoken,}
    r = requests.post('https://flocktory.com/interchange/api/accept-exchange-campaign', json=json_data, verify=False)
    jwttoken = "eyJ" + re.search(r'eyJ(.*?)"', r.text).group(1)

    out = jwt.decode(jwttoken, options={"verify_signature": False})
    return out['coupon']['coupon']

if __name__ == '__main__':
    print(f"Купон: {generate_coupon()}\nСрок действия - 7 дней")
