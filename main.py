from copy import deepcopy
from collections import namedtuple
import sys

Rectangle = namedtuple('Rectangle', ['x', 'y', 'w', 'h'])


def recursive_packing(x, y, w, h, D, remaining, indices, result):
    """Helper function to recursively fit a certain area."""
    priority = 6
    for idx in indices:
        for j in range(0, D + 1):
            if priority > 1 and remaining[idx][(0 + j) % 2] == w and remaining[idx][(1 + j) % 2] == h:
                priority, orientation, best = 1, j, idx
                break
            elif priority > 2 and remaining[idx][(0 + j) % 2] == w and remaining[idx][(1 + j) % 2] < h:
                priority, orientation, best = 2, j, idx
            elif priority > 3 and remaining[idx][(0 + j) % 2] < w and remaining[idx][(1 + j) % 2] == h:
                priority, orientation, best = 3, j, idx
            elif priority > 4 and remaining[idx][(0 + j) % 2] < w and remaining[idx][(1 + j) % 2] < h:
                priority, orientation, best = 4, j, idx
            elif priority > 5:
                priority, orientation, best = 5, j, idx
    if priority < 5:
        if orientation == 0:
            omega, d = remaining[best][0], remaining[best][1]
        else:
            omega, d = remaining[best][1], remaining[best][0]
        result[best] = Rectangle(x, y, omega, d)
        indices.remove(best)
        if priority == 2:
            recursive_packing(x, y + d, w, h - d, D, remaining, indices, result)
        elif priority == 3:
            recursive_packing(x + omega, y, w - omega, h, D, remaining, indices, result)
        elif priority == 4:
            min_w = sys.maxsize
            min_h = sys.maxsize
            for idx in indices:
                min_w = min(min_w, remaining[idx][0])
                min_h = min(min_h, remaining[idx][1])
            # Because we can rotate:
            min_w = min(min_h, min_w)
            min_h = min_w
            if w - omega < min_w:
                recursive_packing(x, y + d, w, h - d, D, remaining, indices, result)
            elif h - d < min_h:
                recursive_packing(x + omega, y, w - omega, h, D, remaining, indices, result)
            elif omega < min_w:
                recursive_packing(x + omega, y, w - omega, d, D, remaining, indices, result)
                recursive_packing(x, y + d, w, h - d, D, remaining, indices, result)
            else:
                recursive_packing(x, y + d, omega, h - d, D, remaining, indices, result)
                recursive_packing(x + omega, y, w - omega, h, D, remaining, indices, result)
