import sys,pygame as pg

pg.init()

WIDTH , HEIGHT = 500,500

SCREEN = pg.display.set_mode((WIDTH,HEIGHT))


def draw_background():
		SCREEN.fill(pg.Color("White"))	#pg.Color() this gives you the list of all kind of color instead of looking for color code you could just write the color name  

		pg.draw.rect(SCREEN,pg.Color("black"),pg.Rect(15,15,470,470),10)

		i = 1
		while i * 

		pg.display.update()








## Main game loop 


def Game_Loop():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		draw_background()	
		pg.display.flip()
	
while True:
	Game_Loop();