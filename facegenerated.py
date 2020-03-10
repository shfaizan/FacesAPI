import urllib.request
# Enter your API key
wp = urllib.request.urlopen("https://api.generated.photos/api/v1/faces?api_key=W2V1uxWklMkLudblcx1WOA")
pw = wp.read()
print(pw)
