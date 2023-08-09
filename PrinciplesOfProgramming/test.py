def edit_distance(s1, s2):
    if s1 == s2:
        return 0
    if len(s2) > len(s1):
        return edit_distance_helper(s1, s2)
    else:
        return edit_distance_helper(s2, s1)



def edit_distance_helper(s1, s2):
    print(f"s1: {s1}")
    print(f"s2: {s2}")
    if s1 == '':
        return len(s2)
    if s1[-1] not in s2:
        return 1 + edit_distance_helper(s1[:-1], s2)
    else:
        return edit_distance_helper(s1[:-1], s2.replace(s1[-1], ''))

print(edit_distance("sandwich", "asnthueo"))