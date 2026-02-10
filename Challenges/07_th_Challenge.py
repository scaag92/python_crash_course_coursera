
resources = [
    {"name": "vm-1", "region": "us-central1"},
    {"name": "db-1", "region": "us-east1"},
    {"name": "vm-2", "region": "us-central1"},
    {"name": "vm-3", "region": "europe-west1"},
    {"name": "lb-1", "region": "us-east1"}
]

def counter(resources):
    result = {}
    us_central1_counter = 0
    us_east1_counter = 0
    europe_west1_counter = 0
    for resource in resources:
        print(resource["region"])
        if resource["region"] == "us-central1":
            us_central1_counter += 1
        if resource["region"] == "us-east1":
            us_east1_counter += 1
        if resource["region"] == "europe-west1":
            europe_west1_counter += 1
        
    result["us-central1"] = us_central1_counter
    result["us-east1"] = us_east1_counter
    result["europe-west1"] = europe_west1_counter
    
    return result 
        
print(counter(resources))

#--------------------------------------------------



def counter2(resources):
    result = {}
    for resource in resources:
        reg = resource["region"]
        if reg not in result:
            result[reg] = 1
        else:
            result[reg] += 1
            
    return result
    
print(counter2(resources))

def counter3(resources):
    result = {}
    for resource in resources:
        reg = resource["region"]
        # .get busca 'reg'. Si no existe, devuelve 0. Luego sumamos 1.
        result[reg] = result.get(reg, 0) + 1
    return result

print(counter2(resources))

