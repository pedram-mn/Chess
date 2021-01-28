import pygame as pg
from pygame.locals import *
import random, sys

screen = pg.display.set_mode((900, 700))
pg.display.set_caption('Chess Pro')
board = pg.image.load("board.png")
screen.blit(board, (0, 0))
##############################################
sarbaz_b1 = pg.image.load("b\sarbaz b.png")
sarbaz_b2 = pg.image.load("b\sarbaz b.png")
sarbaz_b3 = pg.image.load("b\sarbaz b.png")
sarbaz_b4 = pg.image.load("b\sarbaz b.png")
sarbaz_b5 = pg.image.load("b\sarbaz b.png")
sarbaz_b6 = pg.image.load("b\sarbaz b.png")
sarbaz_b7 = pg.image.load("b\sarbaz b.png")
sarbaz_b8 = pg.image.load("b\sarbaz b.png")
asb_b1 = pg.image.load("b\\asb b.png")
asb_b2 = pg.image.load("b\\asb b.png")
fil_b1 = pg.image.load("b\\fil b.png")
fil_b2 = pg.image.load("b\\fil b.png")
rokh_b1 = pg.image.load("b\\rokh b.png")
rokh_b2 = pg.image.load("b\\rokh b.png")
vazir_b = pg.image.load("b\\vazir b.png")
shah_b = pg.image.load("b\\shah b.png")
##############################################
sarbaz_w1 = pg.image.load("w\\sarbaz w.png")
sarbaz_w2 = pg.image.load("w\\sarbaz w.png")
sarbaz_w3 = pg.image.load("w\\sarbaz w.png")
sarbaz_w4 = pg.image.load("w\\sarbaz w.png")
sarbaz_w5 = pg.image.load("w\\sarbaz w.png")
sarbaz_w6 = pg.image.load("w\\sarbaz w.png")
sarbaz_w7 = pg.image.load("w\\sarbaz w.png")
sarbaz_w8 = pg.image.load("w\\sarbaz w.png")
asb_w1 = pg.image.load("w\\asb w.png")
asb_w2 = pg.image.load("w\\asb w.png")
fil_w1 = pg.image.load("w\\fil w.png")
fil_w2 = pg.image.load("w\\fil w.png")
rokh_w1 = pg.image.load("w\\rokh w.png")
rokh_w2 = pg.image.load("w\\rokh w.png")
vazir_w = pg.image.load("w\\vazir w.png")
shah_w = pg.image.load("w\\shah w.png")
##############################################
pos0_b = {sarbaz_b1: [189, 479], sarbaz_b2: [259, 479], sarbaz_b3: [329, 479], sarbaz_b4: [399, 479],
          sarbaz_b5: [471, 479], sarbaz_b6: [542, 479], sarbaz_b7: [612, 479], sarbaz_b8: [682, 479],
          rokh_b1: [189, 546], rokh_b2: [682, 546], asb_b1: [259, 543], asb_b2: [612, 543], fil_b1: [329, 543],
          fil_b2: [542, 543], vazir_b: [399, 543], shah_b: [471, 543]}
