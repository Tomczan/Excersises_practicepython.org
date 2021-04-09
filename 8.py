# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

info = """Rock, Paper, Scissors """

def rps_game():
    while True:
        print("PLAYER 1: Choose", info, "or type end to end a game.")
        player1 = input()
        if player1 == "end":
            break
        
        print("PLAYER 2: Choose", info, "or type end to end a game.")
        player2 = input()
        if player2 == "end":
            break
        
        if player1 == player2:
            print("Draw")
            continue
        elif player1 == "Rock":
            if player2 == "Scissors":
                print("Player 1 win")
                continue
            elif player2 == "Paper":
                print("Player 2 win")
                continue
        elif player1 == "Scissors":
            if player2 == "Paper":
                print("Player 1 win")
                continue
            elif player2 =="Rock":
                print("Player 2 win")
                continue
        elif player1 == "Paper":
            if player2 == "Rock":
                print("Player 1 win")
                continue
            elif player2 =="Scissors":
                print("player 2 win")


rps_game()            
