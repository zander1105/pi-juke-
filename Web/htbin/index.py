#!/usr/local/bin/python3
import cgi, cgitb
cgitb.enable()

print('Content-type: text/html')
print('''
''')
arguments = cgi.FieldStorage()
for i in arguments.keys():
 print(arguments[i].value)


with open('test.log', mode='w', encoding='utf-8') as f:
  f.write('test succeeded')   
print('success')
# print('Content-type: text/html')
# print('''
# <html>
#      <head>
#           <title>My website</title>
#      </head>
#      <body>
#           <p>Here I am</p>
#      </body>
# </html>
# ''')