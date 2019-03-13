
########################
## This  scalable project is about a game called 'Grow and Shrink but Dot't Die' is about a ball that the player will try to survive with it with highest score possible
#there are two types of food to eat , the first one is blue and incereases both
# size and strats with certain sized-ball and has only one minute to score highes possible record
# The player has to track the position of the desired food using mouse left clicks to control the path of the ball
# The game ends if the time runs out or his ball shrinks to zero size
###################
###Code depiction##
# This project has functions based on tkinter and random modules
# the program starts with __init__ function that initiate the attributes of the classs
# then we defined the start function to start the game and end function to end the game play not the game itself
# we defined the function run to run the game  by calling itself every 10 millesceond
#we defined functions for makeing the ball to move and functions for the food types.(grow,shrink,move)
# We also defined a function to control the movement of the ball using the mouse left clicks (mouse_click)
# we defined the function animate to create the balls object .
#Those are the most fundamental function and we hae defined other side functions for handling errors and for adding more luxurious options
# (i.e. highest_scores,help,name_entry)




from tkinter import *
from random import *
import tkinter.messagebox as tik


class game:
    def __init__(self):
        self.point = ''
        self.main_window = Tk()
        self.main_window.title('Ball Game')
        self.controller = False    # for controlling the program
        self.scores = {}
        self.frame = Frame(bg="black").pack()
        self.clock = Label(self.frame, bg="black", fg="white")
        self.clock.pack()
        self.canvas = Canvas(self.frame, bg="black", width=400, height=400) # building the graphical window used for the game.
        self.canvas.pack()


        self.points = Label(self.frame, bg="black", fg="white") # scoring points
        self.points.pack()
        self.playerN = Label(self.frame, bg="black", fg="white",text = 'Player name:').pack()

        self.name = Entry(self.frame, width=15)
        self.name.pack()
        self.button2 = Button(self.frame, bg="black", fg="white", text="Save your name to save score", command=self.name_entry).pack(
            side='left')
        self.button4 = Button(self.frame, bg="black", fg="white", text="Help", command=self.help).pack(side='right')

        self.button3 = Button(self.frame, bg="black", fg="white", text="Players Scores", command=self.highest_scores).pack(
            side='right')
        self.button = Button(self.frame, bg="black", fg="white", text="Click to start", command=self.start).pack(
            side='right')

        self.main_window.mainloop()

    def start(self):    # the start function for initiating the game everytime
        if self.controller == True:
            tik.showinfo('Warning', 'The game is already running!')
            return
        self.time = 0
        self.controller = True
        self.point = 0
        self.size = 3         # initial size of the ball
        self.UP = False        # initial directions
        self.RIGHT = False
        self.DOWN = False
        self.LEFT = False

        self.grower_x = []    # x coordinate for thw food which grows size
        self.grower_y = []    # y coordinate for thw food which grows size

        self.shrinker_x = []    # x coordinate for thw food which shrinks size
        self.shrinker_y = []    # x coordinate for thw food which shrinks size


        self.TEXT = "Welcome to Seeking Survival"
        self.x = 200    # initial x position
        self.y = 200    # initial y position
        self.tempx = 0
        self.tempy = 0

        self.canvas.bind("<ButtonPress-1>", self.mouse_click)      # the event is  A mouse left click is pressed over the widget and the handler is the function mouse_click
        self.run()                   # run the game using run function

