from itertools import batched

import pyglet
from pyglet import shapes

window = pyglet.window.Window(300, 300, "Tic Tac Toe")
batch = pyglet.graphics.Batch()

# Draw grid lines
lines = [
    shapes.Line(100, 0, 100, 300, thickness=3, batch=batch),
    shapes.Line(200, 0, 200, 300, thickness=3, batch=batch),
    shapes.Line(0, 100, 300, 100, thickness=3, batch=batch),
    shapes.Line(0, 200, 300, 200, thickness=3, batch=batch),
]

marks = []  # store X/O shapes here

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):

    col = x // 100
    row = y // 100

    # figure out which cell, then draw an O (circle) or X (two lines) there
    cx, cy = col * 100 + 50, row * 100 + 50

    outer_circle = shapes.Circle(cx, cy, 30, color=(255, 0, 0), batch=batch)
    inner_circle = shapes.Circle(cx, cy, 20, color=(0, 0, 0), batch=batch)
    outer_line1 = shapes.Line(cx-30, cy-30, cx+30, cy+30, thickness=10, color=(255, 0, 0), batch=batch)
    outer_line2 = shapes.Line(cx-30, cy+30, cx+30, cy-30, thickness=10, color=(255, 0, 0), batch=batch)

    marks.append(outer_circle)
    marks.append(inner_circle)
    marks.append(outer_line1)
    marks.append(outer_line2)

if __name__ == "__main__":
    # pyglet.app.run()

    n = 0
    n ^= 1
    print(n)
