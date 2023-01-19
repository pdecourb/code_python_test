api_key = "zerhzehzezrzer" # si l'api a besoin d'une clé d'authent
city = "Paris"
#lire la doc de l'api (swagger)
url = "http://api.rzehrjzehrzhjz"+city+"&appid="*api_key

request = requests.get(url)
json = request.json() # passe le resultat au format json
print(json)

description = json.get("weather")[0].get("description")
print(description)
