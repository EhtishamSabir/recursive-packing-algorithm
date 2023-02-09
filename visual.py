import matplotlib.pyplot as plt
import matplotlib.patches as patches
from random import random


def visualize(width, height, rectangles):
    fig = plt.figure()
    axises = fig.add_subplot(1, 1, 1)
    axises.add_patch(
        patches.Rectangle(
            (0, 0),
            width,
            height,
            hatch='x',
            fill=False,
        )
    )
    for idx, rect in enumerate(rectangles):
        axises.add_patch(
            patches.Rectangle(
                (rect.x, rect.y),  # (x,y)
                rect.w,  # width
                rect.h,  # height
                color=(random(), random(), random()),
            )
        )
        axises.text(rect.x + 0.5 * rect.w, rect.y + 0.5 * rect.h, str(idx))
    axises.set_xlim(0, width)
    axises.set_ylim(0, height)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
