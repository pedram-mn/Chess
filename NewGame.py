import pygame as pg

# load main board of game
board = pg.image.load("board.png")
# --------load black pieces images----------
pa_b1 = pg.image.load("b\\pa b.png")
pa_b2 = pg.image.load("b\\pa b.png")
pa_b3 = pg.image.load("b\\pa b.png")
pa_b4 = pg.image.load("b\\pa b.png")
pa_b5 = pg.image.load("b\\pa b.png")
pa_b6 = pg.image.load("b\\pa b.png")
pa_b7 = pg.image.load("b\\pa b.png")
pa_b8 = pg.image.load("b\\pa b.png")
kn_b1 = pg.image.load("b\\kn b.png")
kn_b2 = pg.image.load("b\\kn b.png")
bi_b1 = pg.image.load("b\\bi b.png")
bi_b2 = pg.image.load("b\\bi b.png")
ro_b1 = pg.image.load("b\\ro b.png")
ro_b2 = pg.image.load("b\\ro b.png")
qu_b = pg.image.load("b\\qu b.png")
ki_b = pg.image.load("b\\ki b.png")
# --------load white pieces images----------
pa_w1 = pg.image.load("w\\pa w.png")
pa_w2 = pg.image.load("w\\pa w.png")
pa_w3 = pg.image.load("w\\pa w.png")
pa_w4 = pg.image.load("w\\pa w.png")
pa_w5 = pg.image.load("w\\pa w.png")
pa_w6 = pg.image.load("w\\pa w.png")
pa_w7 = pg.image.load("w\\pa w.png")
pa_w8 = pg.image.load("w\\pa w.png")
kn_w1 = pg.image.load("w\\kn w.png")
kn_w2 = pg.image.load("w\\kn w.png")
bi_w1 = pg.image.load("w\\bi w.png")
bi_w2 = pg.image.load("w\\bi w.png")
ro_w1 = pg.image.load("w\\ro w.png")
ro_w2 = pg.image.load("w\\ro w.png")
qu_w = pg.image.load("w\\qu w.png")
ki_w = pg.image.load("w\\ki w.png")

# defining positions of each piece
pos_b = {"pa_b1": [189, 478], "pa_b2": [259, 478], "pa_b3": [329, 478], "pa_b4": [399, 478], "pa_b5": [469, 478],
         "pa_b6": [539, 478], "pa_b7": [609, 478], "pa_b8": [679, 478], "ro_b1": [189, 541], "ro_b2": [679, 541],
         "kn_b1": [259, 541], "kn_b2": [609, 541], "bi_b1": [329, 541], "bi_b2": [539, 541], "qu_b": [399, 541],
         "ki_b": [469, 541]}
pos_w = {"pa_w1": [189, 163], "pa_w2": [259, 163], "pa_w3": [329, 163], "pa_w4": [399, 163], "pa_w5": [471, 163],
         "pa_w6": [542, 163], "pa_w7": [612, 163], "pa_w8": [682, 163], "ro_w1": [189, 102], "ro_w2": [682, 102],
         "kn_w1": [259, 100], "kn_w2": [612, 100], "bi_w1": [329, 100], "bi_w2": [542, 100], "qu_w": [399, 100],
         "ki_w": [471, 100]}
pos_blocks = {"a1": ((169, 238), (541, 602)), "b1": ((240, 307), (541, 602)), "c1": ((310, 378), (541, 602)),
              "d1": ((381, 448), (541, 602)), "e1": ((451, 519), (541, 602)), "f1": ((521, 590), (541, 602)),
              "g1": ((592, 661), (541, 602)), "h1": ((663, 731), (541, 602)), "a2": ((169, 238), (477, 538)),
              "b2": ((240, 307), (477, 538)), "c2": ((310, 378), (477, 538)), "d2": ((381, 448), (477, 538)),
              "e2": ((451, 519), (477, 538)), "f2": ((521, 590), (477, 538)), "g2": ((592, 661), (477, 538)),
              "h2": ((663, 731), (477, 538)), "a3": ((169, 238), (414, 475)), "b3": ((240, 307), (414, 475)),
              "c3": ((310, 378), (414, 475)), "d3": ((381, 448), (414, 475)), "e3": ((451, 519), (414, 475)),
              "f3": ((521, 590), (414, 475)), "g3": ((592, 661), (414, 475)), "h3": ((663, 731), (414, 475)),
              "a4": ((169, 238), (350, 412)), "b4": ((240, 307), (350, 412)), "c4": ((310, 378), (350, 412)),
              "d4": ((381, 448), (350, 412)), "e4": ((451, 519), (350, 412)), "f4": ((521, 590), (350, 412)),
              "g4": ((592, 661), (350, 412)), "h4": ((663, 731), (350, 412)), "a5": ((169, 238), (287, 348)),
              "b5": ((240, 307), (287, 348)), "c5": ((310, 378), (287, 348)), "d5": ((381, 448), (287, 348)),
              "e5": ((451, 519), (287, 348)), "f5": ((521, 590), (287, 348)), "g5": ((592, 661), (287, 348)),
              "h5": ((663, 731), (287, 348)), "a6": ((169, 238), (224, 285)), "b6": ((240, 307), (224, 285)),
              "c6": ((310, 378), (224, 285)), "d6": ((381, 448), (224, 285)), "e6": ((451, 519), (224, 285)),
              "f6": ((521, 590), (224, 285)), "g6": ((592, 661), (224, 285)), "h6": ((663, 731), (224, 285)),
              "a7": ((169, 238), (162, 222)), "b7": ((240, 307), (162, 222)), "c7": ((310, 378), (162, 222)),
              "d7": ((381, 448), (162, 222)), "e7": ((451, 519), (162, 222)), "f7": ((521, 590), (162, 222)),
              "g7": ((592, 661), (162, 222)), "h7": ((663, 731), (162, 222)), "a8": ((169, 238), (97, 159)),
              "b8": ((240, 307), (97, 159)), "c8": ((310, 378), (97, 159)), "d8": ((381, 448), (97, 159)),
              "e8": ((451, 519), (97, 159)), "f8": ((521, 590), (97, 159)), "g8": ((592, 661), (97, 159)),
              "h8": ((663, 731), (97, 159))}
