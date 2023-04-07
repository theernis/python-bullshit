import random
import math

state = random.getstate()

#how detailed noise will be
#if set to 0 or negative number it will crash the program because of not stopping while loop
detail = .25

#how strong overlay be compared to previous layer overlay strength
#if set to 1 it will crash the program because of not stopping while loop
overlay_strength = .75

#how many times bigger scale will be compared to previous layer size
#recommended to keep it >1 to make each layer smaller, but it doesnt crash if its =<1
overlay_size = 2

def getGrayscale(x, y, z):
    final_n = 0

    strength = 1
    i = 0
    while True:
        n = []
        for x1 in range(2):
            for y1 in range(2):
                for z1 in range(2):
                    x2 = math.floor(x + x1)
                    y2 = math.floor(y + y1)
                    z2 = math.floor(z + z1)
                    random.setstate(state)
                    random.seed(f"{x2}{y2}{z2}")
                    n.append(random.random())

        n1 = []
        for x3 in range(4):
            n1.append((1-x%1) * n[x3] + (x%1) * n[x3 + 4])

        n2 = []
        for y3 in range(2):
            n2.append((1-y%1) * n1[y3] + (y%1) * n1[y3 + 2])

        n3 = (1-z%1) * n2[0] + (z%1) * n2[1]

        final_n += n3 * strength

        i += strength
        strength *= overlay_strength
        x *= overlay_size
        y *= overlay_size
        z *= overlay_size

        if (min(detail, 1/detail) > strength):
            break

    final_n /= i

    return (final_n*255, final_n*255, final_n*255)

def getColor(x, y, z):
    final_r = 0
    final_g = 0
    final_b = 0

    strength = 1
    i = 0
    while True:
        r = []
        g = []
        b = []
        for x1 in range(2):
            for y1 in range(2):
                for z1 in range(2):
                    x2 = math.floor(x + x1)
                    y2 = math.floor(y + y1)
                    z2 = math.floor(z + z1)
                    random.setstate(state)
                    random.seed(f"{x2}{y2}{z2}")
                    r.append(random.random())
                    g.append(random.random())
                    b.append(random.random())

        r1 = []
        g1 = []
        b1 = []
        for x3 in range(4):
            r1.append((1-x%1) * r[x3] + (x%1) * r[x3 + 4])
            b1.append((1-x%1) * g[x3] + (x%1) * g[x3 + 4])
            g1.append((1-x%1) * b[x3] + (x%1) * b[x3 + 4])
        
        r2 = []
        g2 = []
        b2 = []
        for y3 in range(2):
            r2.append((1-y%1) * r1[y3] + (y%1) * r1[y3 + 2])
            g2.append((1-y%1) * g1[y3] + (y%1) * g1[y3 + 2])
            b2.append((1-y%1) * b1[y3] + (y%1) * b1[y3 + 2])
        
        r3 = (1-z%1) * r2[0] + (z%1) * r2[1]
        g3 = (1-z%1) * g2[0] + (z%1) * g2[1]
        b3 = (1-z%1) * b2[0] + (z%1) * b2[1]
    
        final_r += r3 * strength
        final_g += g3 * strength
        final_b += b3 * strength

        i += strength
        strength *= overlay_strength
        x *= overlay_size
        y *= overlay_size
        z *= overlay_size

        if (min(detail, 1/detail) > strength):
            break
        
    final_r /= i
    final_g /= i
    final_b /= i

    return (final_r*255, final_g*255, final_b*255)