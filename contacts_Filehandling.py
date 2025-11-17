#Real-world file handling + CSV, basics of CRUD.
import csv,os

F="contacts.csv"
HEADERS=["name","phone","email"]

def ensure():
    if not os.path.exists(F):
        with open(F,"w",newline="") as fh:
            writer=csv.DictWriter(fh,fieldnames=HEADERS)
            writer.writeheader()

def read_all():
    with open(F,newline="") as fh:
        return list(csv.DictReader(fh))
def write_all(rows):
    with open(F,"w",newline="") as fh:
        writer=csv.DictWriter(fh,fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)

def list_contacts():
    rows=read_all()
    for i,r in enumerate(rows,1):
        print(i,r["name"],r["phone"],r["email"])
    
def add_contact():
    name=input("Name: ")
    phone=int(input("Phone: "))
    email=input("Email: ")
    rows=read_all()
    rows.append({"name":name,"phone":phone,"email":email})
    write_all(rows)
    print("Added.")

def delete_contact():
    list_contacts()
    n=int(input("Delete "))-1
    rows=read_all()
    rows.pop(n)
    write_all(rows)
    print("Deleted.")

def main():
    ensure()
    while True:
        print("Commands: list,add,del,q")
        cmd=input("> ").strip()
        if cmd=='q':
            break
        if cmd=="list":
            list_contacts()
        elif cmd=="add":
            add_contact()
        elif cmd=='del':
            delete_contact()
        else:
            print("Unkown")
if __name__=="__main__":
    main()