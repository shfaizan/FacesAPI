import urllib.request
# Enter your API key
wp = urllib.request.urlopen("https://api.generated.photos/api/v1/faces?api_key=ADD_YOUR_API_KEY")
pw = wp.read()
print(pw)
#Generate your api key from this website: "https://generated.photos/account#"