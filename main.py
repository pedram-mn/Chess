import pygame as pg
from pygame.locals import *
import random, sys

screen = pg.display.set_mode((900, 700))
pg.display.set_caption('Chess Pro')
board = pg.image.load("board.png")
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
pos_b = {sarbaz_b1: [189, 479], sarbaz_b2: [259, 479], sarbaz_b3: [329, 479], sarbaz_b4: [399, 479],
         sarbaz_b5: [471, 479], sarbaz_b6: [542, 479], sarbaz_b7: [612, 479], sarbaz_b8: [682, 479],
         rokh_b1: [189, 546], rokh_b2: [682, 546], asb_b1: [259, 543], asb_b2: [612, 543], fil_b1: [329, 543],
         fil_b2: [542, 543], vazir_b: [400, 543], shah_b: [471, 543]}
pos_w = {sarbaz_w1: [189, 164], sarbaz_w2: [259, 164], sarbaz_w3: [329, 164], sarbaz_w4: [399, 164],
         sarbaz_w5: [471, 164], sarbaz_w6: [542, 164], sarbaz_w7: [612, 164], sarbaz_w8: [682, 164],
         rokh_w1: [189, 102], rokh_w2: [682, 102], asb_w1: [259, 100], asb_w2: [612, 100], fil_w1: [329, 100],
         fil_w2: [542, 100], vazir_w: [399, 100], shah_w: [471, 100]}

sarbaz_b1_move = [[pos_b[sarbaz_b1][0] + 70, pos_b[sarbaz_b1][1] - 64], [pos_b[sarbaz_b1][0] - 70, pos_b[sarbaz_b1][1] - 64],
                  [pos_b[sarbaz_b1][0], pos_b[sarbaz_b1][1] - 64], [pos_b[sarbaz_b1][0], pos_b[sarbaz_b1][1] - 128]]
sarbaz_b2_move = [[pos_b[sarbaz_b2][0] + 70, pos_b[sarbaz_b2][1] - 64], [pos_b[sarbaz_b2][0] - 70, pos_b[sarbaz_b2][1] - 64],
                  [pos_b[sarbaz_b2][0], pos_b[sarbaz_b2][1] - 64], [pos_b[sarbaz_b2][0], pos_b[sarbaz_b2][1] - 128]]
sarbaz_b3_move = [[pos_b[sarbaz_b3][0] + 70, pos_b[sarbaz_b3][1] - 64], [pos_b[sarbaz_b3][0] - 70, pos_b[sarbaz_b3][1] - 64],
                  [pos_b[sarbaz_b3][0], pos_b[sarbaz_b3][1] - 64], [pos_b[sarbaz_b3][0], pos_b[sarbaz_b3][1] - 128]]
sarbaz_b4_move = [[pos_b[sarbaz_b4][0] + 70, pos_b[sarbaz_b4][1] - 64], [pos_b[sarbaz_b4][0] - 70, pos_b[sarbaz_b4][1] - 64],
                  [pos_b[sarbaz_b4][0], pos_b[sarbaz_b4][1] - 64], [pos_b[sarbaz_b4][0], pos_b[sarbaz_b4][1] - 128]]
sarbaz_b5_move = [[pos_b[sarbaz_b5][0] + 70, pos_b[sarbaz_b5][1] - 64], [pos_b[sarbaz_b5][0] - 70, pos_b[sarbaz_b5][1] - 64],
                  [pos_b[sarbaz_b5][0], pos_b[sarbaz_b5][1] - 64], [pos_b[sarbaz_b5][0], pos_b[sarbaz_b5][1] - 128]]
sarbaz_b6_move = [[pos_b[sarbaz_b6][0] + 70, pos_b[sarbaz_b6][1] - 64], [pos_b[sarbaz_b6][0] - 70, pos_b[sarbaz_b6][1] - 64],
                  [pos_b[sarbaz_b6][0], pos_b[sarbaz_b6][1] - 64], [pos_b[sarbaz_b6][0], pos_b[sarbaz_b6][1] - 128]]