# defining move coordinates of each piece
pa_b1_move = [[pos_b["pa_b1"][0] + 70, pos_b["pa_b1"][1] - 63], [pos_b["pa_b1"][0] - 70, pos_b["pa_b1"][1] - 63],
              [pos_b["pa_b1"][0], pos_b["pa_b1"][1] - 63], [pos_b["pa_b1"][0], pos_b["pa_b1"][1] - 126]]
pa_b2_move = [[pos_b["pa_b2"][0] + 70, pos_b["pa_b2"][1] - 63], [pos_b["pa_b2"][0] - 70, pos_b["pa_b2"][1] - 63],
              [pos_b["pa_b2"][0], pos_b["pa_b2"][1] - 63], [pos_b["pa_b2"][0], pos_b["pa_b2"][1] - 126]]
pa_b3_move = [[pos_b["pa_b3"][0] + 70, pos_b["pa_b3"][1] - 63], [pos_b["pa_b3"][0] - 70, pos_b["pa_b3"][1] - 63],
              [pos_b["pa_b3"][0], pos_b["pa_b3"][1] - 63], [pos_b["pa_b3"][0], pos_b["pa_b3"][1] - 126]]
pa_b4_move = [[pos_b["pa_b4"][0] + 70, pos_b["pa_b4"][1] - 63], [pos_b["pa_b4"][0] - 70, pos_b["pa_b4"][1] - 63],
              [pos_b["pa_b4"][0], pos_b["pa_b4"][1] - 63], [pos_b["pa_b4"][0], pos_b["pa_b4"][1] - 126]]
pa_b5_move = [[pos_b["pa_b5"][0] + 70, pos_b["pa_b5"][1] - 63], [pos_b["pa_b5"][0] - 70, pos_b["pa_b5"][1] - 63],
              [pos_b["pa_b5"][0], pos_b["pa_b5"][1] - 63], [pos_b["pa_b5"][0], pos_b["pa_b5"][1] - 126]]
pa_b6_move = [[pos_b["pa_b6"][0] + 70, pos_b["pa_b6"][1] - 63], [pos_b["pa_b6"][0] - 70, pos_b["pa_b6"][1] - 63],
              [pos_b["pa_b6"][0], pos_b["pa_b6"][1] - 63], [pos_b["pa_b6"][0], pos_b["pa_b6"][1] - 126]]
pa_b7_move = [[pos_b["pa_b7"][0] + 70, pos_b["pa_b7"][1] - 63], [pos_b["pa_b7"][0] - 70, pos_b["pa_b7"][1] - 63],
              [pos_b["pa_b7"][0], pos_b["pa_b7"][1] - 63], [pos_b["pa_b7"][0], pos_b["pa_b7"][1] - 126]]
pa_b8_move = [[pos_b["pa_b8"][0] + 70, pos_b["pa_b8"][1] - 63], [pos_b["pa_b8"][0] - 70, pos_b["pa_b8"][1] - 63],
              [pos_b["pa_b8"][0], pos_b["pa_b8"][1] - 63], [pos_b["pa_b8"][0], pos_b["pa_b8"][1] - 126]]
ro_b1_move = [[pos_b["ro_b1"][0] + 70, pos_b["ro_b1"][1]], [pos_b["ro_b1"][0] + 140, pos_b["ro_b1"][1]],
              [pos_b["ro_b1"][0] + 210, pos_b["ro_b1"][1]], [pos_b["ro_b1"][0] + 280, pos_b["ro_b1"][1]],
              [pos_b["ro_b1"][0] + 350, pos_b["ro_b1"][1]], [pos_b["ro_b1"][0] + 420, pos_b["ro_b1"][1]],
              [pos_b["ro_b1"][0] + 490, pos_b["ro_b1"][1]], [pos_b["ro_b1"][0] - 70, pos_b["ro_b1"][1]],
              [pos_b["ro_b1"][0] - 140, pos_b["ro_b1"][1]], [pos_b["ro_b1"][0] - 210, pos_b["ro_b1"][1]],
              [pos_b["ro_b1"][0] - 280, pos_b["ro_b1"][1]], [pos_b["ro_b1"][0] - 350, pos_b["ro_b1"][1]],
              [pos_b["ro_b1"][0] - 420, pos_b["ro_b1"][1]], [pos_b["ro_b1"][0] - 490, pos_b["ro_b1"][1]],
              [pos_b["ro_b1"][0], pos_b["ro_b1"][1] + 63], [pos_b["ro_b1"][0], pos_b["ro_b1"][1] + 126],
              [pos_b["ro_b1"][0], pos_b["ro_b1"][1] + 189], [pos_b["ro_b1"][0], pos_b["ro_b1"][1] + 252],
              [pos_b["ro_b1"][0], pos_b["ro_b1"][1] + 315], [pos_b["ro_b1"][0], pos_b["ro_b1"][1] + 378],
              [pos_b["ro_b1"][0], pos_b["ro_b1"][1] + 441], [pos_b["ro_b1"][0], pos_b["ro_b1"][1] - 63],
              [pos_b["ro_b1"][0], pos_b["ro_b1"][1] - 126], [pos_b["ro_b1"][0], pos_b["ro_b1"][1] - 189],
              [pos_b["ro_b1"][0], pos_b["ro_b1"][1] - 252], [pos_b["ro_b1"][0], pos_b["ro_b1"][1] - 315],
              [pos_b["ro_b1"][0], pos_b["ro_b1"][1] - 378], [pos_b["ro_b1"][0], pos_b["ro_b1"][1] - 441]]
