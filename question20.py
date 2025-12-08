sample_dict={
    "emp1":{"name":"Jhon","salary":7500},
    "emp2":{"name":"Emma","salary":8000},
    "emp3":{"name":"Shyam","salary":500}
}
for emp, info in sample_dict.items():
    if info["name"]=="Shyam":
        info["salary"]=8500
print(sample_dict)