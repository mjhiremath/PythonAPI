import requests

#get user API
url = 'https://api.github.com/user'


response = requests.get(url,headers={'Authorization': 'Bearer bfcc743ee4211976c82734b074d15b51383e5277'})
#print(response.json())
json2 = response.json()

print(response.url)


# Print the number of duplicate APIs used
url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
my_json = response.json()
print(type(my_json))
url_list = []

# get the urls from dictionary
for photo in my_json:
    #print(photo['url'])
    url_list.append(photo['url'])

#couting the urls
print("Number of urls",len(url_list))

#Removing the duplicates from list using set function
print("Unique urls in photos",len(set(url_list)))


