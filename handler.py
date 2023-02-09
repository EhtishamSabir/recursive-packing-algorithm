from rec_packing import phspprg, visualize

if __name__ == '__main__':

    # boxes to packing in region
    boxes = [[5, 15], [25, 33], [23, 44], [10, 5], [10, 20], [20, 10], [5, 6], [6, 5], [10, 10], [10, 6], [6, 4],
             [1, 10],[8, 4], [6, 6], [20, 17]]

    # room...
    width = 100
    # program for recursive packing called
    height, rectangles = phspprg(width, boxes)

    # display packing
    visualize(width, height, rectangles)
