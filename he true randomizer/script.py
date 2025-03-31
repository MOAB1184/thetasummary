import random
def random_line(lockout):
    with open(lockout, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        return random.choice(lines)
while True:
    test = input('Placeholder: send "run":').lower()
    if test == "run":
        print(random_line('D:/dadas/he true randomizer/lockout.txt'))
    elif test == "q":
        break
