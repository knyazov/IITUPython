def centuryFromYear(year):
    century = year // 100 + 1
    print(f"centuryFromYear(year) = {century}")

year = int(input())
centuryFromYear(year)