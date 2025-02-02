def add(param1, param2):
    print(f"add(param1, param2) = {param1 + param2}")


param1, param2 = map(int, input().split())
add(param1, param2)