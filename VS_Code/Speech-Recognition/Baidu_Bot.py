import requests
import pprint
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=OeX7NRSOGwdOQXoWQThUwzp1' \
#        '&client_secret=9O1haDuwOlrx9CLGK1Gc8RVroeVgoI5L'
# res = requests.get(host)
# print(res.status_code)
# if res:
#     pprint.pprint(res.json())

acess_token = '24.9d29eca68f7f49b23bab8d90184932c5.2592000.1586761493.282335-18831425'
url = 'https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token=' + acess_token
post_data = "{\"log_id\":\"UNITTEST_10000\",\"version\":\"2.0\",\"service_id\":\"S10000\",\"session_id\":\"\"," \
            "\"request\":{\"query\":\"你好\",\"user_id\":\"88888\"}}"
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(url, data=post_data.encode(), headers=headers)
print(response.status_code)
if response:
    print(response.json())