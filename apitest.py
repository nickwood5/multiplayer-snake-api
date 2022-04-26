import requests

a = requests.get("http://multiplayer-snake-api22-nickwood5-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com/get")

print(a.json())