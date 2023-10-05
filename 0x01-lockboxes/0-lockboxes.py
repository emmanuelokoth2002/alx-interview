#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    """Initialize a set to keep track of the boxes we can visit"""
    unlocked_boxes = set()
    unlocked_boxes.add(0)  # Start with the first box

    """Initialize a stack for DFS (Depth-First Search)"""
    stack = [0]

    """Perform DFS to unlock boxes"""
    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        for key in keys:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                stack.append(key)

    return len(unlocked_boxes) == len(boxes)
