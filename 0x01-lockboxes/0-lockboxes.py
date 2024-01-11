#!/usr/bin/python3
'''
this module determines if all boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    this function uses a depth-first search algorithm and their keys.
    '''
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
