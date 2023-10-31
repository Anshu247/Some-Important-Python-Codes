import requests

# response = requests.get("https://www.codewithharry.com")
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'professor',
    "body": 'inevitable',
    "userid": 7,
}

headers = {
    'content-type': 'application/json; charset=UTF-8'
}

response = requests.post(url, headers=headers, json=data)
print(response.text)