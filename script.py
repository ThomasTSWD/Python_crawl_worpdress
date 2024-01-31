import json
import requests

base_url = "https://admin.tswd.fr/wp-json/wp/v2/posts?page="
page_num = 1
all_data = []

while True:
    response = requests.get(base_url + str(page_num))
    
    # Vérifiez si la requête a réussi
    if response.status_code != 200:
        print(f"Erreur lors de la récupération de la page {page_num}")
        break

    data = response.json()
    
    # Si la réponse est vide, cela signifie qu'il n'y a pas d'autres pages
    if not data:
        break

    # Ajoutez le contenu JSON à la liste all_data
    for item in data:
        title = item.get("title", {}).get("rendered", "")
        content = item.get("content", {}).get("rendered", "")
        all_data.append({"title": title, "content": content})

    # Augmentez le numéro de page pour la prochaine itération
    page_num += 1

# Sauvegardez le contenu dans un fichier texte
with open("articles.txt", "w", encoding="utf-8") as file:
    for item in all_data:
        file.write("Titre: " + item["title"] + "\n")
        file.write("Contenu: " + item["content"] + "\n\n")
