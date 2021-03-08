import clear_terminal_screen as cls

bidder = {}


def new_bid():
    name = input('Please enter your name:>>>')
    number = False
    while not number:
        bid = input('Please enter your bid here:>>>')
        if bid.isdigit():
            number = True
        else:
            print('That wasn\'t a valid amount!')
            number = False
    return name, bid


someone_else = True
while someone_else:
    print('Please enter your name and your bid, the winner will be the highest bidder!')
    name, bid = new_bid()
    bidder[name] = bid
    next_bidder = input('Is there anyone else looking to bid? Please enter \'y\' for yes, or \'n\' for no!>>')
    while next_bidder != 'y' or next_bidder != 'n':
        if next_bidder == 'y':
            cls.cls()
            break
        elif next_bidder == 'n':
            someone_else = False
            break
        else:
            next_bidder = input('Invalid selection, please enter \'y\' for yes or \'n\' for no!>>')


print('\n\nAUCTION RESULTS\n\n')
for x, y in bidder.items():
    print(f'We have {x} with a bid of £{y}!\n')


highest_y = 0
for x, y in bidder.items():
    if int(y) >= int(highest_y):
        highest_y = int(y)

for x, y in bidder.items():
    if int(y) == int(highest_y):
        print(f'And the lucky winner is {x} with a bid of £{y}, Congratulations!!')






