import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convertit la réponse en JSON
    print(data[1]["title"])
else:
    print("Erreur:", response.status_code)