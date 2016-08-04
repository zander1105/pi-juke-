import time
import os
import glob
import random
import sys
import vlc
debug = False
def waitTillPlayerFinished( player ):
	state = player.get_state()
	print( state )
	if debug == True:
			print( state )
	while (state == vlc.State.NothingSpecial or
			state == vlc.State.Opening or
			state == vlc.State.Playing ):
		time.sleep( 1 )
		state = player.get_state()

def getFileToPlay( file ):
	fo = open( file, 'r' )
	result = fo.readline();
	result = result.rstrip('\r\n'); 
	fo.close()
	os.remove( file )
	return result

def playASong( tune ):
		print( "Playing" + tune )
		player = vlc.MediaPlayer( tune )
		player.play()
		player.set_fullscreen( True )
		waitTillPlayerFinished( player )
		player.release()

QUEUE_FOLDER = "queue/"
while True:
	QUEUED = glob.glob( QUEUE_FOLDER + "*.txt" )
	if len( QUEUED) > 0:
		QUEUED = sorted( QUEUED )
		for item in QUEUED:
			file = getFileToPlay( item )
			playASong( file )
			print( file )
	else:
		time.sleep( 2 )
