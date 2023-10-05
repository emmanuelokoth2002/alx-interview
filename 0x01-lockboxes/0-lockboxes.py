#!/usr/bin/python3


def canUnlockAll(boxes):
    if not boxes:
        return False

    # Initialize a set to keep track of the boxes we can visit
    unlocked_boxes = set()
    unlocked_boxes.add(0)  # Start with the first box

    # Initialize a stack for DFS (Depth-First Search)
    stack = [0]

    # Perform DFS to unlock boxes
    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        for key in keys:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                stack.append(key)

    # Check if all boxes have been visited
    return len(unlocked_boxes) == len(boxes)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))
