log_entry = "2024-02-08 14:00:00 [ERROR] Connection failed at ip=10.0.0.5"
clean_logentry = log_entry.replace("[", "").replace("]", "").replace("ip=", "")
print(clean_logentry)
dictonary = {}
clean_logentry = clean_logentry.split()
print (clean_logentry[2])
print (clean_logentry[-1])
dictonary ["level"] = clean_logentry[2]
dictonary ["ip"] = clean_logentry[-1]
print (dictonary)
