# File: TheLegendOfThayer.py
# Authors: CDT Nicolas Rodriguez & CDT Harrison Strickland


##Legend of Zelda Sprites Taken from Spriters-Resource.com ##
## https://www.spriters-resource.com/nes/legendofzelda/ ##


import random
import sys

import pygame
from pygame.locals import *

## Initialize Globals ##
MOVEDISTANCE = 30
WINDOWX = 480
WINDOWY = 530
PLAYER = 0
BOSSESDEFEATED = 0 

## Characters Information: Current Position, Direction, Location, and Health ##

CharacterInfo = {"Player" : (0, 0, "North", "LoadScreen", 100), "Sword":(0, 0, "North", "ArvinGym", 100), "Dean": (0, 0, "North", "ThayerHall", 100), "Comm" :(0, 0, "North", "ThePlain", 100), "Thayer":(0, 0, "North", "SecretDungeon", 100)}

##What map the doors go to##

doorTo = {(210, 400): "ArvinGym" , (240, 400): "ArvinGym", (210, 100):"CentralArea", (240, 100):"CentralArea", (0, 220):"ThePlain", (0, 250):"ThePlain", (450, 220): "CentralArea", (450, 250): "CentralArea"}

##Where the doors are located in each map##

doorsAt = {"CentralArea": [(210, 400), (240, 400), (0, 220), (0, 250)], "ArvinGym" :[(210, 100), (240, 100)], "ThayerHall" :[], "ThePlain" : [(450, 220), (450, 250)]}

##What image to load for each direction##

directionDict = {"North":"playerNorth.PNG" , "South":"playerSouth.PNG", "East":"playerEast.PNG", "West":"playerWest.PNG"}

##Where walls are located for each map##

walls = {"CentralArea" : [(0, 100), (0, 130), (0, 160), (0, 190), (0, 280), (0, 310), (0, 340), (0, 370), (0, 400), (450, 100), (450, 130), (450, 160), (450, 190), (450, 220), (450, 250), (450, 280), (450, 310), (450, 340), (450, 370), (450, 400), (0, 100), (30, 100), (60, 100), (90, 100), (120, 100), (150, 100), (180, 100), (210, 100), (240, 100), (270, 100), (300, 100), (330, 100), (360, 100), (390, 100), (420, 100), (450, 100), (0, 400), (30, 400), (60, 400), (90, 400), (120, 400), (150, 400), (180, 400), (270, 400), (300, 400), (330, 400), (360, 400), (390, 400), (420, 400), (450, 400)],\
		"ArvinGym" : [(0, 100), (0, 130), (0, 160), (0, 190), (0, 220), (0, 250), (0, 280), (0, 310), (0, 340), (0, 370), (0, 400), (450, 100), (450, 130), (450, 160), (450, 190), (450, 220), (450, 250), (450, 280), (450, 310), (450, 340), (450, 370), (450, 400), (0, 100), (30, 100), (60, 100), (90, 100), (120, 100), (150, 100), (180, 100), (270, 100), (300, 100), (330, 100), (360, 100), (390, 100), (420, 100), (450, 100), (0, 400), (30, 400), (60, 400), (90, 400), (120, 400), (150, 400), (180, 400), (210, 400), (240, 400), (270, 400), (300, 400), (330, 400), (360, 400), (390, 400), (420, 400), (450, 400)],\
		"ThayerHall" : [(0, 100), (0, 130), (0, 160), (0, 190), (0, 220), (0, 250), (0, 280), (0, 310), (0, 340), (0, 370), (0, 400), (450, 100), (450, 130), (450, 160), (450, 190), (450, 220), (450, 250), (450, 280), (450, 310), (450, 340), (450, 370), (450, 400), (0, 100), (30, 100), (60, 100), (90, 100), (120, 100), (150, 100), (180, 100), (270, 100), (300, 100), (330, 100), (360, 100), (390, 100), (420, 100), (450, 100), (0, 400), (30, 400), (60, 400), (90, 400), (120, 400), (150, 400), (180, 400), (210, 400), (240, 400), (270, 400), (300, 400), (330, 400), (360, 400), (390, 400), (420, 400), (450, 400)],\
		"ThePlain" : [(0, 100), (0, 130), (0, 160), (0, 190), (0, 220), (0, 250), (0, 280), (0, 310), (0, 340), (0, 370), (0, 400), (450, 100), (450, 130), (450, 160), (450, 190), (450, 280), (450, 310), (450, 340), (450, 370), (450, 400), (0, 100), (30, 100), (60, 100), (90, 100), (120, 100), (150, 100), (180, 100), (210, 100), (240, 100), (270, 100), (300, 100), (330, 100), (360, 100), (390, 100), (420, 100), (450, 100), (0, 400), (30, 400), (60, 400), (90, 400), (120, 400), (150, 400), (180, 400), (210, 400), (240, 400), (270, 400), (300, 400), (330, 400), (360, 400), (390, 400), (420, 400), (450, 400)],\
		"SecretDungeon" : [(0, 100), (0, 130), (0, 160), (0, 190), (0, 220), (0, 250), (0, 280), (0, 310), (0, 340), (0, 370), (0, 400), (450, 100), (450, 130), (450, 160), (450, 190), (450, 280), (450, 310), (450, 340), (450, 370), (450, 400), (0, 100), (30, 100), (60, 100), (90, 100), (120, 100), (150, 100), (180, 100), (210, 100), (240, 100), (270, 100), (300, 100), (330, 100), (360, 100), (390, 100), (420, 100), (450, 100), (0, 400), (30, 400), (60, 400), (90, 400), (120, 400), (150, 400), (180, 400), (210, 400), (240, 400), (270, 400), (300, 400), (330, 400), (360, 400), (390, 400), (420, 400), (450, 400)],\
		}
		
