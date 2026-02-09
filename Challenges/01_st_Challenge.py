#instances = [
#    {"name": "vm1", "status": "RUNNING"},
#    {"name": "vm2", "status": "TERMINATED"},
#    {"name": "vm3", "status": "RUNNING"}
#]
#
#running_instantes = []
#
#for i in instances:
#    for l in name:
#        

instances = [
    {"name": "vm1", "status": "RUNNING"},
    {"name": "vm2", "status": "TERMINATED"},
    {"name": "vm3", "status": "RUNNING"}
]

def get_running_vms(instances_list):
    running_instances = []
    
    # 'vm' represents the dictionary: {"name": "vm1", "status": "RUNNING"}
    for vm in instances_list:
        # Access the dictionary value by its key
        if vm["status"] == "RUNNING":
            running_instances.append(vm["name"]) # We want the NAME, not the status
            
    return running_instances # Always RETURN in a function, don't just print

# Usage
print(get_running_vms(instances))


