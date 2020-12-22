
from copy import deepcopy


class Board :
  def __init__(self, board = [["1","2","3"], ["4","5","6"], ["7","8","9"]]) :
    self.board = board


  def allAvaliableMoves(self, player) :
    availableMoves = []
    if player.symbol == "X" :
      for row in range(3) :
        for columen in range(3) :
          if self.board[row][columen] != "X" and self.board[row][columen] != "O" :
            moveBoard = deepcopy(self.board)
            moveBoard[row][columen] = "X"
            move = moveBoard
            availableMoves.append(Board(board = move))
    else :
      for row in range(3) :
        for columen in range(3) :
          if self.board[row][columen] != "X" and self.board[row][columen] != "O" :
            moveBoard = deepcopy(self.board)
            moveBoard[row][columen] = "O"
            move = moveBoard
            availableMoves.append(Board(board = move))

    return availableMoves

  
  def show(self) :
    for r in self.board :
      print("     %s     |     %s     |     %s     "%(r[0],r[1],r[2]))


  def checkWin(self) :
    # check horzintals
    first = ""
    for r in self.board :
      first = r[0]
      if r[1] == first and r[2] == first :
        return first

    # check postive slop
    first = self.board[2][0]
    if self.board[1][1] == first and self.board[0][2] == first :
      return first

    
    # check neagative slop
    first = self.board[0][0]
    if self.board[1][1] == first and self.board[2][2] == first:
      return first


    # check columens
    for i in range(3) :
      columen = []
      for j in range(3) :
        columen.append(self.board[j][i])
      if columen[0] == columen[1] == columen[2] :
        return columen[0]

    return ""

  def isTie(self) :
    for r in self.board :
      for spot in r :
        if spot != "X" and spot != "O" :
          return False

    return True



class Player : 
  def __init__(self, symbol) :
    self.symbol = symbol

  def playMove(self, move, board) :
    board.board[move[0]][move[1]] = self.symbol



  def playBestMove(self, board, humanPlayer, aiPlayer) :
    bestScore = -100
    bestMove = None

    for move in board.allAvaliableMoves(aiPlayer) :
      # print(move.board)
      value = minimax(move, False, aiPlayer, humanPlayer)
      # print("value: ", value)
      if value > bestScore :
        bestScore = value
        bestMove = move

    board.board = bestMove.board


  



def isAvailableMove(board, x, y) :
  if board.board[x][y] != "X" and board.board[x][y] != "O" :
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



def starterChoic() :
  starter = input("enter who do you ant to start X or O: ")
  while starter.upper() != "X" and starter.upper() != "O" :
    print("please selecte either O or X")
    starter = input("enter who will start X or O: ")

  return starter.upper()



def main() :
  board = Board()

  human = humanChoic()
  starter = starterChoic()

  print(human)
  humanPlayer = Player(human)
  aiPlayer = Player("O") if humanPlayer.symbol == "X" else Player("X")

  print(":::::::: GAME STARTED ::::::::")

  while board.checkWin() == "" and not board.isTie() :

    if starter == aiPlayer.symbol :
      aiPlayer.playBestMove(board, humanPlayer, aiPlayer)
      if board.checkWin() != "" or board.isTie() :
        break
      board.show()
    else :
      board.show()

      

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


    move = (int(move[0]), int(move[1]))
    humanPlayer.playMove(move, board)
    if board.checkWin() != "" or board.isTie()  :
      break

    if starter == humanPlayer.symbol :
      aiPlayer.playBestMove(board, humanPlayer, aiPlayer)
      if board.checkWin() != "" or board.isTie() :
        break

    if board.checkWin() != "" or board.isTie()  :
      break
  

  print(":::::::: END OF THE GAME ::::::::")
  board.show()
  if board.checkWin() == "X" or board.checkWin() == "O" :
    winner = board.checkWin()
    print("the winner is ", winner)
  else :
    print("no one wins, it is a tie")



def minimax(board, isMaximizer, aiPlayer, humanPlayer) :
  # print(board.board)
  if board.checkWin() != "" or board.isTie() :
    if board.checkWin() == humanPlayer.symbol:
      return -1
    elif board.checkWin() == aiPlayer.symbol :
      return 1
    else :
      return 0


  if isMaximizer :
    bestValue = -100
    for move in board.allAvaliableMoves(aiPlayer) :
      value = minimax(move, False, aiPlayer, humanPlayer)
      bestValue = max(value, bestValue)
    return bestValue

  else :
    bestValue = 100
    for move in board.allAvaliableMoves(humanPlayer) :
      value = minimax(move, True, aiPlayer, humanPlayer)
      bestValue = min(value, bestValue)
    return bestValue


main()

