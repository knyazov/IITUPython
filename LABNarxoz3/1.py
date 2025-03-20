import json

with open("cities.json", "r") as file:
    output = json.load(file)
    print(output["data"])
    for i in range(len(output["data"])):
        print(output["data"][i])
        if output["data"][i]["departments"] != None:
            for j in range(len(output["data"][i]["departments"])):
                print(output["data"][i]["departments"][j])