from deck import Deck
from player import Player
from war_card_game import WarCardGame


player = Player("AUP", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = WarCardGame(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("\nAre You Ready For The Next Round ?\nPress Enter To Continue. Enter X To Stop !")

    if answer.lower() == "x":
        break


