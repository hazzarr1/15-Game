#imports alllll the good things you need the code to work
from random import randint
import os
import time
import csv








difficulty = 0



starttime = time.time()

NumberMoves = 0


# Timer starts
        
lasttime = starttime

  

timer = True




#loading screen animation; even though nothing is really loading, gives the game some gravitas 
for x in range(6):



        os.system('cls')
        f= open ('Loading 1.txt','r')
        print(''.join([line for line in f]))
        time.sleep(0.05)
        
        os.system('cls')
        f= open ('Loading 2.txt','r')
        print(''.join([line for line in f]))
        time.sleep(0.05)

        os.system('cls')
        f= open ('Loading 3.txt','r')
        print(''.join([line for line in f]))
        time.sleep(0.05)

        os.system('cls')
        f= open ('Loading 4.txt','r')
        print(''.join([line for line in f]))
        time.sleep(0.05)
        os.system('cls')


#Welcome screen
for x in range(1):



        os.system('cls')
        f= open ('Welcome 1.txt','r')
        print(''.join([line for line in f]))
        time.sleep(0.1)
        
        os.system('cls')
        f= open ('Welcome 2.txt','r')
        print(''.join([line for line in f]))
        time.sleep(0.1)

        os.system('cls')
        f= open ('Welcome 3.txt','r')
        print(''.join([line for line in f]))
        time.sleep(0.1)

        os.system('cls')
        f= open ('Welcome 4.txt','r')
        print(''.join([line for line in f]))
        time.sleep(0.1)
        os.system('cls')















#logo
f= open ('logo.txt','r')

print(''.join([line for line in f]))

#gets name from user
username=input("whats ya name: ")
 
class Puzzle:

     


     
    def __init__(self):
        self.items = {}
        self.position = None
 
    def main_frame(self):
        d = self.items
        #clears cmd each time a new board is created, eliminating previous boards for astetic reasons
        os.system('cls')

        f= open ('logo.txt','r')

        print(''.join([line for line in f]))
       


        #main design of the game board
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[1], d[2], d[3], d[4])),
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[5], d[6], d[7], d[8]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[9], d[10], d[11], d[12]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[13], d[14], d[15], d[16]))
        print('+-----+-----+-----+-----+')

        
    #difficulty    
    def format(self, ch):
        ch = ch.strip()
        if len(ch) == 1:
            return '  ' + ch + '  '
        elif len(ch) == 2:
            return '  ' + ch + ' '
        elif len(ch) == 0:
            return '     '

#changes position of tile     
    def change(self, to):
        fro = self.position
        for a, b in self.items.items():
            if b == self.format(str(to)):
                to = a
                break
        self.items[fro], self.items[to] = self.items[to], self.items[fro]
        self.position = to
 
    def build_board(self, difficulty):

        # dificulty
        for i in range(1, 17):
            self.items[i] = self.format(str(i))
        tmp = 0
        for a, b in self.items.items():
            if b == '  16 ':
                self.items[a] = '     '
                tmp = a
                break
        self.position = tmp
        if difficulty == 0:
            diff = 10
        elif difficulty == 1:
            diff = 50
        else:
            diff = 100
        for _ in range(diff):
            lst = self.valid_moves()
            lst1 = []
            for j in lst:
                lst1.append(int(j.strip()))
            self.change(lst1[randint(0, len(lst1)-1)])

 #calculates all valid moves for the user
    def valid_moves(self):
        pos = self.position
        if pos in [6, 7, 10, 11]:
            return self.items[pos - 4], self.items[pos - 1],\
                   self.items[pos + 1], self.items[pos + 4]
        elif pos in [5, 9]:
            return self.items[pos - 4], self.items[pos + 4],\
                   self.items[pos + 1]
        elif pos in [8, 12]:
            return self.items[pos - 4], self.items[pos + 4],\
                   self.items[pos - 1]
        elif pos in [2, 3]:
            return self.items[pos - 1], self.items[pos + 1], self.items[pos + 4]
        elif pos in [14, 15]:
            return self.items[pos - 1], self.items[pos + 1],\
                  self.items[pos - 4]
        elif pos == 1:
            return self.items[pos + 1], self.items[pos + 4]
        elif pos == 4:
            return self.items[pos - 1], self.items[pos + 4]
        elif pos == 13:
            return self.items[pos + 1], self.items[pos - 4]
        elif pos == 16:
            return self.items[pos - 1], self.items[pos - 4]
 
    def game_over(self):
        flag = False
        for a, b in self.items.items():
            if b == '     ':
                pass
            else:
                if a == int(b.strip()):
                    flag = True
                else:
                    flag = False
        return flag
 









 










#Dificulty selection
g = Puzzle()
g.build_board(int(input('Enter the difficulty : 0 1 2\n2 '
                        '=> highest 0=> lowest\n')))
g.main_frame()
print('Enter 0 to exit')
while True:
        #prints hello (username) and gives instructions to the user 
    print(f'Hello {username}:\nTo change the position just enter the number near it')
       
    lst = g.valid_moves()
    lst1 = []
    for i in lst:
        lst1.append(int(i.strip()))
        print(i.strip(), '\t', end='')
        

       


        

        


#whole module continues running the board until the user completes the board or presses 0 to exit
#also checks the allowed moves list, for wring moves 
    
    x = int(input())
    
    if x == 0:
        break
    elif x not in lst1:
        print('Wrong move\nTry again:')
    else:
        g.change(x)
        NumberMoves += 1
    g.main_frame()
        
    if g.game_over():
        
        totaltime = round((time.time() - starttime), 2)
        break
        
        

              
   
    
   
    











#collects user data and packages it into a csv file, used as the leaderboard 


print('You Won!!!!')

with open ("Leaderboard.csv", "a", newline='') as file:
    fields=['name', 'moves', 'time', 'difficulty']
    writer=csv.DictWriter(file, fieldnames=fields)
    writer.writerow({'name' : username, 'moves' : NumberMoves, 'time' : totaltime, 'difficulty' : difficulty})

#for use in debugging, sorts the leaderbaord into from high score to low score 
with open ("Leaderboard.csv", "r") as file:
    sortlist=[]
    reader=csv.reader(file)
    for i in reader:
        sortlist.append(i)
for i in range(len(sortlist)):
    if i != 0:
        sortlist[i][0]=int(sortlist[i][int(0)])


print("")

print("Unsorted:")
for i in range(len(sortlist)):
    print(sortlist[i])


for i in range(555):
    for i in range(len(sortlist)-1):
        if i != 0:
            if sortlist[i][0] < sortlist[i+1][0]:
                change=sortlist[i]
                sortlist[i]=sortlist[i+1]
                sortlist[i+1]=change


print("")

print("Sorted and cut:")
for i in range(len(sortlist)-1):
    print(sortlist[i])      

        























