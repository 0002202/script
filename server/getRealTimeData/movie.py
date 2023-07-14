import requests


def get_movie():
    url = 'https://piaofang.maoyan.com/dashboard'
    rep = requests.get(url)

