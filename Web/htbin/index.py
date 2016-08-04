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
MUSIC_FOLDER = "C:\\Users\\gtafi\\Desktop\\pi-juke-\\songs\\"
TUNES = glob.glob(MUSIC_FOLDER+"*.mp3") +  glob.glob(MUSIC_FOLDER+"*.m4a")
if len(TUNES) == 0:
    print("No Tunes in your JukeBox!")
    print("Exiting....")
    sys.exit(1)
else:
    print (str(len(TUNES)) + " songs found in your JukeBox")

for tune in TUNES :
    name = nopath( tune )
    noExt = noExtension( name )
    print( "<a href=\"./index.py/?song=songs/" + name +"\">" + noext +"</a")
    print( "<h1><font color=\"06dbo6\">" + name + "</font></h1>" )
    print(" <video width=\"240\" height=\"200\" controls>" )
    print("<source src=\"" + tune + "\" type=\"video/mp4\">" )
    print("<source src=\"" + tune + "\" type=\"video/ogg\">" )
    print("Your browser does not support the video tag.")
    print("</video>")

