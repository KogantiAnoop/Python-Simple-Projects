"""HW5 template"""
from graphics import *
import time
import random

class Car(Rectangle):
    def __init__(self, win, x, y, unit):
        self.unit = unit
        self.x = x
        self.y = y
        p1 = Point(x - unit *4,y)
        p2 = Point(x + unit *4,y +unit * 3)     #basis points to make things easier
        super().__init__(p1,p2)
        colorlist = ["green","yellow","red","purple","orange","blue"]
        self.color = colorlist[random.randrange(len(colorlist))]        #gets random color values
        
        
        p3 = Point(0,y + unit * 4)
        # self.parts= []
        
        # self.leftTire = Circle(Point(p1.getX() + (p2.getX() - p1.getX()) / 4, y), abs(p2.getX() - p1.getX())/8)
        # self.leftTire.setFill("Black")          #Used to create the left tire           
        # self.parts.append(self.leftTire)
        
        # self.rightTire = Circle(Point(p1.getX() + (p2.getX() - p1.getX()) *3 / 4, y), abs(p2.getX() - p1.getX())/8 )
        # self.rightTire.setFill("Black")         #Used to create the right tire
        # self.parts.append(self.rightTire)
        
        # self.body = Rectangle(p1,p2)
        # self.body.setFill(self.color)              #used to create the body
        # self.parts.append(self.body)
        
        # self.roof = Polygon(Point(p1.getX() + unit * 2,p2.getY()), Point(abs(p2.getX() - unit * 5),p3.getY()), Point(abs(p2.getX() - unit * 3),p3.getY()), Point(p2.getX() - unit * 2, p2.getY()))
        # self.roof.setFill("black")              #used to create the roof properly
        # self.parts.append(self.roof)

        self.score =int(unit * 10)

        self.drawCar(p1,p2,p3,win)

        
    def getColor(self):
        return self.color       #returns random color

    def getScore(self):
        return self.score       #Gets score which later on gets properly proportioned to make smaller cars more valuable then bigger ones

    def drawCar(self,p1,p2,p3, win):
        self.parts= []
        
        self.leftTire = Circle(Point(p1.getX() + (p2.getX() - p1.getX()) / 4, self.y), abs(p2.getX() - p1.getX())/8)
        self.leftTire.setFill("Black")          #Used to create the left tire           
        self.parts.append(self.leftTire)
        
        self.rightTire = Circle(Point(p1.getX() + (p2.getX() - p1.getX()) *3 / 4, self.y), abs(p2.getX() - p1.getX())/8 )
        self.rightTire.setFill("Black")         #Used to create the right tire
        self.parts.append(self.rightTire)
        
        self.body = Rectangle(p1,p2)
        self.body.setFill(self.color)              #used to create the body
        self.parts.append(self.body)
        
        self.roof = Polygon(Point(p1.getX() + self.unit * 2,p2.getY()), Point(abs(p2.getX() - self.unit * 5),p3.getY()), Point(abs(p2.getX() - self.unit * 3),p3.getY()), Point(p2.getX() - self.unit * 2, p2.getY()))
        self.roof.setFill("black")              #used to create the roof properly
        self.parts.append(self.roof)
        
        for part in self.parts:
            part.draw(win)              #draws the car by running through a list and drawing each component

    def move(self, Xdistance):
        for part in self.parts:     #same as above but moves each component
            part.move(Xdistance,0)
            
    def undraw(self):
        for part in self.parts:
            part.undraw()           #same as above but removes each component
def isClicked(pclick,rec):
    if rec.p1.x <= pclick.x <= rec.p2.x and rec.p1.y <= pclick.y <= rec.p2.y:

        return True             #uses rectangle p1 and p2 locations and their x and y values to determine if click is inside the the box.
    return False
    
def draw_buildings(win, p1_x,p1_y,p2_x,p2_y,color):
    shape=Rectangle(Point(p1_x,p1_y),Point(p2_x,p2_y))
    shape.setFill(color)
    shape.draw(win)

