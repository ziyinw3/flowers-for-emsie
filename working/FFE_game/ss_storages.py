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

for j in range(0, 17):
    coords_w3.append((i * 41, 41, i * 41 + 41, 41 * 2))

for k in range(0, 13):
    coords_i2.append((i * 41, 41 * 2, i * 41 + 41, 41 * 3))

for l in range(0, 17):
    coords_w2.append((i * 41, 41 * 3, i * 41 + 41, 41 * 4))

for m in range(0, 13):
    coords_i1.append((i * 41, 41 * 4, i * 41 + 41, 41 * 5))

for n in range(0, 17):
    coords_w1.append((i * 41, 41 * 5, i * 41 + 41, 41 * 6))

for o in range(0, 13):
    coords_i0.append((i * 41, 41 * 6, i * 41 + 41, 41 * 7))

for p in range(0, 17):
    coords_w0.append((i * 41, 41 * 7, i * 41 + 41, 41 * 8))