pos0_w = {sarbaz_w1: [189, 164], sarbaz_w2: [259,164], sarbaz_w3: [329, 164], sarbaz_w4: [399, 164],
          sarbaz_w5: [471, 164], sarbaz_w6: [542, 164], sarbaz_w7: [612, 164], sarbaz_w8: [682, 164],
          rokh_w1: [189, 102], rokh_w2: [682, 102], asb_w1: [259, 100], asb_w2: [612, 100], fil_w1: [329, 100],
          fil_w2: [542, 100], vazir_w: [399, 100], shah_w: [471, 100]}

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.blit(sarbaz_b1, tuple(pos0_b[sarbaz_b1]))
    screen.blit(sarbaz_b2, tuple(pos0_b[sarbaz_b2]))
    screen.blit(sarbaz_b3, tuple(pos0_b[sarbaz_b3]))
    screen.blit(sarbaz_b4, tuple(pos0_b[sarbaz_b4]))
    screen.blit(sarbaz_b5, tuple(pos0_b[sarbaz_b5]))
    screen.blit(sarbaz_b6, tuple(pos0_b[sarbaz_b6]))
    screen.blit(sarbaz_b7, tuple(pos0_b[sarbaz_b7]))
    screen.blit(sarbaz_b8, tuple(pos0_b[sarbaz_b8]))
    screen.blit(shah_b, tuple(pos0_b[shah_b]))
    screen.blit(vazir_b, tuple(pos0_b[vazir_b]))
    screen.blit(fil_b1, tuple(pos0_b[fil_b1]))
    screen.blit(fil_b2, tuple(pos0_b[fil_b2]))
    screen.blit(asb_b1, tuple(pos0_b[asb_b1]))
    screen.blit(asb_b2, tuple(pos0_b[asb_b2]))
    screen.blit(rokh_b1, tuple(pos0_b[rokh_b1]))
    screen.blit(rokh_b2, tuple(pos0_b[rokh_b2]))

    screen.blit(sarbaz_w1, tuple(pos0_w[sarbaz_w1]))
    screen.blit(sarbaz_w2, tuple(pos0_w[sarbaz_w2]))
    screen.blit(sarbaz_w3, tuple(pos0_w[sarbaz_w3]))
    screen.blit(sarbaz_w4, tuple(pos0_w[sarbaz_w4]))
    screen.blit(sarbaz_w5, tuple(pos0_w[sarbaz_w5]))
    screen.blit(sarbaz_w6, tuple(pos0_w[sarbaz_w6]))
    screen.blit(sarbaz_w7, tuple(pos0_w[sarbaz_w7]))
    screen.blit(sarbaz_w8, tuple(pos0_w[sarbaz_w8]))
    screen.blit(shah_w, tuple(pos0_w[shah_w]))
    screen.blit(vazir_w, tuple(pos0_w[vazir_w]))
    screen.blit(fil_w1, tuple(pos0_w[fil_w1]))
    screen.blit(fil_w2, tuple(pos0_w[fil_w2]))
    screen.blit(asb_w1, tuple(pos0_w[asb_w1]))
    screen.blit(asb_w2, tuple(pos0_w[asb_w2]))
    screen.blit(rokh_w1, tuple(pos0_w[rokh_w1]))
    screen.blit(rokh_w2, tuple(pos0_w[rokh_w2]))
    mouse_pos = pg.mouse.get_pos()
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(97, 159):
        pass
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(97, 159):
        pass
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(97, 159):
        pass
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(97, 159):
        pass
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(97, 159):
        pass
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(97, 159):
        pass
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(97, 159):
        pass
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(97, 159):
        pass
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(162, 222):
        pass
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(162, 222):
        pass
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(162, 222):
        pass
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(162, 222):
        pass
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(162, 222):
        pass
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(162, 222):
        pass
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(162, 222):
        pass
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(162, 222):
        pass
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(224, 285):
        pass
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(224, 285):
        pass
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(224, 285):
        pass
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(224, 285):
        pass
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(224, 285):
        pass
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(224, 285):
        pass
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(224, 285):
        pass
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(224, 285):
        pass
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(287, 348):
        pass
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(287, 348):
        pass
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(287, 348):
        pass
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(287, 348):
        pass
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(287, 348):
        pass
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(287, 348):
        pass
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(287, 348):
        pass
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(287, 348):
        pass
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(350, 412):
        pass
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(350, 412):
        pass
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(350, 412):
        pass
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(350, 412):
        pass
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(350, 412):
        pass
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(350, 412):
        pass
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(350, 412):
        pass
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(350, 412):
        pass
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(414, 475):
        pass
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(414, 475):
        pass
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(414, 475):
        pass
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(414, 475):
        pass
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(414, 475):
        pass
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(414, 475):
        pass
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(414, 475):
        pass
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(414, 475):
        pass
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(477, 538):
        pass
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(477, 538):
        pass
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(477, 538):
        pass
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(477, 538):
        pass
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(477, 538):
        pass
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(477, 538):
        pass
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(477, 538):
        pass
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(477, 538):
        pass
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(541, 602):
        pass
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(541, 602):
        pass
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(541, 602):
        pass
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(541, 602):
        pass
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(541, 602):
        pass
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(541, 602):
        pass
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(541, 602):
        pass
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(541, 602):
        pass

    pg.display.flip()