sarbaz_b7_move = [[pos_b[sarbaz_b7][0] + 70, pos_b[sarbaz_b7][1] - 64], [pos_b[sarbaz_b7][0] - 70, pos_b[sarbaz_b7][1] - 64],
                  [pos_b[sarbaz_b7][0], pos_b[sarbaz_b7][1] - 64], [pos_b[sarbaz_b7][0], pos_b[sarbaz_b7][1] - 128]]
sarbaz_b8_move = [[pos_b[sarbaz_b8][0] + 70, pos_b[sarbaz_b8][1] - 64], [pos_b[sarbaz_b8][0] - 70, pos_b[sarbaz_b8][1] - 64],
                  [pos_b[sarbaz_b8][0], pos_b[sarbaz_b8][1] - 64], [pos_b[sarbaz_b8][0], pos_b[sarbaz_b8][1] - 128]]


def show():
    screen.blit(board, (0, 0))
    screen.blit(sarbaz_b1, tuple(pos_b[sarbaz_b1]))
    screen.blit(sarbaz_b2, tuple(pos_b[sarbaz_b2]))
    screen.blit(sarbaz_b3, tuple(pos_b[sarbaz_b3]))
    screen.blit(sarbaz_b4, tuple(pos_b[sarbaz_b4]))
    screen.blit(sarbaz_b5, tuple(pos_b[sarbaz_b5]))
    screen.blit(sarbaz_b6, tuple(pos_b[sarbaz_b6]))
    screen.blit(sarbaz_b7, tuple(pos_b[sarbaz_b7]))
    screen.blit(sarbaz_b8, tuple(pos_b[sarbaz_b8]))
    screen.blit(shah_b, tuple(pos_b[shah_b]))
    screen.blit(vazir_b, tuple(pos_b[vazir_b]))
    screen.blit(fil_b1, tuple(pos_b[fil_b1]))
    screen.blit(fil_b2, tuple(pos_b[fil_b2]))
    screen.blit(asb_b1, tuple(pos_b[asb_b1]))
    screen.blit(asb_b2, tuple(pos_b[asb_b2]))
    screen.blit(rokh_b1, tuple(pos_b[rokh_b1]))
    screen.blit(rokh_b2, tuple(pos_b[rokh_b2]))

    screen.blit(sarbaz_w1, tuple(pos_w[sarbaz_w1]))
    screen.blit(sarbaz_w2, tuple(pos_w[sarbaz_w2]))
    screen.blit(sarbaz_w3, tuple(pos_w[sarbaz_w3]))
    screen.blit(sarbaz_w4, tuple(pos_w[sarbaz_w4]))
    screen.blit(sarbaz_w5, tuple(pos_w[sarbaz_w5]))
    screen.blit(sarbaz_w6, tuple(pos_w[sarbaz_w6]))
    screen.blit(sarbaz_w7, tuple(pos_w[sarbaz_w7]))
    screen.blit(sarbaz_w8, tuple(pos_w[sarbaz_w8]))
    screen.blit(shah_w, tuple(pos_w[shah_w]))
    screen.blit(vazir_w, tuple(pos_w[vazir_w]))
    screen.blit(fil_w1, tuple(pos_w[fil_w1]))
    screen.blit(fil_w2, tuple(pos_w[fil_w2]))
    screen.blit(asb_w1, tuple(pos_w[asb_w1]))
    screen.blit(asb_w2, tuple(pos_w[asb_w2]))
    screen.blit(rokh_w1, tuple(pos_w[rokh_w1]))
    screen.blit(rokh_w2, tuple(pos_w[rokh_w2]))


def check_marble_b(x_range, y_range):
    x_range_f = x_range[0]
    x_range_e = x_range[1]
    y_range_f = y_range[0]
    y_range_e = y_range[1]
    marbles = pos_b.keys()
    res = False
    for i in marbles:
        if pos_b[i][0] in range(x_range_f, x_range_e) and pos_b[i][1] in range(y_range_f, y_range_e):
            res = True
            break
    return res


