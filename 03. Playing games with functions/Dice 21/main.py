import game

print("--- Your turn ---")
user_total = game.play_user_turn()
print(">> That's a " + game.get_name(user_total) + "!")
    
print("--- Computer turn ---")
computer_total = game.play_computer_turn(user_total)
print(">> The computer has a " + game.get_name(computer_total) + ".")
    
winner = game.get_winner(user_total, computer_total)
print("GAME OVER: " + winner + " wins!")