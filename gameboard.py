import pygame as pg


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.init()

class Gameboard:
    def __init__(self):
        self.screen = pg.display.set_mode((600, 600))
        pg.display.set_caption('Tic-tac-toe')
        self.screen.fill(BLACK)
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
                        color=WHITE,
                        start_pos=item[0],
                        end_pos=item[1],
                        width=2)
            
    
    def add_marker(self):
        pass