show()
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    mouse_pos = pg.mouse.get_pos()
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(97, 159):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((169, 238), (97, 159)):
                pg.draw.lines(screen, "Orange", True, [(169, 97), (238, 97), (238, 159), (169, 159)], 3)
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(97, 159):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((240, 307), (97, 159)):
                pg.draw.lines(screen, "Orange", True, [(240, 97), (307, 97), (307, 159), (240, 159)], 3)
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(97, 159):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((310, 378), (97, 159)):
                pg.draw.lines(screen, "Orange", True, [(310, 97), (378, 97), (378, 159), (310, 159)], 3)
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(97, 159):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((381, 448), (97, 159)):
                pg.draw.lines(screen, "Orange", True, [(381, 97), (448, 97), (448, 159), (381, 159)], 3)
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(97, 159):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((451, 519), (97, 159)):
                pg.draw.lines(screen, "Orange", True, [(451, 97), (519, 97), (519, 159), (451, 159)], 3)
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(97, 159):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((521, 590), (97, 159)):
                pg.draw.lines(screen, "Orange", True, [(521, 97), (590, 97), (590, 159), (521, 159)], 3)
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(97, 159):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((592, 661), (97, 159)):
                pg.draw.lines(screen, "Orange", True, [(592, 97), (661, 97), (661, 159), (592, 159)], 3)
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(97, 159):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((663, 731), (97, 159)):
                pg.draw.lines(screen, "Orange", True, [(663, 97), (731, 97), (731, 159), (663, 159)], 3)
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(162, 222):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((169, 238), (162, 222)):
                pg.draw.lines(screen, "Orange", True, [(169, 162), (238, 162), (238, 222), (169, 222)], 3)
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(162, 222):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((240, 307), (162, 222)):
                pg.draw.lines(screen, "Orange", True, [(240, 162), (307, 162), (307, 222), (240, 222)], 3)
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(162, 222):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((310, 378), (162, 222)):
                pg.draw.lines(screen, "Orange", True, [(310, 162), (378, 162), (378, 222), (310, 222)], 3)
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(162, 222):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((381, 448), (162, 222)):
                pg.draw.lines(screen, "Orange", True, [(381, 162), (448, 162), (448, 222), (381, 222)], 3)
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(162, 222):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((451, 519), (162, 222)):
                pg.draw.lines(screen, "Orange", True, [(451, 162), (519, 162), (519, 222), (451, 222)], 3)
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(162, 222):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((521, 590), (162, 222)):
                pg.draw.lines(screen, "Orange", True, [(521, 162), (590, 162), (590, 222), (521, 222)], 3)
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(162, 222):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((592, 661), (162, 222)):
                pg.draw.lines(screen, "Orange", True, [(592, 162), (661, 162), (661, 222), (592, 222)], 3)
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(162, 222):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((663, 731), (162, 222)):
                pg.draw.lines(screen, "Orange", True, [(663, 162), (731, 162), (731, 222), (663, 222)], 3)
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(224, 285):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((169, 238), (224, 285)):
                pg.draw.lines(screen, "Orange", True, [(169, 224), (238, 224), (238, 285), (169, 285)], 3)
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(224, 285):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((240, 307), (224, 285)):
                pg.draw.lines(screen, "Orange", True, [(240, 224), (287, 224), (287, 285), (240, 285)], 3)
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(224, 285):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((310, 378), (224, 285)):
                pg.draw.lines(screen, "Orange", True, [(310, 224), (378, 224), (378, 285), (310, 285)], 3)
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(224, 285):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((381, 448), (224, 285)):
                pg.draw.lines(screen, "Orange", True, [(381, 224), (448, 224), (448, 285), (381, 285)], 3)
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(224, 285):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((451, 519), (224, 285)):
                pg.draw.lines(screen, "Orange", True, [(451, 224), (519, 224), (519, 285), (451, 285)], 3)
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(224, 285):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((521, 590), (224, 285)):
                pg.draw.lines(screen, "Orange", True, [(521, 224), (590, 224), (590, 285), (521, 285)], 3)
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(224, 285):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((592, 661), (224, 285)):
                pg.draw.lines(screen, "Orange", True, [(592, 224), (661, 224), (661, 285), (592, 285)], 3)
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(224, 285):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((663, 731), (224, 285)):
                pg.draw.lines(screen, "Orange", True, [(663, 224), (731, 224), (731, 285), (663, 285)], 3)
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(287, 348):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((169, 238), (287, 348)):
                pg.draw.lines(screen, "Orange", True, [(169, 287), (238, 287), (238, 348), (169, 348)], 3)
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(287, 348):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((240, 307), (287, 348)):
                pg.draw.lines(screen, "Orange", True, [(240, 287), (307, 287), (307, 348), (240, 348)], 3)
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(287, 348):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((310, 378), (287, 348)):
                pg.draw.lines(screen, "Orange", True, [(310, 287), (378, 287), (378, 348), (310, 348)], 3)
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(287, 348):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((381, 448), (287, 348)):
                pg.draw.lines(screen, "Orange", True, [(381, 287), (448, 287), (448, 348), (381, 348)], 3)
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(287, 348):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((451, 519), (287, 348)):
                pg.draw.lines(screen, "Orange", True, [(451, 287), (519, 287), (519, 348), (451, 348)], 3)
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(287, 348):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((521, 590), (287, 348)):
                pg.draw.lines(screen, "Orange", True, [(521, 287), (590, 287), (590, 348), (521, 348)], 3)
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(287, 348):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((592, 661), (287, 348)):
                pg.draw.lines(screen, "Orange", True, [(592, 287), (661, 287), (661, 348), (592, 348)], 3)
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(287, 348):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((663, 731), (287, 348)):
                pg.draw.lines(screen, "Orange", True, [(663, 287), (731, 287), (731, 348), (663, 348)], 3)
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(350, 412):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((169, 238), (350, 412)):
                pg.draw.lines(screen, "Orange", True, [(169, 350), (238, 350), (238, 412), (169, 412)], 3)
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(350, 412):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((240, 307), (350, 412)):
                pg.draw.lines(screen, "Orange", True, [(240, 350), (307, 350), (307, 412), (240, 412)], 3)
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(350, 412):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((310, 378), (350, 412)):
                pg.draw.lines(screen, "Orange", True, [(310, 350), (378, 350), (378, 412), (310, 412)], 3)
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(350, 412):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((381, 448), (350, 412)):
                pg.draw.lines(screen, "Orange", True, [(381, 350), (448, 350), (448, 412), (381, 412)], 3)
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(350, 412):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((451, 519), (350, 412)):
                pg.draw.lines(screen, "Orange", True, [(451, 350), (519, 350), (519, 412), (451, 412)], 3)
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(350, 412):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((521, 590), (350, 412)):
                pg.draw.lines(screen, "Orange", True, [(521, 350), (590, 350), (590, 412), (521, 412)], 3)
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(350, 412):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((592, 661), (350, 412)):
                pg.draw.lines(screen, "Orange", True, [(592, 350), (661, 350), (661, 412), (592, 412)], 3)
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(350, 412):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((663, 731), (350, 412)):
                pg.draw.lines(screen, "Orange", True, [(663, 350), (731, 350), (731, 412), (663, 412)], 3)
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(414, 475):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((169, 238), (414, 475)):
                pg.draw.lines(screen, "Orange", True, [(169, 414), (238, 414), (238, 475), (169, 475)], 3)
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(414, 475):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((240, 307), (414, 475)):
                pg.draw.lines(screen, "Orange", True, [(240, 414), (307, 414), (307, 475), (240, 475)], 3)
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(414, 475):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((310, 378), (414, 475)):
                pg.draw.lines(screen, "Orange", True, [(310, 414), (378, 414), (378, 475), (310, 475)], 3)
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(414, 475):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((381, 448), (414, 475)):
                pg.draw.lines(screen, "Orange", True, [(381, 414), (448, 414), (448, 475), (381, 475)], 3)
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(414, 475):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((451, 519), (414, 475)):
                pg.draw.lines(screen, "Orange", True, [(451, 414), (519, 414), (519, 475), (451, 475)], 3)
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(414, 475):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((521, 590), (414, 475)):
                pg.draw.lines(screen, "Orange", True, [(521, 414), (590, 414), (590, 475), (521, 475)], 3)
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(414, 475):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((592, 661), (414, 475)):
                pg.draw.lines(screen, "Orange", True, [(592, 414), (661, 414), (661, 475), (592, 475)], 3)
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(414, 475):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((663, 731), (414, 475)):
                pg.draw.lines(screen, "Orange", True, [(663, 414), (731, 414), (731, 475), (663, 475)], 3)
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(477, 538):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((169, 238), (477, 538)):
                pg.draw.lines(screen, "Orange", True, [(169, 477), (238, 477), (238, 538), (169, 538)], 3)
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(477, 538):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((240, 307), (477, 538)):
                pg.draw.lines(screen, "Orange", True, [(240, 477), (307, 477), (307, 538), (240, 538)], 3)
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(477, 538):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((310, 378), (477, 538)):
                pg.draw.lines(screen, "Orange", True, [(310, 477), (378, 477), (378, 538), (310, 538)], 3)
                sarbaz_b3.set_alpha(150)
                for i in sarbaz_b3_move:
                    screen.blit(sarbaz_b3, tuple(i))
                sarbaz_b3.set_alpha(20000)
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(477, 538):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((381, 448), (477, 538)):
                pg.draw.lines(screen, "Orange", True, [(381, 477), (448, 477), (448, 538), (381, 538)], 3)
                sarbaz_b4.set_alpha(150)
                for i in sarbaz_b4_move:
                    screen.blit(sarbaz_b4, tuple(i))
                sarbaz_b4.set_alpha(500)

    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(477, 538):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((451, 519), (477, 538)):
                pg.draw.lines(screen, "Orange", True, [(451, 477), (519, 477), (519, 538), (451, 538)], 3)
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(477, 538):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((521, 590), (477, 538)):
                pg.draw.lines(screen, "Orange", True, [(521, 477), (590, 477), (590, 538), (521, 538)], 3)
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(477, 538):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((592, 661), (477, 538)):
                pg.draw.lines(screen, "Orange", True, [(592, 477), (661, 477), (661, 538), (592, 538)], 3)
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(477, 538):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((663, 731), (477, 538)):
                pg.draw.lines(screen, "Orange", True, [(663, 477), (731, 477), (731, 538), (663, 538)], 3)
    if mouse_pos[0] in range(169, 238) and mouse_pos[1] in range(541, 602):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((169, 238), (541, 602)):
                pg.draw.lines(screen, "Orange", True, [(169, 541), (238, 541), (238, 602), (169, 602)], 3)
    if mouse_pos[0] in range(240, 307) and mouse_pos[1] in range(541, 602):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((240, 307), (541, 602)):
                pg.draw.lines(screen, "Orange", True, [(240, 541), (307, 541), (307, 602), (240, 602)], 3)
    if mouse_pos[0] in range(310, 378) and mouse_pos[1] in range(541, 602):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((310, 378), (541, 602)):
                pg.draw.lines(screen, "Orange", True, [(310, 541), (378, 541), (378, 602), (310, 602)], 3)
    if mouse_pos[0] in range(381, 448) and mouse_pos[1] in range(541, 602):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((381, 448), (541, 602)):
                pg.draw.lines(screen, "Orange", True, [(381, 541), (448, 541), (448, 602), (381, 602)], 3)
    if mouse_pos[0] in range(451, 519) and mouse_pos[1] in range(541, 602):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((451, 519), (541, 602)):
                pg.draw.lines(screen, "Orange", True, [(451, 541), (519, 541), (519, 602), (451, 602)], 3)
    if mouse_pos[0] in range(521, 590) and mouse_pos[1] in range(541, 602):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((521, 590), (541, 602)):
                pg.draw.lines(screen, "Orange", True, [(521, 541), (590, 541), (590, 602), (521, 602)], 3)
    if mouse_pos[0] in range(592, 661) and mouse_pos[1] in range(541, 602):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((592, 661), (541, 602)):
                pg.draw.lines(screen, "Orange", True, [(592, 541), (661, 541), (661, 602), (592, 602)], 3)
    if mouse_pos[0] in range(663, 731) and mouse_pos[1] in range(541, 602):
        if pg.mouse.get_pressed()[0]:
            show()
            if check_marble_b((663, 731), (541, 602)):
                pg.draw.lines(screen, "Orange", True, [(663, 541), (731, 541), (731, 602), (663, 602)], 3)
    pg.display.update()
