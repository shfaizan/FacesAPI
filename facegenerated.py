import urllib.request
# Enter your API key
wp = urllib.request.urlopen("https://api.generated.photos/api/v1/faces?api_key=YourAPIKEY")
pw = wp.read()
print(pw)
#Generate your api key from this website: "https://generated.photos/account#"