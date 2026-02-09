file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}

disks = [
    {"id": "d-1", "size_gb": 100, "attached_to": "vm-1"},
    {"id": "d-2", "size_gb": 50,  "attached_to": None},  # Unattached
    {"id": "d-3", "size_gb": 200, "attached_to": None},  # Unattached
    {"id": "d-4", "size_gb": 500, "attached_to": "vm-2"}
]


for i in disks:
    for d in i.values():
        if i["attached_to"] == "None":
            print (i.values())