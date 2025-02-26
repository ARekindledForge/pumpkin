import requests
import json

"""
# TODO Steam does not send password as plain payload. Password is hashed and sent before sending to Steam. need to find alternate way to log into Steam
# Fill in your details here to be posted to the login form.
payload = {
    'inUserName': 'goldenfiredrake',
    'inUserPass': ''
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://steamcommunity.com/login/home/?goto=', data=payload)
    # TODO - DEBUG
    
    # print the HTML returned or something more intelligent to see if it's a successful login page.
    f = open("response.html", "w", encoding="utf-8")
    f.write(p.text)
    f.close()
    # print(p.text)
    
    # Get cookies from the session
    cookies = s.cookies

    # Print all cookies
    for cookie in cookies:
        print(f"{cookie.name} = {cookie.value}")

    # Get a specific cookie by name
    specific_cookie = cookies.get("sessionid")
    if specific_cookie:
        print(f"Specific cookie value: {specific_cookie}")

    # fetch list of user games
    # sessionid can only be fetched after steam login
    gameFetchURL = "https://steamcommunity.com/actions/GetOwnedApps/?sessionid=" + specific_cookie
    response = requests.get(gameFetchURL)
    print(response.status_code)
"""
# open sample_owned_games_output_1.json list of dictionary items 
jsonAsText = open("./sample_user_libraries/sample_owned_games_output_1.json", "r", encoding="utf8") 
listOfGames = json.loads(jsonAsText.read())

# create list of game IDs
listOfGameIDs = []
for game in listOfGames:
    listOfGameIDs.append(game["appid"])

dictOfGameGenres = {}
# get game details and put into dict of game Genres
for gameID in listOfGameIDs:
    # TODO Steam's servers limit to 200req/5min; cannot query for list of appids; may need to consider alternative approach
    responseOfDetails = requests.get("https://store.steampowered.com/api/appdetails?appids=" + str(gameID))
    if responseOfDetails.status_code != 200:
        raise Exception("Error Retrieving Game: id:" + str(game["appid"]) + " (" + game["name"] + ") | HTML Code: " + responseOfDetails.status_code)
    dictOfDetails = json.loads(responseOfDetails.text)
    if dictOfDetails[str(gameID)]["success"] == False:
        raise Exception("API failed to return valid app details: " + str(game["appid"] + " | HTML Code: " + str(responseOfDetails.status_code)))
    if dictOfDetails[str(gameID)]["data"]["type"] == "game":
        for genre in dictOfDetails[str(gameID)]["data"]["genres"]:
            try:
                dictOfGameGenres.update({str(genre["description"]) : dictOfGameGenres[str(genre["description"])] + 1})
            except:
                dictOfGameGenres[genre["description"]] = 1
    file = open("genre_profile.txt", "w")
    file.write(json.dumps(dictOfGameGenres))

print(dictOfGameGenres)