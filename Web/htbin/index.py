#!/usr/bin/python3
# coding: utf-8
import cgi, cgitb
cgitb.enable()
import time
import os
import glob
import random
import sys

print('Content-type: text/html')
print('''
''')

def noExtension( filename ):
    return os.path.splitext( filename )[0]

def noPath( filename ):
    return os.path.basename( filename )

def postQueueToJukebox( song ):
    if song != None:
        fname = "../queue/" + str( time.time()) + ".txt"
        with open(fname, mode='w', encoding='utf-8')as f:
            f.write( song.value )


            #did we query here?
arguments = cgi.FieldStorage()

if "song" in arguments:
    postQueueToJukebox( arguments['song'])
MUSIC_FOLDER = "../songs/"
TUNES = glob.glob(MUSIC_FOLDER+"*.mp3") +  glob.glob(MUSIC_FOLDER+"*.m4a")
if len(TUNES) == 0:
    print("No Tunes in your JukeBox!")
    print("Exiting....")
    sys.exit(1)
else:
    print (str(len(TUNES)) + " songs found in your JukeBox")
    print ("<link type=\"text/css\" rel=\"stylesheet\" href=\"/style.css\">")
    print ("<h1> Pi Juke!</h1>")
for tune in TUNES :
    name = noPath( tune )
    noExt = noExtension( name )
    print( "<h2><a href=\"/htbin/index.py/?song=songs/" + name +"\">" + noExt +"</a>")


