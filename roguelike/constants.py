import tcod as libtcod
import pygame

pygame.init()

'''Game size'''
CAMERA_WIDTH = 800
CAMERA_HEIGHT = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

#FPS LIMIT
GAME_FPS = 60

#MAP VARS
MAP_WIDTH = 100
MAP_HEIGHT = 100
MAP_MAX_NUM_ROOMS = 25
MAP_NUM_LEVELS = 10

#ROOM LIMITATIONS
ROOM_MAX_HEIGHT = 7
ROOM_MIN_HEIGHT = 3
ROOM_MAX_WIDTH = 5
ROOM_MIN_WIDTH = 3


#Color defs
COLOUR_BLACK = (0,0,0)
COLOUR_WHITE = (255,255,255)
COLOUR_GREY = (100,100,100)
COLOUR_DGREY = (50,50,50)
COLOUR_RED = (255,0,0)
COLOUR_GREEN = (0,255,0)
COLOUR_PURPLE = (106,13,173)
COLOUR_YELLOW = (255,255,0)
COLOUR_DEFAULT_BG = (100,100,100)

#GAme colors
COLOUR_DEFAULT_BF = COLOUR_GREY

#FOV SETTIGNS
FOV_ALGO = libtcod.FOV_BASIC
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 8


#MESSAGE DEFAULTS
NUM_MESSAGES = 4

FONT_TITLE_SCREEN_OUTLINE = pygame.font.Font("data/harry_p.ttf", 49)
FONT_TITLE_SCREEN = pygame.font.Font("data/harry_p.ttf", 48)
FONT_CREDITS = pygame.font.Font("data/harry_p.ttf", 25)
FONT_DEBUG_MESSAGE = pygame.font.Font("data/joystix monospace.ttf", 16)
FONT_MESSAGE_TEXT =  pygame.font.Font("data/joystix monospace.ttf", 12)
FONT_CURSOR_TEXT =  pygame.font.Font("data/joystix monospace.ttf", CELL_HEIGHT)

DEPTH_PLAYER = -100
DEPTH_CREATURE = 1 
DEPTH_ITEM = 2
DEPTH_CORPSE = 100
DEPTH_BKGD = 150