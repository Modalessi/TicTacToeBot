

def creatBoard() :
  board = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
  ]

  return board




def play(player,board,x,y) :
  board[x][y] = player
  return board

  
def checkWin(board) :
  # check horzintals
  first = ""
  for r in board :
    first = r[0]
    if r[1] == first and r[2] == first :
      return first

  # check postive slop
  first = board[2][0]
  if board[1][1] == first and board[0][2] == first :
    return first

    
  # check neagative slop
  first = board[0][0]
  if board[1][1] == first and board[2][2] == first:
    return first


  # check columens
  for i in range(3) :
    columen = []
    for j in range(3) :
      columen.append(board[j][i])
    
    if columen[0] == columen[1] == columen[2] :
      return columen[0]



  return ""



def showBoard(board) :
  for r in board :
    print("     %s     |     %s     |     %s     "%(r[0],r[1],r[2]))



def isAvailableMove(board, x, y) :
  if board[x][y] != "X" and board[x][y] != "O" :
    return True
  else :
    return False


def translateMove(move) :
  moves = {
    "1" : "00",
    "2" : "01",
    "3" : "02",
    "4" : "10",
    "5" : "11",
    "6" : "12",
    "7" : "20",
    "8" : "21",
    "9" : "22"
  }

  return moves[move]


def humanChoic() :
  human = input("enter what do you want to play with X or O: ")

  while human.upper() != "X" and human.upper() != "O" :
    print("please selecte either O or X")
    human = input("enter who will start X or O: ")

  return human.upper()


def validateInput(string) :
  for i in string :
    if not i.isdigit() :
      return False
  
  if len(string) != 1  :
    return False

  return True





def isTie(board) :

  for r in board :
    for spot in r :
      if spot != "X" and spot != "O" :
        return False

  return True


def starterChoic() :
  starter = input("enter who do you ant to start X or O: ")
  while starter.upper() != "X" and starter.upper() != "O" :
    print("please selecte either O or X")
    starter = input("enter who will start X or O: ")

  return starter.upper()



def main() :
  board = creatBoard()

  human = humanChoic()
  starter = starterChoic()

  bot = "X" if human == "O" else "O"
  print(":::::::: GAME STARTED ::::::::")


  while checkWin(board) == "" and not isTie(board) :


    if starter == bot :
      aiTurn(board, bot, human)
      if checkWin(board) != "" or isTie(board) :
        break
      showBoard(board)
    else :
      showBoard(board)

      


    flag = True

    while flag :
      move = input("enter where you want to play %s:"%(human))
      
      while not validateInput(move) :
        print("invalid input, please select number from the board above")
        move = input("enter where you want to play :")

      move = translateMove(move)

      if isAvailableMove(board, int(move[0]), int(move[1])) :
        flag = False
      else :
        print("not Available Move, pick another one")

    play(human,board,int(move[0]),int(move[1]))
    if checkWin(board) != "" or isTie(board)  :
      break

    if starter == human :
      aiTurn(board, bot, human)
      if checkWin(board) != "" or isTie(board) :
        break

    if checkWin(board) != "" or isTie(board)  :
      break
  

  print(":::::::: END OF THE GAME ::::::::")
  showBoard(board)
  if checkWin(board) == "X" or checkWin(board) == "O" :
    winner = checkWin(board)
    print("the winner is ", winner)
  else :
    print("no one wins, it is a tie")





def aiTurn(board, botChar, human) :
  aiMove = bestMove(board, botChar, human)
  board[aiMove[0]][aiMove[1]] = botChar



def bestMove(board , bot, human) :
  bestValue = -100
  bestMove = None
  for r in range(3) :
    for j in range(3) :
      if board[r][j] != "X" and board[r][j] != "O" :
        boxNum = board[r][j]
        board[r][j] = bot
        value = minimax(board, 0, False, bot, human)
        board[r][j] = boxNum
        if value > bestValue :
          bestValue = value
          bestMove = (r,j)
  
  return bestMove




def minimax(board, depth, isMaximizer, bot, human) :
  #print(board)
  if checkWin(board) != "" or isTie(board):
    if checkWin(board) == human:
      return -1
    elif checkWin(board) == bot :
      return 1
    else :
      return 0


  if isMaximizer :
    bestValue = -100
    for r in range(3) :
      for j in range(3) :
        if board[r][j] != "X" and board[r][j] != "O" :
          boxNum = board[r][j]
          board[r][j] = bot
          value = minimax(board, depth + 1, False, bot, human)
          board[r][j] = boxNum
          if value > bestValue :
            bestValue = value
    return bestValue

  else :
    bestValue = 100
    for r in range(3) :
      for j in range(3) :
        if board[r][j] != "X" and board[r][j] != "O" :
          boxNum = board[r][j]
          board[r][j] = human
          value = minimax(board, depth + 1, True, bot, human)
          board[r][j] = boxNum
          if value < bestValue :
            bestValue = value
    return bestValue

          
  #test
  #this one is to test gitlens
  



main()
print("ohhh that is very cool hahah :)")

  



# this is just a comment removed the s
