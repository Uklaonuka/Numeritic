a = int(input())
ozenki = input()
ozenki = ozenki.split()
if len(ozenki) < 8:
    print(ozenki.count('5'))
else:
    results = []
    i = 0
    while i <= a - 7:
        week = ozenki[i:i+7]
        if week.count('2') == 0 and week.count('3') == 0:
            results.append(week.count('5'))
        i += 1
    if len(results) == 0:
        print(-1)
    else: print(max(results))

