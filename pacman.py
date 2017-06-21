import random


"""
Add comments
"""
board = []
coins = []
level = None
class Person:
        def __init__(self):
                x = random.randint(1,15)
                y = random.randint(1,35)
                self.pos = [x,y]
        
        def get_pos(self):
                return self.pos
        
        def check_wall(self,x,y):
                if((x not in xrange(0,15)) or (y not in xrange(0,35))):
                        return True
                elif(board[x][y] == 'X'):
                        return True
                else:
                        return False

        def change_pos(self,move):
                x=int(self.pos[0])
                y=int(self.pos[1])
                if (move=="a"):
                        y-=1
                elif (move=="w"):
                        x-=1
                elif (move=="d"):
                        y+=1
                elif (move=="s"):
                        x+=1
                else:
                        return None
                if(self.check_wall(x,y) == False):
                        board[(self.pos[0])][(self.pos[1])]='.'
                        self.pos = [x,y]
                        return True
                else:
                        return False
        


class Pacman(Person):
        def __init__(self):
                self.pos = [11,20]
                self.score = 0
                board[11][20]='P'
        def collect_coin(self,x,y):
                if(board[x][y] == 'C'):
                        self.score+=1
                        coins.remove([x,y])
                        return True
                else:
                        return False
        
        def change_pos(self,move):
                if(Person.change_pos(self,move)):
                        self.collect_coin(self.pos[0],self.pos[1])
                        x = self.pos
                        if(board[x[0]][x[1]] == 'G'):
                                board[x[0]][x[1]] = 'P'
                                return False
                        else:
                                board[x[0]][x[1]] = 'P'
                                return True

                return None

        def get_score(self):
                return self.score

class Ghost(Person):
        def __init__(self):
                while True:
                        x = random.randint(0,14)
                        y = random.randint(0,34)
                        if((self.check_wall(x,y) == False) and (not ([x,y] == [11,20]))):
                                self.pos = [x,y]
                                board[x][y]='G'
                                break
        
        def change_pos(self,move):
                temp = eval("self.pos")
                if(Person.change_pos(self,move)):
                        x = self.pos
                        board[(x[0])][x[1]] = 'G'
                        if (temp in coins):
                                board[temp[0]][temp[1]] = 'C'
                        return True
                else:
                        return False

        
#function to create game board
def make_board():
        global board
        for i in xrange(0,15):
                temp=[]
                for j in xrange(0,35):
                        temp.append('.')
                board.append(temp)
        for i in xrange(4,9):
                board[2][i]='X'
                board[12][i]='X'
        for i in xrange(26,31):
                board[2][i]='X'
                board[12][i]='X'
        for i in xrange(3,6):
                board[i][4]='X'
                board[i][30]='X'
        for i in xrange(9,12):
                board[i][4]='X'
                board[i][30]='X'
        for i in xrange(5,10):
                board[i][9]='X'
                board[i][25]='X'
        for i in xrange(13,22):
                board[4][i]='X'
                board[10][i]='X'

#function for the output of the current game frame
def print_board():
        for i in board:
                for j in i:
                        print j,
                print '\n',

#function for the execution of game
make_board()
pac = Pacman()
ghosts=[]
coins = []
for i in xrange(0,(4)):
	x = Ghost()
	ghosts.append(x)
for i in xrange(0,20):
	while True:
	        x = random.randint(0,14)
                y = random.randint(0,34)
                if not( board[x][y] == 'X' or board[x][y] == 'P' or board[x][y] == 'G' or board[x][y] == 'C'):
  	              coins.append([x,y])
  	              board[x][y]='C'
                      break
                                        
def game():
        global board
        global level
        global coins
        level=1
        moves = ['a','w','d','s']
        while True:
                board = []
                make_board()
                pac = Pacman()
                ghosts=[]
                coins = []
                for i in xrange(0,(level+3)):
                        x = Ghost()
                        ghosts.append(x)
                for i in xrange(0,20+((level-1)*10)):
                        while True:
                                x = random.randint(0,14)
                                y = random.randint(0,34)
                                if not( board[x][y] == 'X' or board[x][y] == 'P' or board[x][y] == 'G' or board[x][y] == 'C'):
                                        coins.append([x,y])
                                        board[x][y]='C'
                                        break
                                        
                while True:
                           
                           print_board()
                           print "score: ",(pac.get_score())
                           print "your move: ",
                           move = raw_input()
                           if(move == "q"):
                                   return None
                           else:
                                   
                                   for i in ghosts:
                                           if(level == 1):
                                                   while True:
                                                           temp = random.randint(0,3)
                                                           if(i.change_pos(moves[temp])):
                                                                   break
                                           elif(level >= 2):
                                                   pos = i.get_pos()
                                                   chase = pac.get_pos()
                                                   temp = ['a','w','d','s']
						   iter_count = 0
                                                   while True:
                                                           if(iter_count<2):
                                                                   if(pos[0]>chase[0]):
									   iter_count+=1
                                                                           if(i.change_pos("w")):
                                                                                   break
                                                                           else:
									   	if "w" in temp:
                                                                                	temp.remove("w")
                                                                   if(pos[0]<chase[0]):
									   iter_count+=1
                                                                           if(i.change_pos("s")):
                                                                                   break
                                                                           else:
										if "s" in temp:
                                                                                	temp.remove("s")
                                                                   if(pos[1]>chase[1]):
									   iter_count+=1
                                                                           if(i.change_pos("a")):
                                                                                   break
                                                                           else:
										if "a" in temp:
                                                                                	temp.remove("a")
                                                                   if(pos[1]<chase[1]):
									   iter_count+=1
                                                                           if(i.change_pos("d")):
                                                                                   break
                                                                           else:
										if "d" in temp:
                                                                                	temp.remove("d")
                                                           else:
                                                                   r_move = random.randint(0,1)
                                                                   i.change_pos(temp[r_move])
							           break
                                   if(pac.change_pos(move) == False):
                                           print_board()
                                           print "gameover"
                                           print "final score: ", pac.get_score()
                                           print "q to quit and r to restart",
                                           res = raw_input()
                                           if(res == "q"):
                                                   return True
                                           else:
                                              level = 1
                                              break
                                   if(len(coins) == 0):
                                           print_board()
                                           print "********Congrats********\n********level:",level," completed********"
                                           if(level<3):
                                                   level+=1
                                                   break
                                           else:
                                                   print "******Congrats******\n*******Game Completed********"
                                                   print "finalscore: ", pac.get_score()
                                                   print "q to quit r to restart",
                                                   res = raw_input()
                                                   if(res == "q"):
                                                           return True
                                                   else:
                                                           level =1
                                                           break                

#game()               
