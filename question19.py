group1 = {"Ram", "Sita", "Hari"}
group2 = {"Geeta", "Hari", "Ravi"}
common_students = group1.intersection(group2)
if len(common_students) == 0:
    print("Groups are OK-no overlap.")
else:
    print("Warning: Groups share at least one student!")
