"""
A BFS Example
"""

from collections import deque


def person_is_seller(name: str):
    """
    Check if the person is a mango seller.

    Parameters:
    name (str): The name of the person to check.

    Returns:
    bool: True if the person is a mango seller, False otherwise.
    """
    return name[-1] == "m"  # Just a silly example, modify as needed


def search(name: str):
    """
    Search for a mango seller in the social network graph using BFS.

    Parameters:
    name (str): The starting person's name to search from.

    Returns:
    bool: True if a mango seller is found, False otherwise.
    """
    search_queue: deque[str] = deque()
    search_queue += my_mango_network[name]
    searched: set[str] = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += my_mango_network[person]
                searched.add(person)
    return False


# Example graph data
my_mango_network: dict[str, list[str]] = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}
