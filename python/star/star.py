import math

width = 120
height = 40
x_scale = 2.2

outer_radius = 0.95
inner_radius = outer_radius * math.sin(math.radians(18)) / math.sin(math.radians(54))
points = []
for k in range(10):
    angle = math.radians(90 - k * 36)
    radius = outer_radius if k % 2 == 0 else inner_radius
    points.append((radius * math.cos(angle), radius * math.sin(angle)))


def point_in_polygon(x, y, polygon):
    inside = False
    for i in range(len(polygon)):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i + 1) % len(polygon)]
        if ((y0 > y) != (y1 > y)) and (x < (x1 - x0) * (y - y0) / (y1 - y0) + x0):
            inside = not inside
    return inside


for i in range(height):
    y = 1.0 - 2.0 * i / (height - 1)
    line = ""
    for j in range(width + 1):
        x = (2.0 * j / width - 1.0) * x_scale
        if point_in_polygon(x, y, points):
            line += "*"
        else:
            line += " "
    print(line.rstrip())
