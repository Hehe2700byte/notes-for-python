import pygame as pg

pg.init()

window = pg.display.set_mode((800, 600))

pg.display.set_caption('Hello pygame')

window.fill('red')

#draw
pg.draw.line(window, 'blue', (10, 20), (50, 100), 5)
pg.draw.aaline(window, 'blue', (10, 60), (50, 140), 5)
points = [(10, 10), (10, 40), (30, 30)]
pg.draw.lines(window, 'green', True, points, 3)
pg.draw.polygon(window, 'green', points)
'''
pg.draw.rect()
pg.draw.circle()
pg.draw.ellipse()
'''
pg.display.update()
pg.time.wait(5000)
pg.quit()
