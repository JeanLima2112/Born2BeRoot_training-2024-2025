import datetime

try:
    while True:
        day, month, year = map(int, input().split('/'))

        if year < 0:
            year = year + 3114
            today = datetime.datetime(year, month, day)
            bc_days = (today - datetime.datetime(1, 8, 11)).days
            ac_days = 0

        else:
            today = datetime.datetime(year, month, day)
            ac_days = (today - datetime.datetime(1, 1, 1)).days
            bc_days = 1137143

        days = ac_days + bc_days
        mayan_cicles = [144000, 7200, 360, 20, 1]
        mayan_date = []

        for cicle in mayan_cicles:
            mayan_date.append(days // cicle)
            days -= cicle * mayan_date[-1]

        print(".".join(map(str, mayan_date)))

except EOFError:
    pass
