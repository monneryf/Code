from urllib.request import urlopen

doc = urlopen("http://www.python.org").read( )

print(doc)




