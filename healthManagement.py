# Health management system
def getdate():
    """this function returns the current time."""
    import datetime
    cdate = datetime.datetime.now()
    return cdate
 
def food():
    fname = n+ef+".txt"
    if rw=="Write":
        f1 = input("what do you eat : ")
        print(getdate()," - ",f1)
        global date
        date = getdate()
        with open(fname, "a") as f:
            f.write(f"{date} - {f1}\n")
    else:        
        with open(fname, "r") as f:
            print(f.read())        
    
def exercise():
    fname = n+ef+".txt"
    if(rw=="Write"):
        e1 = input("what exercise you have done : ")
        print(getdate()," - ",e1)
        global date
        date = getdate()        
        with open(fname, "a") as f:
            f.write(f"{date} - {e1}\n")
    else:
        with open(fname, "r") as f:
            print(f.read())
            
print(getdate())                 
rw=(input("enter your option read/write : ")).capitalize()

print(f"which file you want to {rw}.\nRam\nShyam\nAdnam\nenter your choice")
n = (input()).capitalize()
if(n=="Ram"):
    print(f"what do you want to {rw}, enter",
    "\nfood or exercise")
    ef=(input()).capitalize()
    if(ef=="Food"):
        food()
    else:
        exercise() 

elif(n=="Shyam"):
    print(f"what do you want to {rw}.\nfood or exercise\nenter your choice")
    ef=(input()).capitalize()
    if(ef=="Food"):
        food()
    else:
        exercise()
    
else:
    print(f"what do you want to {rw}.\nfood or exercise\nenter your choice")
    ef=(input()).capitalize()
    if(ef=="Food"):
        food()
    else:
        exercise()  