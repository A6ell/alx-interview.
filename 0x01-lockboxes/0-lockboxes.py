def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists representing locked boxes.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
