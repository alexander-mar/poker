#game is a better hand evaluator that teaches you which hand is better, including pre, post, river, turn, etc..


#game loading screen and instructions
def game_intro():
    
    print("Welcome to Poker hand evaluator training")
    print("Enter 's' to start")

#loading first hand of cards and then passing through to the poker
def game_start():
    
    print("Welcome to Poker")
    #give list of moves


def main():

    started = False
    #main loop of the game
    while True:

        if not started:
            game_intro()
            started = True

        inp = input("Input a move: ")
        inp = inp.lower()

        if inp == 'start':
            game_start()
        
        elif inp in ['raise', 'call', 'check', 'fold']:
            move_converter(inp)

        else:
            print("enter a valid move")

if __name__ == "__main__":
    main()