# time changes every 10 milliseconds
    def grow(self, ball):
        if len(self.grower_x) < self.time // 1000 + 1:     #  the more time we pass the more grow pieces we find
            self.grower_x.append(randint(20, 380))    # create random grow elements , the same applies for shrink
        if len(self.grower_y) < self.time // 1000 + 1:
            self.grower_y.append(randint(20, 380))
        for i in range(len(self.grower_x)):
            self.canvas.create_rectangle(self.grower_x[i], self.grower_y[i],self.grower_x[i] +10,  self.grower_y[i] + 10,
                                         fill="blue")   # create
        for i in range(len(self.grower_x)):
            if len(self.canvas.find_overlapping(self.grower_x[i], self.grower_y[i], self.grower_x[i] + 10,
                                                self.grower_y[i] + 10)) >= 1:      #find_overlapping as a collision handler for the grow elements
                if ball in self.canvas.find_overlapping(self.grower_x[i], self.grower_y[i], self.grower_x[i] + 10,
                                                        self.grower_y[i] + 10):    #Finds all items that overlap the given rectangle, or that are completely enclosed by it.
                    self.point += 100
                    self.size += 0.3
                    self.grower_x.pop(i)           # we don't need them any more
                    self.grower_y.pop(i)
                    self.grow(ball)

    def shrink(self, ball):
        if len(self.shrinker_x) < self.time // 1000 + 1:     # the more time we pass the more shrink pieces we find
            self.shrinker_x.append(randint(20, 380))
        if len(self.shrinker_y) < self.time // 1000 + 1:
            self.shrinker_y.append(randint(20, 380))
        for i in range(len(self.shrinker_x)):
            self.canvas.create_rectangle(self.shrinker_x[i],  self.shrinker_y[i], self.shrinker_x[i] + 12,self.shrinker_y[i] + 12,
                                         fill="red")
        for i in range(len(self.shrinker_x)):
            if len(self.canvas.find_overlapping(self.shrinker_x[i], self.shrinker_y[i], self.shrinker_x[i] + 10,
                                                self.shrinker_y[i] + 10)) >=1:
                if ball in self.canvas.find_overlapping(self.shrinker_x[i], self.shrinker_y[i], self.shrinker_x[i] + 10,
                                                        self.shrinker_y[i] + 10):

                    self.size -= 0.5
                    self.point -= 50
                    self.shrinker_x.pop(i)
                    self.shrinker_y.pop(i)
                    self.shrink(ball)



    def animate(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(100, 100,  fill="green")

        if self.time // 100 <= 60:   #1 minute is our limit
            if 10 * self.size > 8:

                ball = self.canvas.create_oval(self.x - 10 * self.size, self.y - 10 * self.size, self.x + 10 * self.size, self.y + 10 * self.size, fill="white")    # create our ball

                self.shrink(ball)
                self.grow(ball)

            elif 10 * self.size > 150:
                self.clock['text'] = "Game Over"
                self.end()

            else:
                self.clock['text'] = "Game Over"
                self.end()
        else:
            self.clock['text'] = "Time's up"
            self.end()

    def move(self, b, speed):                             # this function is responsible for our ball movement    self.move(10 * self.size, 2.5)
        if self.UP == True and self.y - b > 0:    # define our boundaries
            self.y -= speed
        elif self.UP == True and self.y - b <= 0:
            self.UP = False
            self.DOWN = True
        if self.DOWN == True and self.y + b < 400:
            self.y += speed
        elif self.DOWN == True and self.y + b >= 400:
            self.DOWN = False
            self.UP = True
        if self.RIGHT == True and self.x + b < 400:
            self.x += speed
        elif self.RIGHT == True and self.x + b >= 400:
            self.RIGHT = False
            self.LEFT = True
        if self.LEFT == True and self.x - b > 0:
            self.x -= speed
        elif self.LEFT == True and self.x - b <= 0:
            self.LEFT = False
            self.RIGHT = True

    def mouse_click(self, event):       # this function for defining the control of the ball path usin mouse left clicks
        self.tempx = event.x            # event.x and event.y are the coordinates where the mouse left clicks
        self.tempy = event.y
        if event.y > self.y and self.y != self.tempy:
            self.DOWN = True
            self.UP = False
        elif event.y < self.y and self.y != self.tempy:
            self.UP = True
            self.DOWN = False
        else:
            self.y = self.tempy
            self.DOWN = False
            self.UP = False
        if event.x > self.x and self.x != self.tempx:
            self.RIGHT = True
            self.LEFT = False
        elif event.x < self.x and self.x != self.tempx:
            self.LEFT = True
            self.RIGHT = False
        else:
            self.x = self.tempx
            self.RIGHT = False
            self.LEFT = False


    def run(self):  # run the game  it is called every 10 milliseconds this function runs every other function
        if self.controller is True:
            self.time += 1
            self.points['text'] = "Scored Points: " + str(self.point)
            self.clock['text'] = "TIME:" + str(self.time // 100)  # 10 *100 = 1 second

            self.move(10 * self.size, 2.5)
            self.animate()
            self.main_window.after(10, self.run)

    def name_entry(self):
        playername = self.name.get()
        if playername =='':
            tik.showinfo('Warning','You must write your name first!')
        if self.point=='':
            tik.showinfo('Warning', 'You must play first before saving your score!')
            return
        self.scores[playername] = self.point


    def highest_scores(self):
       score_page =  Toplevel()
       score_page.title('Scores')
       score_page.geometry('300x300')
       LList_scores = 'Player  :  Score\n'
       for player in self.scores:
           row = player+'   :   '+str(self.scores[player])+'\n'
           LList_scores+=row
       self.label5= Label(score_page,text =LList_scores )
       self.label5.pack()

    def help(self):
        help_page = Toplevel()
        help_page.title('Help')
        help_page.geometry('800x300')

        # Create widges in the new window
        self.label4 = Label(help_page, text= """ 'Grow and Shrink but Dot't Die'\n 
        You have to survive grow and shrink as fas as possible to get the highest score possible.\n
        There are two types of food to eat , the first one  increases both size and score of the ball. 
         the second  makes the ball shrinks and decreases the score.
          \n Remember! you have only one minute to score.\n
           Track the position of the desired food using mouse left clicks.\n
           Becareful being too small or too big otherwise you will lose.\n
         The game ends if the time runs out or his ball shrinks to zero size. """, fg='black')
        self.label4.pack()
        help_page.focus_set()


    def end(self):
        self.controller = False
        self.canvas.unbind("<ButtonPress-1>")   # unbind the mouse click out of the canvas




app = game()

