import requests

url = 'https://httpbin.org/post'
payload = {"key1": 123,
           "key2": [234, 456]}
r = requests.post(url, data=payload)

print(r.headers)
print(r.json())