ro_b2_move = [[pos_b["ro_b2"][0] + 70, pos_b["ro_b2"][1]], [pos_b["ro_b2"][0] + 140, pos_b["ro_b2"][1]],
              [pos_b["ro_b2"][0] + 210, pos_b["ro_b2"][1]], [pos_b["ro_b2"][0] + 280, pos_b["ro_b2"][1]],
              [pos_b["ro_b2"][0] + 350, pos_b["ro_b2"][1]], [pos_b["ro_b2"][0] + 420, pos_b["ro_b2"][1]],
              [pos_b["ro_b2"][0] + 490, pos_b["ro_b2"][1]], [pos_b["ro_b2"][0] - 70, pos_b["ro_b2"][1]],
              [pos_b["ro_b2"][0] - 140, pos_b["ro_b2"][1]], [pos_b["ro_b2"][0] - 210, pos_b["ro_b2"][1]],
              [pos_b["ro_b2"][0] - 280, pos_b["ro_b2"][1]], [pos_b["ro_b2"][0] - 350, pos_b["ro_b2"][1]],
              [pos_b["ro_b2"][0] - 420, pos_b["ro_b2"][1]], [pos_b["ro_b2"][0] - 490, pos_b["ro_b2"][1]],
              [pos_b["ro_b2"][0], pos_b["ro_b2"][1] + 63], [pos_b["ro_b2"][0], pos_b["ro_b2"][1] + 126],
              [pos_b["ro_b2"][0], pos_b["ro_b2"][1] + 189], [pos_b["ro_b2"][0], pos_b["ro_b2"][1] + 252],
              [pos_b["ro_b2"][0], pos_b["ro_b2"][1] + 315], [pos_b["ro_b2"][0], pos_b["ro_b2"][1] + 378],
              [pos_b["ro_b2"][0], pos_b["ro_b2"][1] + 441], [pos_b["ro_b2"][0], pos_b["ro_b2"][1] - 63],
              [pos_b["ro_b2"][0], pos_b["ro_b2"][1] - 126], [pos_b["ro_b2"][0], pos_b["ro_b2"][1] - 189],
              [pos_b["ro_b2"][0], pos_b["ro_b2"][1] - 252], [pos_b["ro_b2"][0], pos_b["ro_b2"][1] - 315],
              [pos_b["ro_b2"][0], pos_b["ro_b2"][1] - 378], [pos_b["ro_b2"][0], pos_b["ro_b2"][1] - 441]]
kn_b1_move = [[pos_b["kn_b1"][0] - 70, pos_b["kn_b1"][1] - 126], [pos_b["kn_b1"][0] + 70, pos_b["kn_b1"][1] - 126],
              [pos_b["kn_b1"][0] + 140, pos_b["kn_b1"][1] - 63], [pos_b["kn_b1"][0] + 140, pos_b["kn_b1"][1] + 63],
              [pos_b["kn_b1"][0] + 70, pos_b["kn_b1"][1] + 126], [pos_b["kn_b1"][0] - 70, pos_b["kn_b1"][1] + 126],
              [pos_b["kn_b1"][0] - 140, pos_b["kn_b1"][1] + 63], [pos_b["kn_b1"][0] - 140, pos_b["kn_b1"][1] - 63],
              ]
kn_b2_move = [[pos_b["kn_b2"][0] + 70, pos_b["kn_b2"][1] + 126], [pos_b["kn_b2"][0] + 140, pos_b["kn_b2"][1] + 63],
              [pos_b["kn_b2"][0] + 140, pos_b["kn_b2"][1] - 63], [pos_b["kn_b2"][0] + 70, pos_b["kn_b2"][1] - 126],
              [pos_b["kn_b2"][0] - 70, pos_b["kn_b2"][1] - 126], [pos_b["kn_b2"][0] - 140, pos_b["kn_b2"][1] - 63],
              [pos_b["kn_b2"][0] - 140, pos_b["kn_b2"][1] + 63], [pos_b["kn_b2"][0] - 70, pos_b["kn_b2"][1] + 126]]
bi_b1_move = [[pos_b["bi_b1"][0] + 70, pos_b["bi_b1"][1] - 63], [pos_b["bi_b1"][0] + 140, pos_b["bi_b1"][1] - 126],
              [pos_b["bi_b1"][0] + 210, pos_b["bi_b1"][1] - 189], [pos_b["bi_b1"][0] + 280, pos_b["bi_b1"][1] - 252],
              [pos_b["bi_b1"][0] + 350, pos_b["bi_b1"][1] - 315], [pos_b["bi_b1"][0] + 420, pos_b["bi_b1"][1] - 378],
              [pos_b["bi_b1"][0] + 490, pos_b["bi_b1"][1] - 441], [pos_b["bi_b1"][0] + 70, pos_b["bi_b1"][1] + 63],
              [pos_b["bi_b1"][0] + 140, pos_b["bi_b1"][1] + 126], [pos_b["bi_b1"][0] + 210, pos_b["bi_b1"][1] + 189],
              [pos_b["bi_b1"][0] + 280, pos_b["bi_b1"][1] + 252], [pos_b["bi_b1"][0] + 350, pos_b["bi_b1"][1] + 315],
              [pos_b["bi_b1"][0] + 420, pos_b["bi_b1"][1] + 378], [pos_b["bi_b1"][0] + 490, pos_b["bi_b1"][1] + 441],
              [pos_b["bi_b1"][0] - 70, pos_b["bi_b1"][1] + 63], [pos_b["bi_b1"][0] - 140, pos_b["bi_b1"][1] + 126],
              [pos_b["bi_b1"][0] - 210, pos_b["bi_b1"][1] + 189], [pos_b["bi_b1"][0] - 280, pos_b["bi_b1"][1] + 252],
              [pos_b["bi_b1"][0] - 350, pos_b["bi_b1"][1] + 315], [pos_b["bi_b1"][0] - 420, pos_b["bi_b1"][1] + 378],
              [pos_b["bi_b1"][0] - 490, pos_b["bi_b1"][1] + 441], [pos_b["bi_b1"][0] - 70, pos_b["bi_b1"][1] - 63],
              [pos_b["bi_b1"][0] - 140, pos_b["bi_b1"][1] - 126], [pos_b["bi_b1"][0] - 210, pos_b["bi_b1"][1] - 189],
              [pos_b["bi_b1"][0] - 280, pos_b["bi_b1"][1] - 252], [pos_b["bi_b1"][0] - 350, pos_b["bi_b1"][1] - 315],
              [pos_b["bi_b1"][0] - 420, pos_b["bi_b1"][1] - 378], [pos_b["bi_b1"][0] - 490, pos_b["bi_b1"][1] - 441]]
