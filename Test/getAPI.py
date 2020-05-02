import requests
import urllib.request
def test_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200


url = "https://jsonplaceholder.typicode.com/photos"

response = requests.get(url)
print(response)

print("##########################Post method##############################")

jsonPayload = {'albumId':1,'title':'test','url':'hiremath.com','thumbnailUrl':'hiremath.com','id':5001}

response = requests.post(url,json=jsonPayload)
print(response.json())
print(response.request)
print(response.status_code)
assert response.status_code == 201

print("####################Put method###################################")
jsonPayload = {'albumId':1,'title':'test','url':'hiremath.com','thumbnailUrl':'hiremath.com','id':5001}
url = "https://jsonplaceholder.typicode.com/photos/100"
response = requests.put(url,json=jsonPayload)
print(response.json())
print(response.request)
print(response.status_code)
assert response.status_code == 200

print("######################Delete method###########################")
response = requests.delete(url)
print(response.json())
print(response.request)
print(response.status_code)
assert response.status_code == 200