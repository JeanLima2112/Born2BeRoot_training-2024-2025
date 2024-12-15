try:
    
    while True:
        d = int(input())
        m = int(input())

        if not d:
            break

        if d in (98, 99) or m in (98, 99):
            x = max(d, m)
            if x == 98:
                print('IAN BIRTHDAY, GO OUT FOR DINNER')
            else:
                print('HELEN BIRTHDAY, GO OUT FOR DANCING')
        else:
            print('WATCH ' + ('MOVIE' if (d + m + 99) % 2 == 1 else 'SERIES'))

except:
    pass
