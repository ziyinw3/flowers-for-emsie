# all tuples for creating rects for character

coords_i3 = []
coords_w3 = []

coords_i2 = []
coords_w2 = []

coords_i1 = []
coords_w1 = []

coords_i0 = []
coords_w0 = []

for i in range(0, 13):
    coords_i3.append((i * 41, 0, i * 41 + 41, 41))

for i in range(0, 17):
    coords_w3.append((i * 41, 41, i * 41 + 41, 41 * 2))

for i in range(0, 13):
    coords_i2.append((i * 41, 41 * 2, i * 41 + 41, 41 * 3))

for i in range(0, 17):
    coords_w2.append((i * 41, 41 * 3, i * 41 + 41, 41 * 4))

for i in range(0, 13):
    coords_i1.append((i * 41, 41 * 4, i * 41 + 41, 41 * 5))

for i in range(0, 17):
    coords_w1.append((i * 41, 41 * 5, i * 41 + 41, 41 * 6))

for i in range(0, 13):
    coords_i0.append((i * 41, 41 * 6, i * 41 + 41, 41 * 7))

for i in range(0, 17):
    coords_w0.append((i * 41, 41 * 7, i * 41 + 41, 41 * 8))


# print(coords_w3)

coords_mm = []

for i in range(0, 6):
    coords_mm.append((i * 640, 0, i * 640 + 640, 480))

# print (coords_mm)

coords_buttonu = []

for i in range(0, 3):
    coords_buttonu.append((i * 128, 0, i * 128 + 128, 52))

coords_buttond = []

for i in range(0, 3):
    coords_buttond.append((i * 128, 52, i * 128 + 128, 2 * 52))

# options menu

coords_op = []

for i in range(0, 2):
    coords_op.append((i * 640, 0, i * 640 + 640, 480))

#coords for flowers that are unhovered

coords_flower_bu = []

for i in range (0, 2):
    coords_flower_bu.append((0, i * 64, 64, 56))

coords_flower_bd = []

for i in range (0, 2):
    coords_flower_bd.append((0, i * 64 + 64, 64, 56 * 2))

print(coords_flower_bu)
print(coords_flower_bd)