bi_b2_move = [[pos_b["bi_b2"][0] + 70, pos_b["bi_b2"][1] - 63], [pos_b["bi_b2"][0] + 140, pos_b["bi_b2"][1] - 126],
              [pos_b["bi_b2"][0] + 210, pos_b["bi_b2"][1] - 189], [pos_b["bi_b2"][0] + 280, pos_b["bi_b2"][1] - 252],
              [pos_b["bi_b2"][0] + 350, pos_b["bi_b2"][1] - 315], [pos_b["bi_b2"][0] + 420, pos_b["bi_b2"][1] - 378],
              [pos_b["bi_b2"][0] + 490, pos_b["bi_b2"][1] - 441], [pos_b["bi_b2"][0] + 70, pos_b["bi_b2"][1] + 63],
              [pos_b["bi_b2"][0] + 140, pos_b["bi_b2"][1] + 126], [pos_b["bi_b2"][0] + 210, pos_b["bi_b2"][1] + 189],
              [pos_b["bi_b2"][0] + 280, pos_b["bi_b2"][1] + 252], [pos_b["bi_b2"][0] + 350, pos_b["bi_b2"][1] + 315],
              [pos_b["bi_b2"][0] + 420, pos_b["bi_b2"][1] + 378], [pos_b["bi_b2"][0] + 490, pos_b["bi_b2"][1] + 441],
              [pos_b["bi_b2"][0] - 70, pos_b["bi_b2"][1] + 63], [pos_b["bi_b2"][0] - 140, pos_b["bi_b2"][1] + 126],
              [pos_b["bi_b2"][0] - 210, pos_b["bi_b2"][1] + 189], [pos_b["bi_b2"][0] - 280, pos_b["bi_b2"][1] + 252],
              [pos_b["bi_b2"][0] - 350, pos_b["bi_b2"][1] + 315], [pos_b["bi_b2"][0] - 420, pos_b["bi_b2"][1] + 378],
              [pos_b["bi_b2"][0] - 490, pos_b["bi_b2"][1] + 441], [pos_b["bi_b2"][0] - 70, pos_b["bi_b2"][1] - 63],
              [pos_b["bi_b2"][0] - 140, pos_b["bi_b2"][1] - 126], [pos_b["bi_b2"][0] - 210, pos_b["bi_b2"][1] - 189],
              [pos_b["bi_b2"][0] - 280, pos_b["bi_b2"][1] - 252], [pos_b["bi_b2"][0] - 350, pos_b["bi_b2"][1] - 315],
              [pos_b["bi_b2"][0] - 420, pos_b["bi_b2"][1] - 378], [pos_b["bi_b2"][0] - 490, pos_b["bi_b2"][1] - 441]]
qu_b_move = [[pos_b["qu_b"][0] + 70, pos_b["qu_b"][1]], [pos_b["qu_b"][0] + 140, pos_b["qu_b"][1]],
             [pos_b["qu_b"][0] + 210, pos_b["qu_b"][1]], [pos_b["qu_b"][0] + 280, pos_b["qu_b"][1]],
             [pos_b["qu_b"][0] + 350, pos_b["qu_b"][1]], [pos_b["qu_b"][0] + 420, pos_b["qu_b"][1]],
             [pos_b["qu_b"][0] + 490, pos_b["qu_b"][1]], [pos_b["qu_b"][0] - 70, pos_b["qu_b"][1]],
             [pos_b["qu_b"][0] - 140, pos_b["qu_b"][1]], [pos_b["qu_b"][0] - 210, pos_b["qu_b"][1]],
             [pos_b["qu_b"][0] - 280, pos_b["qu_b"][1]], [pos_b["qu_b"][0] - 350, pos_b["qu_b"][1]],
             [pos_b["qu_b"][0] - 420, pos_b["qu_b"][1]], [pos_b["qu_b"][0] - 490, pos_b["qu_b"][1]],
             [pos_b["qu_b"][0], pos_b["qu_b"][1] + 63], [pos_b["qu_b"][0], pos_b["qu_b"][1] + 126],
             [pos_b["qu_b"][0], pos_b["qu_b"][1] + 189], [pos_b["qu_b"][0], pos_b["qu_b"][1] + 252],
             [pos_b["qu_b"][0], pos_b["qu_b"][1] + 315], [pos_b["qu_b"][0], pos_b["qu_b"][1] + 378],
             [pos_b["qu_b"][0], pos_b["qu_b"][1] + 441], [pos_b["qu_b"][0], pos_b["qu_b"][1] - 63],
             [pos_b["qu_b"][0], pos_b["qu_b"][1] - 126], [pos_b["qu_b"][0], pos_b["qu_b"][1] - 189],
             [pos_b["qu_b"][0], pos_b["qu_b"][1] - 252], [pos_b["qu_b"][0], pos_b["qu_b"][1] - 315],
             [pos_b["qu_b"][0], pos_b["qu_b"][1] - 378], [pos_b["qu_b"][0], pos_b["qu_b"][1] - 441],
             [pos_b["qu_b"][0] + 70, pos_b["qu_b"][1] + 63],
             [pos_b["qu_b"][0] + 140, pos_b["qu_b"][1] + 126],
             [pos_b["qu_b"][0] + 210, pos_b["qu_b"][1] + 189],
             [pos_b["qu_b"][0] + 280, pos_b["qu_b"][1] + 252],
             [pos_b["qu_b"][0] + 350, pos_b["qu_b"][1] + 315],
             [pos_b["qu_b"][0] + 420, pos_b["qu_b"][1] + 378],
             [pos_b["qu_b"][0] + 490, pos_b["qu_b"][1] + 441],
             [pos_b["qu_b"][0] + 70, pos_b["qu_b"][1] - 63],
             [pos_b["qu_b"][0] + 140, pos_b["qu_b"][1] - 126],
             [pos_b["qu_b"][0] + 210, pos_b["qu_b"][1] - 189],
             [pos_b["qu_b"][0] + 280, pos_b["qu_b"][1] - 252],
             [pos_b["qu_b"][0] + 350, pos_b["qu_b"][1] - 315],
             [pos_b["qu_b"][0] + 420, pos_b["qu_b"][1] - 378],
             [pos_b["qu_b"][0] + 490, pos_b["qu_b"][1] - 441],
             [pos_b["qu_b"][0] - 70, pos_b["qu_b"][1] - 63],
             [pos_b["qu_b"][0] - 140, pos_b["qu_b"][1] - 126],
             [pos_b["qu_b"][0] - 210, pos_b["qu_b"][1] - 189],
             [pos_b["qu_b"][0] - 280, pos_b["qu_b"][1] - 252],
             [pos_b["qu_b"][0] - 350, pos_b["qu_b"][1] - 315],
             [pos_b["qu_b"][0] - 420, pos_b["qu_b"][1] - 378],
             [pos_b["qu_b"][0] - 490, pos_b["qu_b"][1] - 441],
             [pos_b["qu_b"][0] - 70, pos_b["qu_b"][1] + 63],
             [pos_b["qu_b"][0] - 140, pos_b["qu_b"][1] + 126],
             [pos_b["qu_b"][0] - 210, pos_b["qu_b"][1] + 189],
             [pos_b["qu_b"][0] - 280, pos_b["qu_b"][1] + 252],
             [pos_b["qu_b"][0] - 350, pos_b["qu_b"][1] + 315],
             [pos_b["qu_b"][0] - 420, pos_b["qu_b"][1] + 378],
             [pos_b["qu_b"][0] - 490, pos_b["qu_b"][1] + 441]]
