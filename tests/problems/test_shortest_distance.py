"""
Test distance between two words
"""

from py_algo_ds.problems.shortest_distance import shortest_distance


def test_shortest_distance():
    words1 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    word11 = "fox"
    word21 = "dog"
    expected_output1 = 5
    assert shortest_distance(words1, word11, word21) == expected_output1

    words2 = ["a", "b", "c", "d", "a", "b"]
    word12 = "a"
    word22 = "b"
    expected_output2 = 1
    assert shortest_distance(words2, word12, word22) == expected_output2

    words3 = ["a", "c", "d", "b", "a"]
    word13 = "a"
    word23 = "b"
    expected_output3 = 1
    assert shortest_distance(words3, word13, word23) == expected_output3

    words4 = ["a", "b", "c", "d", "e"]
    word14 = "a"
    word24 = "e"
    expected_output4 = 4
    assert shortest_distance(words4, word14, word24) == expected_output4

    words5 = ["a", "b", "c", "f", "d", "e"]
    word15 = "a"
    word25 = "f"
    expected_output5 = 3
    assert shortest_distance(words5, word15, word25) == expected_output5
