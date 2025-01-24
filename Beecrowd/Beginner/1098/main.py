from decimal import Decimal

i = Decimal('0.0')
j = Decimal('1.0')
while i != Decimal('2.2'):
    if i % 1 == 0:
        print(f"I={i:.0f} J={j:.0f}")
        print(f"I={i:.0f} J={j + 1:.0f}")
        print(f"I={i:.0f} J={j + 2:.0f}")
    else:

        print(f"I={i} J={j}")
        print(f"I={i} J={j + 1}")
        print(f"I={i} J={j + 2}")
    i += Decimal('0.2')
    j += Decimal('0.2')