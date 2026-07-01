import typer

print("Type the words and hit enter within the time limit!\n")
level = int(input("Select one of these levels (1-5):\n\n" +
      "\t1. Beginner\n" +
      "\t2. Easy\n" +
      "\t3. Medium \n" + 
      "\t4. Advanced\n" +
      "\t5. Expert :)\n\n"))

words_comp = 0

# Play three rounds of a speed typing game.
for round in range(1, level + 1):
    print("Level " + str(round))

    num_words = typer.get_level_words(round)   
    mode = typer.get_level_mode(round)
    secs = typer.get_level_seconds(round)

    words_to_type = typer.pick_random_words(num_words, mode)
    passed = typer.play_round(words_to_type, secs)
    if passed:
        words_comp += 1
        print("Congratulations, you completed the level <3")
    if not passed:
        print("Oops!")
        break
print("You completed " + str(words_comp) + 
      " out of " + str(level) + " levels.")
print("Thanks for playing.")
