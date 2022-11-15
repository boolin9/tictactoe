import pygame as pg


BG_COLOR = (155, 213, 175)
TRIM_COLOR = (216, 245, 231)
BLACK = (0, 0, 0)

pg.init()

class Gameboard:
    def __init__(self):
        self.screen = pg.display.set_mode((600, 600))
        pg.display.set_caption('Tic-tac-toe')
        self.screen.fill(BG_COLOR)
        pg.display.flip()
        self.clock = pg.time.Clock()
        self.state = True
        self.draw_lines()
    
    
    def draw_lines(self):
        lines = [[(200, 0), (200, 600)], 
                 [(400, 0), (400, 600)],
                 [(0, 200), (600, 200)],
                 [(0, 400), (600, 400)]]
        
        for item in lines:
            pg.draw.line(surface=self.screen,
                        color=TRIM_COLOR,
                        start_pos=item[0],
                        end_pos=item[1],
                        width=1)