import random
import requests


def return_random():
    random_number = random.randint(0, 100)
    return random_number


# 返回土味情话
def return_sweets():
    url = 'https://api.lovelive.tools/api/SweetNothings/1/Serialization/Json'
    req = requests.get(url)
    if req.status_code == 200:
        return req.json().get('returnObj')[0]
    else:
        return "对不起，网络出小差了~"
