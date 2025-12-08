required_tasks={"Email","Report","Meeting"}
completed_tasks={"Email","Report"}
if required_tasks.issubset(completed_tasks):
    print("All taks done!")
else:
    print("Some tasks pending.")
    