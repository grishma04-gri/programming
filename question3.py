frist_set={27,43,34}
second_set={34,93,22,27,43,53,48}
if frist_set.issubset(second_set):
    frist_set.clear()
elif frist_set.issuperset(second_set):
    frist_set.clear()
print(f"Frist set after checking:{frist_set}")
