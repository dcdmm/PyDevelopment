import requests

r0 = requests.post('http://127.0.0.1:5000/get_data', data={"data": 123})

print(r0.headers)
print(r0.text)
print(r0.json())

header = {'Content-Type': 'application/x-www-form-urlencoded'}
r1 = requests.post('http://127.0.0.1:5000/get_data', data={"data": 123},
                   # Custom Headers
                   headers=header)

print(r1.headers)
print(r1.text)
print(r1.json())
