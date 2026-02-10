#--------------------------------------------------
raw_ips = ["192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.10", "10.0.0.5"]
    
def organizador(raw_ips):
    raw_ips = set(raw_ips)
    raw_ips = list(raw_ips)
    raw_ips.sort()
    return(raw_ips)

print(organizador(raw_ips))

#--------------------------------------------------
