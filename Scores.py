import requests
import pandas as pd
Api_ligue2 = "https://odds.p.rapidapi.com/v4/sports/soccer_france_ligue_two"


def appeler_api (param):
    url = (Api_ligue2)+(param)

    querystring = {"daysFrom": 3}
    headers = {
	"X-RapidAPI-Key": "31a4de273cmshc7c54fcd952327cp1de738jsn930216fdfcc4",
	"X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return(response.text)

score = appeler_api("/scores")

# Charger le fichier JSON dans un DataFrame
df = pd.read_json(score)
# Écrire le DataFrame dans un fichier CSV
df.to_csv('fichier1.csv', index=False) 
# Afficher les 10 premières lignes du DataFrame
print(df.head)  