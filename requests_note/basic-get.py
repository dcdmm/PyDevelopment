import requests

url0 = 'https://httpbin.org/get?name=frank&gender=male'

# Sends a GET request.
response = requests.get(url0,
                        # You can tell Requests to stop waiting for a response after a given number of seconds with the timeout parameter.
                        # Nearly all production code should use this parameter in nearly all requests.
                        # Failure to do so can cause your program to hang indefinitely
                        timeout=5)

# Final URL location of Response.
print(response.url)

url1 = 'https://httpbin.org/get'
payload = {'name': 'frank', 'gender': 'male'}
print(requests.get(url1, params=payload).url)  # 与上等价

# Integer Code of responded HTTP Status, e.g. 404 or 200.
print(response.status_code)

# Textual reason of responded HTTP Status, e.g. “Not Found” or “OK”.
print(response.reason)

# Encoding to decode with when accessing r.text.
print(response.encoding)

# Case-insensitive Dictionary of Response Headers. For example, headers['content-encoding'] will return the value of a 'Content-Encoding' response header.
print(response.headers)

'''
Content of the response, in unicode.

If Response.encoding is None, encoding will be guessed using charset_normalizer or chardet.
'''
print(response.text)

# Content of the response, in bytes.
# You can also access the response body as bytes, for non-text requests:
print(response.content)

'''
Returns the json-encoded content of a response, if any.

Parameters **kwargs – Optional arguments that json.loads takes.
Raises  requests.exceptions.JSONDecodeError – If the response body does not contain valid json.
'''
print(response.json())