##Map Info for each map, starting position, mapimage, and startingplayer image##

mapInfo = {"CentralArea" : [7 * MOVEDISTANCE, 100 + 9 * MOVEDISTANCE, "CentralArea.png", "playerNorth.png"],\
		   "ArvinGym" : [7 * MOVEDISTANCE, 100 + MOVEDISTANCE, "ArvinGym.png", "playerSouth.png"],\
		   "ThePlain" : [420, 220, "ThePlain.png", "playerWest.png"]\
		  }

## Control Functions ##

def init_main_window(dimensions, caption):
	pygame.init()
	pygame.display.set_caption(caption)
	icon = pygame.image.load('playerSouth.png')
	pygame.display.set_icon(icon)
	return pygame.display.set_mode(dimensions)


def loadMap(NEWMAP, CharacterInfo, PLAYER):	
	CURX, CURY, CURDIR, CURMAP, CURHEALTH = CharacterInfo["Player"]
	CURMAP = NEWMAP
	MAPINFO = mapInfo[CURMAP]
	CURX = MAPINFO[0]
	CURY = MAPINFO[1]
	main_image = pygame.image.load(MAPINFO[2])
	main = main_image.get_rect()
	main.y = 100
	player_image = pygame.image.load(MAPINFO[3])
	player = player_image.get_rect()
	player.x = CURX
	player.y = CURY
	PLAYER = 1
	CharacterInfo["Player"] = (CURX, CURY, CURDIR, CURMAP, CURHEALTH)
	return main_image, main, CharacterInfo, PLAYER, player_image, player

def movePlayer(event, CharacterInfo): 
	CURX, CURY, CURDIR, CURMAP, CURHEALTH = CharacterInfo["Player"]
	if event.key == K_UP:
		if not ((CURX, CURY-MOVEDISTANCE) in walls[CURMAP]): 
			CURDIR = "North"
			CURY = CURY - MOVEDISTANCE
	elif event.key == K_DOWN: 
		if not ((CURX, CURY+MOVEDISTANCE) in walls[CURMAP]):
			CURDIR = "South"
			CURY = CURY + MOVEDISTANCE
	elif event.key == K_LEFT: 
		if not ((CURX - MOVEDISTANCE, CURY) in walls[CURMAP]):	
			CURDIR = "West"
			CURX = CURX - MOVEDISTANCE
	elif event.key == K_RIGHT:
	
		if not ((CURX + MOVEDISTANCE, CURY) in walls[CURMAP]):	
			CURDIR = "East"
			CURX = CURX + MOVEDISTANCE
	CharacterInfo["Player"] = (CURX, CURY, CURDIR, CURMAP, CURHEALTH)
	return CharacterInfo

### Will take the players current position and return the position of the square that took damage	
def getDamage(CharacterInfo): 
	return (DamageX, DamageY)

## Will do damage to whatever is at DamageX, DamageY, and on the same map as the player then update the character's health## 
def doDamage(CharacterInfo, DamageX, DamageY): 
	return CharacterInfo

## Will move the boss to a different square and update their CharacterInfo##
def moveBoss(): 
	return

## Will unlock the final room by changing central areas map info and walls after all three Bosses are deafeated ##
def unlockThayer(mapInfo, walls): 
	return

## Returns HealthBar to Blit based on Character's current health ##
def showHealth(CharacterInfo): 
	return
	
DISPLAYSURF = init_main_window((WINDOWX, WINDOWY), 'The Legend Of Thayer')

main_image = pygame.image.load('fullloadingscreen.png')
main = main_image.get_rect()

while True:
		if BOSSESDEFEATED == 3: 
			unlockThayer(mapInfo, walls)
		for event in pygame.event.get():
			CURX, CURY, CURDIR, CURMAP, CURHEALTH = CharacterInfo["Player"]
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			#If still on loadscreen, load CentralArea ##
			elif event.type == KEYDOWN and CURMAP == "LoadScreen" and event.key == K_RETURN:
				main_image, main, CharacterInfo, PLAYER, player_image, player = loadMap("CentralArea", CharacterInfo, PLAYER)
			#If spacebar is hit, do damage to the square in front of the player #
			elif event.type == KEYDOWN and event.key == K_SPACE: 
				damagex, damagey = getDamage(CURX, CURY, CURDIR)
			#Move player based on arrow key pressed#
			elif event.type == KEYDOWN and event.key != K_RETURN and event.key != K_SPACE: 
				CharacterInfo = movePlayer(event, CharacterInfo)
				CURX, CURY, CURDIR, CURMAP, CURHEALTH = CharacterInfo["Player"]
				if not ((CURX, CURY) in doorsAt[CURMAP]):
					player.x = CURX
					player.y = CURY
					player_image = pygame.image.load(directionDict[CURDIR])
				else: 
					main_image, main, CharacterInfo, PLAYER, player_image, player = loadMap(doorTo[(CURX, CURY)], CharacterInfo, PLAYER)
		

		DISPLAYSURF.fill((0,   0,   0))
		DISPLAYSURF.blit(main_image, main)

		if PLAYER == 1: 
			DISPLAYSURF.blit(player_image, player)

			
		pygame.display.update()