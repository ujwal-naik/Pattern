import math

width = 120
height = 40
x_scale = 2.2

outer_radius = 0.95
outer_points = []
for k in range(5):
    angle = math.radians(90 - k * 72)
    outer_points.append((outer_radius * math.cos(angle), outer_radius * math.sin(angle)))

# Connect every second outer vertex to form the classic 5-point star shape.
star_indices = [0, 2, 4, 1, 3, 0]
star_points = [outer_points[i] for i in star_indices]


def to_grid(point):
    x, y = point
    gx = int(round((x / x_scale + 1.0) * 0.5 * (width - 1)))
    gy = int(round((1.0 - y) * 0.5 * (height - 1)))
    return gx, gy


grid = [[" " for _ in range(width)] for _ in range(height)]


def draw_line(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if 0 <= x0 < width and 0 <= y0 < height:
            grid[y0][x0] = "*"
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy


for i in range(len(star_points) - 1):
    draw_line(to_grid(star_points[i]), to_grid(star_points[i + 1]))

for row in grid:
    print("".join(row).rstrip())
