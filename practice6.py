p1=input("Player 1, Enter your move (rock, paper, scissors):").lower()
p2=input("Player 2, Enter your move (rock, paper, scissors):").lower()
if p1=='rock':
    if p2=='rock':
        print("Its tie!")
    elif p2=='paper':
        print("Player 2 wins!")
    elif p2=="scissors":
        print("Player 1 wins!")
    else:
        print("Invalid move by Player 2.")
elif p1=="paper":
    if p2=='paper':
        print("Its tie!")
    elif p2=='scissors':
        print("Player 2 wins!")
    elif p2=="rock":
        print("Player 1 wins!")
    else:
        print("Invalid move by Player 2.")
elif p1=="scissors":
    if p2=="scissors":
        print("Its tie!")
    elif p2=='rock':
        print("Player 2 wins!")
    elif p2=="paper":
        print("Player 1 wins!")
    else:
        print("Invalid move by Player 2.")
else:
    print("Invalid move by player 1.")