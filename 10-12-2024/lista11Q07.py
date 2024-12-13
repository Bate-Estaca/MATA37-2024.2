DataBase = {}
DB_backup = {}

def addToDB(key, value):
   DB_backup[key] = DataBase[key] = value
   if len(DataBase) > 4:
       print("\n",DataBase,"\n")
       DataBase.clear()

for n in range(50):
    addToDB("key"+str(n),n)

