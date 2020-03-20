def year_day():
    d1, m1, y1 = [int(x) for x in input('plz enter the first date like this: \n1 6 1398 \n').split()]
    d2, m2, y2 = [int(x) for x in input('plz enter the second date like this: \n1 6 1398 \n').split()]
    if m1 == 12:
        totald1 = d1 + (m1 * 29) + (y1 * 365) + int(m1 / 4)
        totald2 = d2 + (m2 * 29) + (y2 * 365) + int(m2 / 4)
    elif m1 <= 6:
        totald1 = d1 + (m1 * 31) + (y1 * 365)
        totald2 = d2 + (m2 * 31) + (y2 * 365)
    elif m2 >= 6:
        totald1 = d1 + (m1 * 30) + (y1 * 365)
        totald2 = d2 + (m2 * 30) + (y2 * 365)

    diff = totald1 - totald2  # total days
    if diff < 0:
        diff = diff * -1

    ydiff = diff // 365
    x1 = diff - (ydiff * 356)  # total months full years excluded
    mdiff = (x1 // 29)
    ddiff = x1 - (mdiff * 29)  # total days full years and months excluded

    print(ydiff, ' years and ', mdiff, ' months and ', ddiff, 'days')
    print('with total ', diff, ' days!')


year_day()
