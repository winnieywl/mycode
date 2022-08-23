import requests
url: "https://statsapi.web.nhl.com/api/v1/teams"

url =  "https://statsapi.web.nhl.com/api/v1/teams"

# send a get request save the response 
resp = requests.get(url)
print(type(resp))

print(resp.status_code)
print(resp.json())

# .put
# .post
# . delete
# press i to go into insert mode first, see how it says -- INSERT -- at the bottom? that's the only time you can actually type anything


# you try it:
print("Winnie")



# now press esc, then type :wq and hit enter

