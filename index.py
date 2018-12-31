#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi,os
form = cgi.FieldStorage()

def getList():
  files = os.listdir('data')
  listStr = ''
  for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name = item)
  return listStr

if 'id' in form:
  pageId = form["id"].value
  description = open('data/'+pageId,'r').read()
  update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
  delete_action = '''
    <form action="process_delete.py" method="post">
      <input type="hidden" name = "pageId" value={}>
      <input type="submit" value="delete">
    </form>
    '''.format(pageId)
else : 
  pageId = 'welcome'
  description = 'Hello, Web2 - Python'
  update_link = ''
  delete_action = ''

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
  <a href="create.py">create</a>
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}
  </p>
</body>
</html>
'''.format(
  title=pageId,
  desc = description,
  listStr=getList(),
  update_link=update_link,
  delete_action = delete_action))