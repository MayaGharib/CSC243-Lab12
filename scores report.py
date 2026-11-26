
records=[]
try:
    with open("scores.txt","r") as file:
        for line in file:
            data=line.strip().split(",")
            name=data[0]
            try:
                score=int(data[1])
                records.append([name,score])
            except ValueError:
                continue
    for record in records:
        if record[0]=="Karim":
            print(record[1])
    print(len(records))
    updated=[]
    for record in records:
        name=record[0]
        score=record[1]
        if name=="Maya":
            score=88
        if name!="Nour":
            updated.append([name,score])
    with open("scores.txt","w") as file:
        for record in updated:
            file.write(record[0]+","+str(record[1])+"\n")
    with open("pass.txt","w") as file:
        for record in updated:
            if record[1]>=60:
                file.write(record[0]+"\n")
except FileNotFoundError:
    print("File not found.")
