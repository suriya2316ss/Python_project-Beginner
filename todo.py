import json, os
FNAME = "todo.json"

def load():
    if os.path.exists(FNAME):
        try:
            return json.load(open(FNAME))
        except:
            print("Corrupted todo.json — resetting file.")
            return []
    return []

def save(items):
    json.dump(items, open(FNAME,"w"), indent=2)

def show(items):
    if not items:
        print("No tasks.")
    for i, t in enumerate(items,1):
        status = "✓" if t.get("done") else " "
        print(f"{i}. [{status}] {t['task']}")

def main():
    items = load()
    while True:
        print("\nCommands: add, done <n>, del <n>, list, q")
        cmd = input("> ").strip()
        if cmd == 'q': 
            break
        if cmd == 'list': 
            show(items)
            continue
        if cmd.startswith("add"):
            task = cmd[3:].strip() or input("Task: ")
            items.append({"task":task, "done":False})
            save(items)
            print("Added.")
            continue
        parts = cmd.split()
        if len(parts)>=2 and parts[0] in ("done","del"):
            try:
                n = int(parts[1])-1
                if parts[0]=="done": items[n]["done"]=True; print("Marked done.")
                else: items.pop(n); print("Deleted.")
                save(items)
            except Exception as e:
                print("Invalid index.", e)
            continue
        print("Unknown command.")
if __name__=="__main__":
    main()
