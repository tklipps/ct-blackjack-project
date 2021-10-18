import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class BlackJack():
    DECK = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
    
    def __init__(self):
        random.shuffle(BlackJack.DECK)
        self.game_deck = BlackJack.DECK
        self.user_show = []
        self.user_points = []
        self.dealer_hide = []
        self.dealer_show = []
        self.dealer_points = []
        self.dealer_insta = False
        self.user_insta = False
        
        

    def deal_cards(self):
        self.dealer_hide.append(self.game_deck.pop())
        self.dealer_show.append(self.game_deck.pop())
        self.user_show.append(self.game_deck.pop())
        self.user_show.append(self.game_deck.pop())
        self.dealer_score()
        if self.dealer_total == 21:
            self.dealer_insta = True
            self.end_game()
        self.user_score()
        if self.user_total == 21:
            self.user_insta = True
            self.end_game()
        self.dealer_points.clear()
        self.user_points.clear()

            

    def user_score(self):
        for card in self.user_show:
            if card == "2":
                self.user_points.append(2)
            elif card == "3":
                self.user_points.append(3)
            elif card == "4":
                self.user_points.append(4)
            elif card == "5":
                self.user_points.append(5)
            elif card == "6":
                self.user_points.append(6)
            elif card == "7":
                self.user_points.append(7)
            elif card == "8":
                self.user_points.append(8)
            elif card == "9":
                self.user_points.append(9)
            elif card == "10":
                self.user_points.append(10)
            elif card == "J":
                self.user_points.append(10)
            elif card == "Q":
                self.user_points.append(10)
            elif card == "K":
                self.user_points.append(10)
            elif card == "A":
                self.user_points.append(11)
        self.user_total = sum(self.user_points)
            
        

    def dealer_score(self):
            for card in self.dealer_hide:
                if card == "2":
                    self.dealer_points.append(2)
                elif card == "3":
                    self.dealer_points.append(3)
                elif card == "4":
                    self.dealer_points.append(4)
                elif card == "5":
                    self.dealer_points.append(5)
                elif card == "6":
                    self.dealer_points.append(6)
                elif card == "7":
                    self.dealer_points.append(7)
                elif card == "8":
                    self.dealer_points.append(8)
                elif card == "9":
                    self.dealer_points.append(9)
                elif card == "10":
                    self.dealer_points.append(10)
                elif card == "J":
                    self.dealer_points.append(10)
                elif card == "Q":
                    self.dealer_points.append(10)
                elif card == "K":
                    self.dealer_points.append(10)
                elif card == "A":
                    self.dealer_points.append(11)
            
            for card in self.dealer_show:
                if card == "2":
                    self.dealer_points.append(2)
                elif card == "3":
                    self.dealer_points.append(3)
                elif card == "4":
                    self.dealer_points.append(4)
                elif card == "5":
                    self.dealer_points.append(5)
                elif card == "6":
                    self.dealer_points.append(6)
                elif card == "7":
                    self.dealer_points.append(7)
                elif card == "8":
                    self.dealer_points.append(8)
                elif card == "9":
                    self.dealer_points.append(9)
                elif card == "10":
                    self.dealer_points.append(10)
                elif card == "J":
                    self.dealer_points.append(10)
                elif card == "Q":
                    self.dealer_points.append(10)
                elif card == "K":
                    self.dealer_points.append(10)
                elif card == "A":
                    self.dealer_points.append(11)
            self.dealer_total = sum(self.dealer_points)
                
            


    def show_hands(self):
        print(f"Dealer hand: |?|, {self.dealer_show}")
        print(f"Your hand: {self.user_show}")
        print(self.dealer_points)
        print(self.user_points)
        print(self.dealer_total)
        print(self.user_total)
        

    def user_check(self):
        if self.user_total > 21:
            self.end_game()
        return True
                
         


    def user_hit(self):
        
        self.user_show.append(self.game_deck.pop())
        self.user_points.clear()
        self.user_score()
        clear_screen()
        self.show_hands()
        
        

            
        

    def dealer_turn(self):        
        while self.dealer_total < 17 and self.dealer_total <= self.user_total:
            self.dealer_show.append(self.game_deck.pop())
            clear_screen() 
            print(self.dealer_show)
            self.dealer_points.clear()
            self.dealer_score()
            if self.dealer_total > self.user_total and self.dealer_total <= 21:
                self.end_game()
                break
            elif  self.dealer_total > 21:
                self.end_game()
                break               
        

    def end_game(self):
        if self.dealer_insta == True:
            return 7
        elif self.dealer_insta == True:
            return 8
        elif self.user_total > 21:
            return 1
        elif self.dealer_total > 21:
            return 2
        elif self.user_total > self.dealer_total:
            return 3
        elif self.dealer_total >= self.user_total:
            return 4
        else:
            return 0

               
            
            

        






class UI():
    game = BlackJack()
    @classmethod
    def play_game(cls):        
        print("Welcome to Black Jack!")
        cls.game.user_show.clear()
        cls.game.dealer_show.clear()
        cls.game.dealer_hide.clear()
        while True:
            
            start_game = input("Start a new game? Type 'N' for no or 'ENTER' to start: ")
            if start_game.lower() == "n":
                print("Goodbye!")
                break
            cls.game.deal_cards()
            clear_screen()
            cls.game.dealer_score()
            cls.game.user_score()
            cls.game.show_hands()
            while True:
                response = input("Would you like another card? Enter 'Y' or 'N'")
                if response.lower() == "y":
                    cls.game.user_hit()
                    cls.game.user_check()
                    if cls.game.user_check:
                        break
                elif response.lower() == "n":
                    cls.game.dealer_turn()
                    break
                else:
                    print("Entry not valid - please try again.")
            if cls.game.end_game() == 7:
                clear_screen()
                print(f"{cls.game.dealer_hide}{cls.game.dealer_show}")
                print(cls.game.user_show)
                print("Dealer Blackjack!!!")
                cls.play_game()
            elif cls.game.end_game() == 8:
                clear_screen()
                print(f"{cls.game.dealer_hide}{cls.game.dealer_show}")
                print(cls.game.user_show)
                print("You have a Blackjack!!!")
                cls.play_game()
            if cls.game.end_game() == 1:
                clear_screen()
                print(f"{cls.game.dealer_hide}{cls.game.dealer_show}")
                print(cls.game.user_show)
                print("You bust! Dealer wins!")
                cls.play_game()
            elif cls.game.end_game() == 2:
                clear_screen()
                print(f"{cls.game.dealer_hide}{cls.game.dealer_show}")
                print(cls.game.user_show)
                print("Dealer busts! You win!")
                cls.play_game()
            elif cls.game.end_game() == 3:
                clear_screen()
                print(f"{cls.game.dealer_hide}{cls.game.dealer_show}")
                print(cls.game.user_show)
                print("You win!")
                cls.play_game()
            elif cls.game.end_game() == 4:
                clear_screen()
                print(f"{cls.game.dealer_hide}{cls.game.dealer_show}")
                print(cls.game.user_show)
                print("Dealer wins!")
                cls.play_game()
            

my_game = UI()
my_game.play_game()