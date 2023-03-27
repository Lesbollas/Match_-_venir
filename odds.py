import requests

Api_ligue2 = "https://odds.p.rapidapi.com/v4/sports/upcoming/odds"


def appeler_api ():
    url = (Api_ligue2)

    querystring = {"regions":"us","oddsFormat":"decimal","markets":"h2h,spreads","dateFormat":"iso"}
    headers = {
	"X-RapidAPI-Key": "31a4de273cmshc7c54fcd952327cp1de738jsn930216fdfcc4",
	"X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return(response.text)


print (appeler_api())
# score = appeler_api()
# print (score)