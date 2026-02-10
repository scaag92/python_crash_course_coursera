api_response = {
    "kind": "compute#instanceList",
    "items": [
        {
            "name": "web-server-1",
            "config": {
                "metadata": {"env": "prod", "role": "frontend"},
                "status": "RUNNING"
            }
        },
        {
            "name": "db-server-1",
            "config": {
                "metadata": {"env": "dev", "role": "database"},
                "status": "STOPPED"
            }
        },
        {
            "name": "web-server-2",
            "config": {
                "metadata": {"env": "prod", "role": "frontend"},
                "status": "TERMINATED"
            }
        }
    ]
}

def get_prod_instances(api_response):
    result = []
    for i in api_response["items"]:
        if i["config"]["metadata"]["env"] == "prod":
            result.append(i["name"])
    return result

print(get_prod_instances(api_response))   

            