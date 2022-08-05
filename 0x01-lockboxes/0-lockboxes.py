#!usr/bin/python3
def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened. """
    numberOfLockedBoxes = len(boxes)
    myList = [0]
    for i in myList:
        for j in boxes[i]:
            if j not in myList:
                if j < numberOfLockedBoxes:
                    myList.append(j)
    if len(myList) == numberOfLockedBoxes:
        return True
    return False
