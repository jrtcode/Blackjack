import random
from textwrap import dedent

suits = ('Diamond', 'Club', 'Heart', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
cards = []
p1 = []
dh = []
table = [p1, dh]
facedown = []

'''''''''''
''Classes''
'''''''''''


class Deck:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits

    def build(self):
        for suit in suits:
            for rank in ranks:
                phrase = rank + ' of ' + suit
                cards.append(phrase)


class Dealer:
    def __init__(self, p1, dh):
        self.p1 = p1
        self.dh = dh

    # Give it a good shuffle

    def shuffle(self):
        random.shuffle(cards)
        random.shuffle(cards)
        random.shuffle(cards)
        random.shuffle(cards)

    # Deal out first cards to player and dealer

    def deal_hands(self):
        p1.append(cards[0])
        cards.pop(0)
        dh.append(cards[0])
        cards.pop(0)
        p1.append(cards[0])
        cards.pop(0)
        facedown.append(cards[0])
        dh.append('FACEDOWN CARD')
        cards.pop(0)
        print(table)

    # We have a facedown, reveal it once player is done hitting

    def reveal(self):
        dh.pop(-1)
        dh.append(facedown[0])
        facedown.pop()
        print(table)

    # Define hand value for dealer    

    def value(self):
        return sum([values.get(card.split()[0]) for card in dh])

    # Dealer hits to hard 17

    def hard17(self):
        while (self.value() < 17):
            dh.append(cards[0])
            cards.pop(0)

    # Adjust for Ace in hand

    def adjust_for_ace(self):
        count = 0
        adjusted = 0
        for card in dh:
            if 'Ace' in card:
                count = count + 1
        if count >= 3 and dlr.value() > 21:
            adjusted = dlr.value() - 10 * (count - 1)
            if adjusted > 21:
                adjusted = adjusted - 10
            return adjusted
        elif count == 2 and dlr.value() > 21:
            adjusted = dlr.value() - 10
            if adjusted > 21:
                adjusted = adjusted - 10
            return adjusted
        elif count == 1 and dlr.value() > 21:
            adjusted = dlr.value() - 10
            return adjusted
        else:
            pass

    # Check for winner

    def winner_is(self):
        if plyr.value() > 21 and dlr.value() > 21:
            if plyr.value() < dlr.value():
                print("Player Push")
                b.money_return()
            else:
                print("Player Bust")
                print("You Lose")
        elif plyr.value() > 21:
            print("Player Bust ")
        elif dlr.value() > 21:
            print("Dealer Bust")
            b.win_money()
        elif plyr.value() > dlr.value() and plyr.value() < 22:
            print("Player Wins!")
            b.win_money()
            print(f"Player's {plyr.value()} to Dealer's {dlr.value()}")
        elif plyr.value() < dlr.value() and dlr.value() < 22:
            print("Dealer Wins!")
            print(f"Dealer's {dlr.value()} to Player's {plyr.value()}")
        else:
            print("Push")
            b.money_return()
            print(f"Player's {plyr.value()} to Dealer's {dlr.value()}")


class Player:
    def __init__(self, p1):
        self.p1 = p1

    # Define hand value for player

    def value(self):
        return sum([values.get(card.split()[0]) for card in p1])

    # Adjust for Ace

    def adjust_for_ace(self):
        count = 0
        for card in p1:
            if 'Ace' in card:
                count += 1
        if count and plyr.value() > 21:
            adjusted = plyr.value() - (10 * (count - 1))
            return adjusted
        else:
            pass

    # Ask for player hit or stay

    def hit_stay(self):
        hitting = True
        while hitting:
            answer = str(input("Hit or Stay? "))
            if answer.upper() == "HIT":
                print("Hitting")
                p1.append(cards[0])
                self.adjust_for_ace()
                print(table)
                if self.value() > 21:
                    print("Player Bust")
                    hitting = False
                    print(table)
            elif answer.upper() == "STAY":
                print("Player Stays")
                hitting = False
                print(table)
            else:
                print('Try Again')


class Banker:
    def __init__(self, bank, pot):
        self.bank = bank  # Integer value only
        self.pot = pot  # Integer value only

    def __str__(self):
        return dedent(f"""
        Player Bank: $ {self.bank}
        Pot: $ {self.pot}""")

    def add_money(self, deposit):
        self.bank = self.bank + deposit
        print("Money Added")

    def bet_money(self, withdraw):
        self.last_withdraw = 0
        if withdraw > self.bank:
            print("SORRY AMOUNT EXCEEDS BANK FUNDS")
            print(self.bank)
        else:
            self.bank = self.bank - withdraw
            self.pot = self.pot + withdraw
            self.last_withdraw = withdraw
            print("Bet Placed")
            print(b)

    def get_bet(self):
        answer = int(input("Please place your bets "))
        self.bet_money(answer)
        print(b)

    def win_money(self):
        winnings = self.last_withdraw * 2
        self.pot = self.pot - winnings
        self.add_money(winnings)

    def money_return(self):
        money_return = self.last_withdraw
        self.pot = self.pot - money_return
        self.add_money(money_return)


# Assign Classes


b = Banker(1000, 10000)
d = Deck(ranks, suits)
dlr = Dealer(p1, dh)
plyr = Player(p1)

# MAIN LOOP

live_game = True

while live_game:
    # welcome to the game
    print("Welcome to BlackJack")
    print("Let's Play")
    d.build()
    dlr.shuffle()
    betting = True
    while betting:
        try:
            answer = int(input("Please place your bets "))
        except:
            print("Please give a number")
        else:
            betting = False
    b.bet_money(answer)
    dlr.deal_hands()
    plyr.hit_stay()
    dlr.reveal()
    dlr.hard17()
    print(table)
    dlr.winner_is()
    print(b)
    replay = True
    while replay:
        play_again = str(input("Would you like to play again? "))
        if play_again.upper() == "YES":
            cards = []
            p1 = []
            dh = []
            table = [p1, dh]
            facedown = []
            break
        elif play_again.upper() == "NO":
            replay = False
        else:
            print("Yes or No ")
    if replay == False:
        live_game = False