ki_b_move = [[pos_b["ki_b"][0], pos_b["ki_b"][1] - 63], [pos_b["ki_b"][0] + 70, pos_b["ki_b"][1] - 63],
             [pos_b["ki_b"][0] + 70, pos_b["ki_b"][1]], [pos_b["ki_b"][0] + 70, pos_b["ki_b"][1] + 63],
             [pos_b["ki_b"][0], pos_b["ki_b"][1] + 63], [pos_b["ki_b"][0] - 70, pos_b["ki_b"][1] + 63],
             [pos_b["ki_b"][0] - 70, pos_b["ki_b"][1]], [pos_b["ki_b"][0] - 70, pos_b["ki_b"][1] - 63]]

move_data = [[], [], ""]
# defining the main function


def Start():
    screen = pg.display.set_mode((900, 700))
    pg.display.set_caption('Chess Pro')

    # defining show function to show pieces in their positions
    def show():
        # blit images to screen
        screen.blit(board, (0, 0))
        screen.blit(pa_b1, tuple(pos_b["pa_b1"]))
        screen.blit(pa_b2, tuple(pos_b["pa_b2"]))
        screen.blit(pa_b3, tuple(pos_b["pa_b3"]))
        screen.blit(pa_b4, tuple(pos_b["pa_b4"]))
        screen.blit(pa_b5, tuple(pos_b["pa_b5"]))
        screen.blit(pa_b6, tuple(pos_b["pa_b6"]))
        screen.blit(pa_b7, tuple(pos_b["pa_b7"]))
        screen.blit(pa_b8, tuple(pos_b["pa_b8"]))
        screen.blit(ki_b, tuple(pos_b["ki_b"]))
        screen.blit(qu_b, tuple(pos_b["qu_b"]))
        screen.blit(bi_b1, tuple(pos_b["bi_b1"]))
        screen.blit(bi_b2, tuple(pos_b["bi_b2"]))
        screen.blit(kn_b1, tuple(pos_b["kn_b1"]))
        screen.blit(kn_b2, tuple(pos_b["kn_b2"]))
        screen.blit(ro_b1, tuple(pos_b["ro_b1"]))
        screen.blit(ro_b2, tuple(pos_b["ro_b2"]))

        screen.blit(pa_w1, tuple(pos_w["pa_w1"]))
        screen.blit(pa_w2, tuple(pos_w["pa_w2"]))
        screen.blit(pa_w3, tuple(pos_w["pa_w3"]))
        screen.blit(pa_w4, tuple(pos_w["pa_w4"]))
        screen.blit(pa_w5, tuple(pos_w["pa_w5"]))
        screen.blit(pa_w6, tuple(pos_w["pa_w6"]))
        screen.blit(pa_w7, tuple(pos_w["pa_w7"]))
        screen.blit(pa_w8, tuple(pos_w["pa_w8"]))
        screen.blit(ki_w, tuple(pos_w["ki_w"]))
        screen.blit(qu_w, tuple(pos_w["qu_w"]))
        screen.blit(bi_w1, tuple(pos_w["bi_w1"]))
        screen.blit(bi_w2, tuple(pos_w["bi_w2"]))
        screen.blit(kn_w1, tuple(pos_w["kn_w1"]))
        screen.blit(kn_w2, tuple(pos_w["kn_w2"]))
        screen.blit(ro_w1, tuple(pos_w["ro_w1"]))
        screen.blit(ro_w2, tuple(pos_w["ro_w2"]))

    # defining movements function to move pieces

    def movements(marble):

        # defining not_in_bw function to check if there is any b or w piece in movement line of pieces
        def not_in_bw(marble, num):
            res = [True, True]
            if marble == "ro_b1":
                if num in range(7):
                    j = 0
                if num in range(7, 14):
                    j = 7
                if num in range(14, 21):
                    j = 14
                if num in range(21, 28):
                    j = 21
                while j < num:
                    if ro_b1_move[j] not in pos_w.values() and ro_b1_move[j] not in pos_b.values():
                        pass
                    else:
                        res[0] = False
                        break
                    j += 1
                if j == num:
                    if ro_b1_move[j] in pos_b.values():
                        res[1] = False
                    else:
                        pass
            if marble == "ro_b2":
                if num in range(7):
                    j = 0
                if num in range(7, 14):
                    j = 7
                if num in range(14, 21):
                    j = 14
                if num in range(21, 28):
                    j = 21
                while j < num:
                    if ro_b2_move[j] not in pos_w.values() and ro_b2_move[j] not in pos_b.values():
                        pass
                    else:
                        res[0] = False
                        break
                    j += 1
                if j == num:
                    if ro_b2_move[j] in pos_b.values():
                        res[1] = False
                    else:
                        pass
            if marble == "bi_b1":
                if num in range(7):
                    j = 0
                if num in range(7, 14):
                    j = 7
                if num in range(14, 21):
                    j = 14
                if num in range(21, 28):
                    j = 21
                while j < num:
                    if bi_b1_move[j] not in pos_w.values() and bi_b1_move[j] not in pos_b.values():
                        pass
                    else:
                        res[0] = False
                        break
                    j += 1
                if j == num:
                    if bi_b1_move[j] in pos_b.values():
                        res[1] = False
                    else:
                        pass
            if marble == "bi_b2":
                if num in range(7):
                    j = 0
                if num in range(7, 14):
                    j = 7
                if num in range(14, 21):
                    j = 14
                if num in range(21, 28):
                    j = 21
                while j < num:
                    if bi_b2_move[j] not in pos_w.values() and bi_b2_move[j] not in pos_b.values():
                        pass
                    else:
                        res[0] = False
                        break
                    j += 1
                if j == num:
                    if bi_b2_move[j] in pos_b.values():
                        res[1] = False
                    else:
                        pass
            if marble == "qu_b":
                if num in range(7):
                    j = 0
                if num in range(7, 14):
                    j = 7
                if num in range(14, 21):
                    j = 14
                if num in range(21, 28):
                    j = 21
                if num in range(28, 35):
                    j = 28
                if num in range(35, 42):
                    j = 35
                if num in range(42, 49):
                    j = 42
                if num in range(49, 56):
                    j = 49
                while j < num:
                    if qu_b_move[j] not in pos_w.values() and qu_b_move[j] not in pos_b.values():
                        pass
                    else:
                        res[0] = False
                        break
                    j += 1
                if j == num:
                    if qu_b_move[j] in pos_b.values():
                        res[1] = False
                    else:
                        pass

            return res
        count = []
        move = []
        if marble != "None":
            if marble == "pa_b1":
                move = pa_b1_move
                if pa_b1_move[0][0] < 680 and pa_b1_move[0][1] > 100 and pa_b1_move[0] in pos_w.values() and \
                        pa_b1_move[0] not in pos_b.values():
                    count += [0]
                if pa_b1_move[1][0] > 189 and pa_b1_move[1][1] > 100 and pa_b1_move[1] in pos_w.values() and \
                        pa_b1_move[0] not in pos_b.values():
                    count += [1]
                if pa_b1_move[3][1] > 100 and pa_b1_move[2] not in pos_w.values() and pa_b1_move[0] not in \
                        pos_b.values():
                    count += [2]
                if pos_b["pa_b1"] == [189, 478] and [189, 415] not in pos_w.values() and [189,
                                                                                          352] not in pos_w.values():
                    count += [3]
                for i in count:
                    pa_b1.set_alpha(150)
                    screen.blit(pa_b1, tuple(pa_b1_move[i]))
                    pa_b1.set_alpha(20000)
            if marble == "pa_b2":
                move = pa_b2_move
                if pa_b2_move[0][0] < 680 and pa_b2_move[0][1] > 100 and pa_b2_move[0] in pos_w.values() and \
                        pa_b2_move[0] not in pos_b.values():
                    count += [0]
                if pa_b2_move[1][0] > 189 and pa_b2_move[1][1] > 100 and pa_b2_move[1] in pos_w.values() and \
                        pa_b2_move[0] not in pos_b.values():
                    count += [1]
                if pa_b2_move[3][1] > 100 and pa_b2_move[2] not in pos_w.values() and pa_b2_move[0] not in \
                        pos_b.values():
                    count += [2]
                if pos_b["pa_b2"] == [259, 478] and [259, 415] not in pos_w.values() and [259,
                                                                                          352] not in pos_w.values():
                    count += [3]
                for i in count:
                    pa_b2.set_alpha(150)
                    screen.blit(pa_b2, tuple(pa_b2_move[i]))
                    pa_b2.set_alpha(20000)
            if marble == "pa_b3":
                move = pa_b3_move
                if pa_b3_move[0][0] < 680 and pa_b3_move[0][1] > 100 and pa_b3_move[0] in pos_w.values() and \
                        pa_b3_move[0] not in pos_b.values():
                    count += [0]
                if pa_b3_move[1][0] > 189 and pa_b3_move[1][1] > 100 and pa_b3_move[1] in pos_w.values() and \
                        pa_b3_move[0] not in pos_b.values():
                    count += [1]
                if pa_b3_move[3][1] > 100 and pa_b3_move[2] not in pos_w.values() and pa_b3_move[0] not in \
                        pos_b.values():
                    count += [2]
                if pos_b["pa_b3"] == [329, 478] and [329, 415] not in pos_w.values() and [329,
                                                                                          352] not in pos_w.values():
                    count += [3]
                for i in count:
                    pa_b3.set_alpha(150)
                    screen.blit(pa_b3, tuple(pa_b3_move[i]))
                    pa_b3.set_alpha(20000)
            if marble == "pa_b4":
                move = pa_b4_move
                if pa_b4_move[0][0] < 680 and pa_b4_move[0][1] > 100 and pa_b4_move[0] in pos_w.values() and \
                        pa_b4_move[0] not in pos_b.values():
                    count += [0]
                if pa_b4_move[1][0] > 189 and pa_b4_move[1][1] > 100 and pa_b4_move[1] in pos_w.values() and \
                        pa_b4_move[0] not in pos_b.values():
                    count += [1]
                if pa_b4_move[3][1] > 100 and pa_b4_move[2] not in pos_w.values() and pa_b4_move[0] not in \
                        pos_b.values():
                    count += [2]
                if pos_b["pa_b4"] == [399, 478] and [399, 415] not in pos_w.values() and [399,
                                                                                          352] not in pos_w.values():
                    count += [3]
                for i in count:
                    pa_b4.set_alpha(150)
                    screen.blit(pa_b4, tuple(pa_b4_move[i]))
                    pa_b4.set_alpha(20000)
            if marble == "pa_b5":
                move = pa_b5_move
                if pa_b5_move[0][0] < 680 and pa_b5_move[0][1] > 100 and pa_b5_move[0] in pos_w.values() and \
                        pa_b5_move[0] not in pos_b.values():
                    count += [0]
                if pa_b5_move[1][0] > 189 and pa_b5_move[1][1] > 100 and pa_b5_move[1] in pos_w.values() and \
                        pa_b5_move[0] not in pos_b.values():
                    count += [1]
                if pa_b5_move[3][1] > 100 and pa_b5_move[2] not in pos_w.values() and pa_b5_move[1] not in \
                        pos_b.values():
                    count += [2]
                if pos_b["pa_b5"] == [469, 478] and [469, 415] not in pos_w.values() and [469,
                                                                                          352] not in pos_w.values():
                    count += [3]
                for i in count:
                    pa_b5.set_alpha(150)
                    screen.blit(pa_b5, tuple(pa_b5_move[i]))
                    pa_b5.set_alpha(20000)
            if marble == "pa_b6":
                move = pa_b6_move
                if pa_b6_move[0][0] < 680 and pa_b6_move[0][1] > 100 and pa_b6_move[0] in pos_w.values() and \
                        pa_b6_move[0] not in pos_b.values():
                    count += [0]
                if pa_b6_move[1][0] > 189 and pa_b6_move[1][1] > 100 and pa_b6_move[1] in pos_w.values() and \
                        pa_b6_move[0] not in pos_b.values():
                    count += [1]
                if pa_b6_move[3][1] > 100 and pa_b6_move[2] not in pos_w.values() and pa_b8_move[1] not in \
                        pos_b.values():
                    count += [2]
                if pos_b["pa_b6"] == [539, 478] and [539, 415] not in pos_w.values() and [539,
                                                                                          352] not in pos_w.values():
                    count += [3]
                for i in count:
                    pa_b6.set_alpha(150)
                    screen.blit(pa_b6, tuple(pa_b6_move[i]))
                    pa_b6.set_alpha(20000)
            if marble == "pa_b7":
                move = pa_b7_move
                if pa_b7_move[0][0] < 680 and pa_b7_move[0][1] > 100 and pa_b7_move[0] in pos_w.values() and \
                        pa_b7_move[0] not in pos_b.values():
                    count += [0]
                if pa_b7_move[1][0] > 189 and pa_b7_move[1][1] > 100 and pa_b7_move[1] in pos_w.values() and \
                        pa_b7_move[0] not in pos_b.values():
                    count += [1]
                if pa_b7_move[3][1] > 100 and pa_b7_move[2] not in pos_w.values() and pa_b7_move[1] not in \
                        pos_b.values():
                    count += [2]
                if pos_b["pa_b7"] == [609, 478] and [609, 415] not in pos_w.values() and [609,
                                                                                          352] not in pos_b.values():
                    count += [3]
                for i in count:
                    pa_b7.set_alpha(150)
                    screen.blit(pa_b7, tuple(pa_b7_move[i]))
                    pa_b7.set_alpha(20000)
            if marble == "pa_b8":
                move = pa_b8_move
                if pa_b8_move[0][0] < 680 and pa_b8_move[0][1] > 100 and pa_b8_move[0] in pos_w.values() and \
                        pa_b8_move[0] not in pos_b.values():
                    count += [0]
                if pa_b8_move[1][0] > 189 and pa_b8_move[1][1] > 100 and pa_b8_move[1] in pos_w.values() and \
                        pa_b8_move[1] not in pos_b.values():
                    count += [1]
                if pa_b8_move[2][1] > 100 and pa_b8_move[2] not in pos_w.values() and pa_b8_move[2] not in \
                        pos_b.values():
                    count += [2]
                if pos_b["pa_b8"] == [679, 478] and [679, 415] not in pos_w.values() and [679,
                                                                                          352] not in pos_b.values():
                    count += [3]
                for i in count:
                    pa_b8.set_alpha(150)
                    screen.blit(pa_b8, tuple(pa_b8_move[i]))
                    pa_b8.set_alpha(20000)
            if marble == "ro_b1":
                move = ro_b1_move
                for i in range(7):
                    if ro_b1_move[i][0] < 680 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(7, 14):
                    if ro_b1_move[i][0] > 189 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(14, 21):
                    if ro_b1_move[i][1] < 541 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(21, 28):
                    if ro_b1_move[i][1] > 100 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in count:
                    ro_b1.set_alpha(150)
                    screen.blit(ro_b1, tuple(ro_b1_move[i]))
                    ro_b1.set_alpha(20000)
            if marble == "ro_b2":
                move = ro_b2_move
                for i in range(7):
                    if ro_b2_move[i][0] < 680 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(7, 14):
                    if ro_b2_move[i][0] > 189 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(14, 21):
                    if ro_b2_move[i][1] < 541 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(21, 28):
                    if ro_b2_move[i][1] > 100 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in count:
                    ro_b2.set_alpha(150)
                    screen.blit(ro_b2, tuple(ro_b2_move[i]))
                    ro_b2.set_alpha(20000)
            if marble == "kn_b1":
                move = kn_b1_move
                for i in range(8):
                    if 188 < kn_b1_move[i][0] < 680 and 100 < kn_b1_move[i][1] < 541 and \
                            kn_b1_move[i] not in pos_b.values():
                        count += [i]
                for i in count:
                    kn_b1.set_alpha(150)
                    screen.blit(kn_b1, tuple(kn_b1_move[i]))
                    kn_b1.set_alpha(20000)
            if marble == "kn_b2":
                move = kn_b2_move
                for i in range(8):
                    if 188 < kn_b2_move[i][0] < 680 and 100 < kn_b2_move[i][1] < 541 and \
                            kn_b2_move[i] not in pos_b.values():
                        count += [i]
                for i in count:
                    kn_b2.set_alpha(150)
                    screen.blit(kn_b2, tuple(kn_b2_move[i]))
                    kn_b2.set_alpha(20000)
            if marble == "bi_b1":
                move = bi_b1_move
                for i in range(7):
                    if bi_b1_move[i][0] < 680 and bi_b1_move[i][1] > 100 and not_in_bw(marble, i)[0] and not_in_bw(marble,
                                                                                                                   i)[1]:
                        count += [i]
                for i in range(7, 14):
                    if bi_b1_move[i][0] < 680 and bi_b1_move[i][1] < 541 and not_in_bw(marble, i)[0] and not_in_bw(marble,
                                                                                                                   i)[1]:
                        count += [i]
                for i in range(14, 21):
                    if bi_b1_move[i][0] > 188 and bi_b1_move[i][1] < 541 and not_in_bw(marble, i)[0] and not_in_bw(marble,
                                                                                                                   i)[1]:
                        count += [i]
                for i in range(21, 28):
                    if bi_b1_move[i][0] > 188 and bi_b1_move[i][1] > 100 and not_in_bw(marble, i)[0] and not_in_bw(marble,
                                                                                                                   i)[1]:
                        count += [i]
                for i in count:
                    bi_b1.set_alpha(150)
                    screen.blit(bi_b1, tuple(bi_b1_move[i]))
                    bi_b1.set_alpha(20000)
            if marble == "bi_b2":
                move = bi_b2_move
                for i in range(7):
                    if bi_b2_move[i][0] < 680 and bi_b2_move[i][1] > 100 and not_in_bw(marble, i)[0] and not_in_bw(marble,
                                                                                                                   i)[1]:
                        count += [i]
                for i in range(7, 14):
                    if bi_b2_move[i][0] < 680 and bi_b2_move[i][1] < 541 and not_in_bw(marble, i)[0] and not_in_bw(marble,
                                                                                                                   i)[1]:
                        count += [i]
                for i in range(14, 21):
                    if bi_b2_move[i][0] > 188 and bi_b2_move[i][1] < 541 and not_in_bw(marble, i)[0] and not_in_bw(marble,
                                                                                                                   i)[1]:
                        count += [i]
                for i in range(21, 28):
                    if bi_b2_move[i][0] > 188 and bi_b2_move[i][1] > 100 and not_in_bw(marble, i)[0] and not_in_bw(marble,
                                                                                                                   i)[1]:
                        count += [i]
                for i in count:
                    bi_b2.set_alpha(150)
                    screen.blit(bi_b2, tuple(bi_b2_move[i]))
                    bi_b2.set_alpha(20000)
            if marble == "qu_b":
                move = qu_b_move
                for i in range(7):
                    if qu_b_move[i][0] < 680 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(7, 14):
                    if qu_b_move[i][0] > 189 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(14, 21):
                    if qu_b_move[i][1] < 541 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(21, 28):
                    if qu_b_move[i][1] > 100 and not_in_bw(marble, i)[0] and not_in_bw(marble, i)[1]:
                        count += [i]
                for i in range(28, 35):
                    if qu_b_move[i][0] < 680 and qu_b_move[i][1] < 541 and not_in_bw(marble, i)[0] and not_in_bw(
                            marble, i)[1]:
                        count += [i]
                for i in range(35, 42):
                    if qu_b_move[i][0] < 680 and qu_b_move[i][1] > 100 and not_in_bw(marble, i)[0] and not_in_bw(
                            marble, i)[1]:
                        count += [i]
                for i in range(42, 49):
                    if qu_b_move[i][0] > 188 and qu_b_move[i][1] > 100 and not_in_bw(marble, i)[0] and not_in_bw(
                            marble, i)[1]:
                        count += [i]
                for i in range(49, 56):
                    if qu_b_move[i][0] > 188 and qu_b_move[i][1] < 541 and not_in_bw(marble, i)[0] and not_in_bw(
                            marble, i)[1]:
                        count += [i]
                for i in count:
                    qu_b.set_alpha(150)
                    screen.blit(qu_b, tuple(qu_b_move[i]))
                    qu_b.set_alpha(20000)
            if marble == "ki_b":
                move = ki_b_move
                if ki_b_move[0][1] > 100 and ki_b_move[0] not in pos_b.values():
                    count += [0]
                if ki_b_move[1][0] < 680 and ki_b_move[0][1] > 100 and ki_b_move[1] not in pos_b.values():
                    count += [1]
                if ki_b_move[2][0] < 680 and ki_b_move[2] not in pos_b.values():
                    count += [2]
                if ki_b_move[3][0] < 680 and ki_b_move[3][1] < 541 and ki_b_move[3] not in pos_b.values():
                    count += [3]
                if ki_b_move[4][1] < 541 and ki_b_move[4] not in pos_b.values():
                    count += [4]
                if ki_b_move[5][0] > 189 and ki_b_move[5][1] < 541 and ki_b_move[5] not in pos_b.values():
                    count += [5]
                if ki_b_move[6][0] > 189 and ki_b_move[6] not in pos_b.values():
                    count += [6]
                if ki_b_move[7][0] > 189 and ki_b_move[7][1] > 100 and ki_b_move[7] not in pos_b.values():
                    count += [7]
                for i in count:
                    ki_b.set_alpha(150)
                    screen.blit(ki_b, tuple(ki_b_move[i]))
                    ki_b.set_alpha(20000)
            global move_data
            move_data = [move, count, marble]

    def check_marble_b(x_range, y_range):
        x_range_f = x_range[0]
        x_range_e = x_range[1]
        y_range_f = y_range[0]
        y_range_e = y_range[1]
        marbles = pos_b.keys()
        res = [False, "None"]
        for i in marbles:
            if pos_b[i][0] in range(x_range_f, x_range_e) and pos_b[i][1] in range(y_range_f, y_range_e):
                res = [True, i]
                break
        return res

    show()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        mouse_pos = pg.mouse.get_pos()
        for j in pos_blocks.values():
            if mouse_pos[0] in range(j[0][0], j[0][1]) and mouse_pos[1] in range(j[1][0], j[1][1]):
                if pg.mouse.get_pressed(3)[0]:
                    if check_marble_b(j[0], j[1])[1] == "None":
                        for i in move_data[1]:
                            print(move_data[0][i])
                            if move_data[0][i][0] in range(j[0][0], j[0][1]) and move_data[0][i][1] in range(j[1][0], j[1][1]):
                                global pos_b
                                pos_b[move_data[2]][0] = move_data[0][i][0]
                                pos_b[move_data[2]][1] = move_data[0][i][1]
                                print(pos_b[move_data[2]])
                    show()
                    if check_marble_b(j[0], j[1])[0]:
                        pg.draw.lines(screen, "Orange", True,
                                      [(j[0][0], j[1][0]), (j[0][1], j[1][0]), (j[0][1], j[1][1]), (j[0][0], j[1][1])],
                                      3)
                        movements(check_marble_b(j[0], j[1])[1])
                        print(move_data)
        pg.display.update()
