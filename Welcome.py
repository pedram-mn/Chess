import NewGame
import pygame as pg
screen = pg.display.set_mode((900, 700))
pg.display.set_caption('Chess Pro')
welcome = pg.image.load("Welcome.png")
done = False
screen.blit(welcome, (0, 0))
while not done:
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    if pos[0] in range(268, 625) and pos[1] in range(304, 368):
        if pg.mouse.get_pressed()[0]:
            done = True
            NewGame.Start()
    pg.display.update()
