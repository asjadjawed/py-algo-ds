def recursive_max(list):
    if list is None or list == []:
        return None
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    submax = recursive_max(list[1:])
    return list[0] if list[0] > submax else submax
