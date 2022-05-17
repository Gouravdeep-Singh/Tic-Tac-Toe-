board=["_","_","_",
       "_","_","_",
       "_","_","_"]

def makingboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])


winner=0
def check():
    global winner
    if board[0]==board[1]==board[2]=="x":
        print("Player 1 wins")
        winner=1
    elif board[0]==board[1]==board[2]=="0":
        print("Player 2 wins")
        winner=2
    elif board[3]==board[4]==board[5]=="x":
        print("Player 1 wins")
        winner=1 
    elif board[3]==board[4]==board[5]=="0":
        print("Player 2 wins")
        winner=2
    elif board[6]==board[7]==board[8]=="x":
        print("Player 1 wins")
        winner=1
    elif board[6]==board[7]==board[8]=="0":
        print("Player 2 wins")
        winner=2
    elif board[0]==board[3]==board[6]=="x":
        print("Player 1 wins")
        winner=1
    elif board[0]==board[3]==board[6]=="0":
        print("Player 2 wins")
        winner=2
    elif board[1]==board[4]==board[7]=="x":
        print("Player 1 wins")
        winner=1
    elif board[1]==board[4]==board[7]=="0":
        print("Player 2 wins")
        winner=2
    elif board[2]==board[5]==board[8]=="x":
        print("Player 1 wins")
        winner=1
    elif board[2]==board[5]==board[8]=="0":
        print("Player 2 wins")
        winner=2
    elif board[0]==board[4]==board[8]=="x":
        print("Player 1 wins")
        winner=1
    elif board[0]==board[4]==board[8]=="0":
        print("Player 2 wins")
        winner=2
    elif board[2]==board[4]==board[6]=="x":
        print("Player 1 wins")
        winner=1
    elif board[2]==board[4]==board[6]=="0":
        print("Player 2 wins")
        winner=2
    else:
        pass
        

print("The game board ranges from 0-8")
for i in range(20):
    print("Enter location for player 1:")
    inp = int(input())
    if board[inp]=="_":
        board[inp] = "x"
    else:
        print("position already occupied,enter again: ")
        inp = int(input())
        board[inp] = "x"
    makingboard(board)
    check()
    if winner>0:
        break
    if i==4:
        print("Tie!")
        break
    
    print("Enter location for player 2:")
    inp = int(input())
    if board[inp]=="_":
        board[inp] = "0"
    else:
        print("position already occupied,enter again: ")
        inp = int(input())
        board[inp] = "0"
    makingboard(board)
    check()
    if winner>0:
        break
    
    







