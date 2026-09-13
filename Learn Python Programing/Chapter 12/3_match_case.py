def http_status(status):
    match status:
        case 200:
            return"ok"
        case 404:
            return"not found"
        case 500:
            return"Internal server error"
        case _:
            "Unknown status" 
                 # Usage print(http_status(200))
                 #Output :ok print (http_status(404))
                 #Output :Not found print(http_Status(500))
                 #Output :Internal server