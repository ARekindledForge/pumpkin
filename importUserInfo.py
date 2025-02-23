# Built on Python 3.11

# import module to request APIs
import requests
import json

# TODO Steam does not send password as plain payload. Password is hashed and sent before sending to Steam
# Fill in your details here to be posted to the login form.
payload = {
    'inUserName': 'goldenfiredrake',
    'inUserPass': ''
}

"""
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
jsonAsText = open("./sample_user_libraries/sample_owned_games_output_1.json", "r", encoding="utf8") 
allGames = json.loads(jsonAsText.read())
print(allGames)