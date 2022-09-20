"""
Test for 2 Crystal Balls
"""

from random import randint

from py_algo_ds.problems.crystal_balls import crystal_balls


class TestCrystalBalls():
    "Test 2 Crystal Balls Problem"
    total_floors = 10  # has to be at least 1
    # the end is inclusive so can result in fully false data
    idx = randint(0, total_floors)

    floor_data = [False] * total_floors

    for i in range(idx, total_floors):
        floor_data[i] = True

    def test_crystal_ball_breaks_at_first_floor_one_floor(self):
        "crystal ball breaks at 1st floor in one floor building"
        assert crystal_balls([True]) == 0

    def test_crystal_ball_does_not_breaks_at_first_floor_one_floor(self):
        "crystal ball does not break at 1st floor in one floor building"
        assert crystal_balls([False]) == -1

    def test_crystal_ball_random_floors(self):
        "testing crystal ball with random floors"
        if self.idx >= len(self.floor_data):
            # there is no floor at which crystals break
            assert crystal_balls(self.floor_data) == -1
        else:
            # there is a floor at which crystal break
            assert crystal_balls(self.floor_data) == self.idx

    def test_crystal_ball_with_all_false(self):
        "testing crystal balls for a tall building where the don't break"
        assert crystal_balls([False] * 10) == -1
