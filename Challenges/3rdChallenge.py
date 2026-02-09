disks = [
    {"id": "d-1", "size_gb": 100, "attached_to": "vm-1"},
    {"id": "d-2", "size_gb": 50,  "attached_to": None},  # Unattached
    {"id": "d-3", "size_gb": 200, "attached_to": None},  # Unattached
    {"id": "d-4", "size_gb": 500, "attached_to": "vm-2"}
]


size_gb = 0

def calculate_wasted_storage (disks):
    total_size = 0
    for d in disks:
        if d["attached_to"] is None:
            total_size += d["size_gb"]
    return total_size
            

print(calculate_wasted_storage(disks))