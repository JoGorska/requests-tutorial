import requests

# get with parameters after ?
r = requests.get('https://httpbin.org/get?page=2&count=25')

# proper way to pass the parameters:
payload = {
    'page': 2,
    'count': 25
}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)  # json response

print(r.url)  # gives exactly the same url as manually typed above

# send data via post request. get json response back
payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

print(r.text)

# makes python dictionary out of json response
# this makes data accessible as in python dictionary
r_dict = r.json()
print(r_dict['form'])