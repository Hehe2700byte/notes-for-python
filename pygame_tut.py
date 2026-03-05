import pygame as pg

pg.init()
window = pg.display.set_mode((800, 600))
pg.display.set_caption('Hello pygame')
window.fill('red')
pg.display.update()
pg.time.wait(5000)
pg.quit()
