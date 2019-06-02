import urllib.request
import json
import textwrap


with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
  text = f.read()
  decodeedText = text.decode('utf-8')
  print(textwrap.fill(decodeedText,width=50))

print()

obj = json.loads(decodeedText)
print(obj['kind'])