#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi,os
form = cgi.FieldStorage()

files = os.listdir('data')
listStr = ''
for item in files:
  listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name = item)

if 'id' in form:
  pageId = form["id"].value
  description = open('data/'+pageId,'r').read()
else : 
  pageId = 'welcome'
  description = 'Hello, Web2 - Python'

print('''
<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <h2>{title}</h2>
  <p>{desc}
  </p>
</body>
</html>
'''.format(title=pageId,desc = description,listStr=listStr))