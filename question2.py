frist_set={23,42,65,57,78,83,29}
second_set={57,83,29,67,73,43,48}
common_set=frist_set.intersection(second_set)
print(f"Common set:{common_set}")
difference_update=frist_set.difference(second_set)
print(f"Frist set after removing common set:{difference_update}")