from gameboard import Gameboard
import pygame as pg


gb = Gameboard()


class Main:
    def __init__(self) -> None:
        while gb.state:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gb.state = False
                    
            pg.display.update()
            gb.clock.tick(30)


if __name__ == "__main__":
    Main()