import requests

URL = 'https://www.amazon.com/iRobot-Roomba-675-Connectivity-Carpets/dp/B07DL4QY5V/ref=sr_1_3?dchild=1&keywords=roomba&qid=1587854652&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

page = requests.get(URL, headers=headers)