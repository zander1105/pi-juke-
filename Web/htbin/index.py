#!/usr/local/bin/python3
import cgitb
cgitb.enable()
with open('test.log', mode='w', encoding='utf-8') as f:
  f.write('test succeeded')   
print('Content-type: text/html')
print('''
<html>
     <head>
          <title>My website</title>
     </head>
     <body>
          <p>Here I am</p>
     </body>
</html>
''')