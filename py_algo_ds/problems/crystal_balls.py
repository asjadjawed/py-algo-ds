"""
2 Crystal Balls Problem:

You are given two glass balls in a n-story building.
You have to find out in two drops which is the lowest floor at which they would break.

Must be faster than O(n). Since we only need one ball to solve it in O(n)
As we can test each floor until ball breaks

For O(n) or brute force approach only give on crystal ball

It is a possibility that the building is not tall enough to break the balls
If that happens return -1

Note: Ground Floor is 0
Hint: Problem can be solved in O(sqrt(n))
"""

import math

# Hint this is about finding the optimal jump point
# Once ball breaks we can go back the jump point difference
# And then linearly try again


def crystal_balls(building_floors: list[bool]) -> int:
    """
    Find the floor at which balls will break.
    Args:
        building_floors (list[bool]): a list of booleans with index as floor number
        and the value 'True' if ball breaks or 'False' otherwise.

    Returns:
        int: the floor at which the ball breaks else return -1
    """
    # we jump sqrt(floors)
    jump_length = math.floor(math.sqrt(len(building_floors)))

    # python for loop variables are not scoped to the loop
    for i in range(0, len(building_floors), jump_length):
        if building_floors[i]:
            break

    # if true is within the first jump we need to make sure
    # that i is at least 0 i.e. not underground when we jump back
    i = 0 if i - jump_length < 0 else i - jump_length

    # then we iterate normally after the sqrt(n) jump back
    for break_floor in range(i, len(building_floors)):
        if building_floors[break_floor]:
            return break_floor

    return -1
