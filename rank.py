import pandas as pd
dataread = input("whats the name of your file ")
data = pd.read_csv(dataread)
colname = input("whats the column name of the things you want to rank? ")
ogitems = data[colname].tolist()
items =  []
items.append(ogitems[0])
del ogitems[0]
for person in ogitems:
    changeableitems = items.copy()
    while True:
        print()
        zone = len(changeableitems)
        against = changeableitems[(zone)//2]
        usri = input(f"Does {person} mog {against} y/n:")
        if usri.lower() == "y":
            if zone == 1 or zone == 2:
               items.insert(items.index(against)+1, person)
               break
            else:
                del changeableitems[0:(zone//2)+1]
                
        elif usri.lower() == "n":
            if zone ==1:
                items.insert(items.index(against), person)
                break
            else:
                del changeableitems[zone//2:]
print(items)
items.reverse()
for i in range(len(items)-1):
    print(f"{i}. {items[i]}")


       