def main():
    win = GraphWin("Moving Cars", 800, 600)
    win.setCoords(0, 0, 40, 40)

    bg = Rectangle(Point(0,25), Point(40, 40))
    bg.setFill("light blue")
    bg.draw(win)

    ground = Rectangle(Point(0,6) , Point(40, 24))
    ground.setFill("light grey")
    ground.draw(win)
    temp=4
    
    while temp<40:
        gnd_lines1= Line(Point(temp,10),Point(temp+4,10))
        gnd_lines1.setWidth(5)
        gnd_lines1.setFill("white")
        gnd_lines2= Line(Point(temp,15),Point(temp+4,15))
        gnd_lines2.setWidth(5)
        gnd_lines2.setFill("white")
        gnd_lines3= Line(Point(temp,20),Point(temp+4,20))
        gnd_lines3.setWidth(5)
        gnd_lines3.setFill("white")
        temp=temp+10
        gnd_lines1.draw(win)
        gnd_lines2.draw(win)
        gnd_lines3.draw(win)

    sun = Circle(Point(37,38), 1.5)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(win)

    with open('hw5_input.txt','r') as file:
     # reading each line
        for line in file:
            coordinates=[]
            # reading each word
            for word in line.split():
             # displaying the words
                coordinates.append(word)
            draw_buildings(win,coordinates[0],coordinates[1],coordinates[2],coordinates[3],coordinates[4])


    button = Rectangle(Point(2,2), Point(6, 4))
    button.setFill("gray")
    button.draw(win)
    label = Text(Point(4, 3), "Start")
    label.setStyle("bold")
    label.setTextColor("white")
    label.draw(win)

    bottom_message = Text(Point(12, 5), "Please click the Start button to begin")
    bottom_message.setStyle("bold")
    bottom_message.setTextColor("green")
    bottom_message.draw(win)
    car_on_screen_message = Text(Point(15, 27), "")
    car_on_screen_message.setStyle("bold")
    car_on_screen_message.setTextColor("purple")
    car_on_screen_message.draw(win)
    score_title = Text(Point(15, 3), "Current Score: ")
    score_title.setStyle("bold")
    score_title.setSize(18)
    score_title.setTextColor("blue")
    score_title.draw(win)
    score_message = Text(Point(21, 3), "0")
    score_message.setStyle("bold")
    score_message.setSize(18)
    score_message.setTextColor("blue")
    score_message.draw(win)
    clicked_colors_message = Text(Point(29, 5), "")
    clicked_colors_message.setStyle("bold")
    clicked_colors_message.setTextColor("black")
    clicked_colors_message.draw(win)

    exit_bg = Rectangle(Point(10,5), Point(30, 20))
    exit_bg.setFill("light gray")
    exit_message = Text(Point(20, 15), "Click Exit to stop \n or Resume to continue")
    exit_message.setSize(18)
    exit_message.setStyle("bold")
    exit_message.setTextColor("red")
    confirm_button = Rectangle(Point(13, 7), Point(17, 9))
    confirm_button.setFill("gray")
    confirm_label = Text(Point(15, 8), "Exit")
    confirm_label.setStyle("bold")
    confirm_label.setTextColor("white")
    go_back_button = Rectangle(Point(23, 7), Point(27, 9))
    go_back_button.setFill("gray")
    go_back_label = Text(Point(25, 8), "Resume")
    go_back_label.setStyle("bold")
    go_back_label.setTextColor("white")

    mylabel=Text(Point(26,3),"Clicked Color:")
    mylabel.setStyle("bold")
    mylabel.draw(win)
    myrectangle=Rectangle(Point(29,2),Point(31,4))
    myrectangle.draw(win)

    pixel_per_second =10
    refresh_sec = 0.05
    gameState = 0 # 0 for initial mode, 1 for start mode, 2 for pause mode
    total_score = 0 #general varible to get total score after 100 * 1/bonus
    car_list = []
    clicked_colors = {}     #dictionary 
    start_time1 = 0
    start_time2 = 0
    while True:
        
        pClick = win.checkMouse()       #checks where each mouse click is 
        if gameState == 0: #initial
            time.sleep(0.1)
            if pClick != None:
                if isClicked(pClick, button):
                    gameState = 1           #change gamestate to start phase
                    bottom_message.setText("Click a moving car or Pause to stop")
                    label.setText("Pause")

        elif gameState == 1: # start
            if pClick != None:
                if isClicked(pClick, button):
                    #for #...
                    exit_bg.draw(win)
                    exit_message.draw(win)
                    confirm_button.draw(win)        #Draw up the pause menu and then change gamestate to 2, stopping all movement
                    confirm_label.draw(win)
                    go_back_button.draw(win)
                    go_back_label.draw(win)
                    gameState = 2
                    
                    
                else:
                    for car in car_list:
                        if isClicked(pClick,car.body):
                            total_score += int(100 * (1/ car.getScore()))
                            score_message.setText(total_score)                  #Else statement to delete the cars when they are clicked on
                            myrectangle.setFill(car.getColor())
                            clicked_colors[car.getColor()] = clicked_colors.get(car.getColor(),0) + 1 #used as a method to incrememnt when new and concurrent dictionary keys are spotted
                            clicked_colors_message.setText(str(clicked_colors).replace("}","").replace(":","").replace("{","").replace("'","")) #Prints out the dictionary and uses replace functions to remove the unnecesary portions
                            car.undraw()
                            car_list.remove(car)
                
            
            #...
            
            # if the gen time lag is greater than 1, then generate a new car
            # and reset timer for car generation
            current_time = time.time()
            if (current_time - start_time1) >= 0.2:
                x = (random.random() - 0.5 + 4) - 2
                y = random.uniform(7,23)
                unit = random.random() * 0.6 + 0.4             #obtaining general random values for x,y, and unit within their respective domains according to the assignment requirements
                car = Car(win,x,y,unit)
                car_list.append(car)            #car production center(ASK TA IF ITS SUPPOSED TO SPAWN AT THE LOCATION IT IS SPAWNING AND NOT THE VERY LEFT)
                # car.drawCar(win)                ### (ask TA or professor if it is okay to change the drawCar() method to take out the p1,p2,and p3 values that were originally in it)
                start_time1 = current_time + 1
            # if moving time lag is greater than refesh,
            # set proportional distance to the lag. Then check whether car goes outside window
            if current_time - start_time2 >= refresh_sec:
                for car in car_list:
                    car.move(pixel_per_second * refresh_sec)
                
                    if car.body.getP1().getX() >= 40:   #car destruction center basically when the left end of the car passes the border, it gets first undrawn and then removed from the list 
                        car.undraw()
                        car_list.remove(car)
                start_time2 = current_time
        elif gameState == 2: # pause
            time.sleep(0.1)
            if pClick != None:
                if isClicked(pClick, confirm_button):
                    break                           #basically clicking exit and shutting down the infinite loop
                            
                elif isClicked(pClick, go_back_button):
                    exit_bg.undraw()
                    exit_message.undraw()           #Clicking resume which undraws the pause menu and changes gamestate back to 1, resuming all movement 
                    confirm_button.undraw()
                    confirm_label.undraw()
                    go_back_button.undraw()
                    go_back_label.undraw()
                    gameState = 1

if __name__ == '__main__':
    main()