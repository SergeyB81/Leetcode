def unique_in_order(sequence):
    if not sequence:
        return []

    result = [sequence[0]]
    for item in sequence[1:]:
        if item != result[-1]:
            result.append(item)
    return result



print(unique_in_order('AAAABBBCCDAABBB'))  # ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCCAD'))         # ['A', 'B', 'C', 'A', 'D']
print(unique_in_order([1, 2, 2, 3, 3]))   # [1, 2, 3]
print(unique_in_order([]))