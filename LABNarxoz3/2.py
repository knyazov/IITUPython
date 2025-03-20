import json
a = {
    "cities" : {
        "Roma": 0,
        "Venice": 0,
        "Tokyo": 0,
        "Hiroshima": 0,
        "Southlake": 5,
        "South San Francisco": 45,
        "South Brunswick": 0,
        "Seattle": 2,
        "Toronto": 2,
        "Whitehorse": 0,
        "Beijing": 0,
        "Bombay": 0,
        "Sydney": 0,
        "Singapore": 0,
        "London": 1,
        "Oxford": 34,
        "Stretford": 0,
        "Munich": 1,
        "Sao Paulo": 0,
        "Geneva": 0,
        "Bern": 0,
        "Utrecht": 0,
        "Mexico City": 0
    }
}
sum = 0
for key in a["cities"]:
    sum += a["cities"][key]
print(sum)
# with open("dictionary_output.json", "r") as file:
#     out = json.load(file)
#     print(out)
#     print(out["cities"])
#     sum = 0
#     for key in out["cities"]:
#         sum += out["cities"][key]
#     print(sum)