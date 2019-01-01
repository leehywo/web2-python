#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi,os,view
form = cgi.FieldStorage()



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
  <form action="process_create.py" method="post">
      <a href="create.py">create</a>
      <p><input type = "text" name = "title" placeholder = "title"></p>
      <p><textarea rows="4" name = "description" placeholder = "description"></textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(
  title=pageId,
  desc = description,
  listStr=view.getList()))