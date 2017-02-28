import datetime
import time
import pyglet
import pygame

def getTimestamp():
	return [int(i) for i in datetime.datetime.now().strftime('%Y %m %d %H %M %S').split()]

def alarm(t):
	print("poi?", str(t), getTimestamp())
	pygame.init()
	song = pygame.mixer.Sound('akatsuki/'+str(t)+'.ogg')
	clock = pygame.time.Clock()
	song.play()
	time.sleep(song.get_length()+1)
	pygame.quit()

def execute():
	while 1:
		t = getTimestamp()
		if t[5] == 0 and t[4] == 0:
			alarm(t[3])
			time.sleep(1)
		else:
			time.sleep(1)



if __name__=="__main__":
	# execute()

	for i in range(24):
		alarm(i)