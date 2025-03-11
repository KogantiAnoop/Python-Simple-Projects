"""HW4 Fall 2021-2022, template. PLEASE FILL IN "#..." with your code"""

from graphics import *
from time import *
import random

#given top and lower left corner, draw the tires and car body
def draw_car(win,p1,p2):
    carlist1=[]
    tire_left= Circle(Point(p1.x+abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
    tire_left.setFill("black")
    tire_left.draw(win)
    carlist1.append(tire_left)
    tire_right = Circle(Point(p2.x-abs(p2.x - p1.x)/4, p1.y),abs(p2.x - p1.x)/8) #builds the 2nd tire by finding the width using p2.x - p1.x
    tire_right.setFill("black")
    tire_right.draw(win)
    carlist1.append(tire_right)
    body = Rectangle(Point(p1.x,p1.y),Point(p2.x,p2.y)) #Builds the body using the two points clicked
    body.setFill("blue")
    body.draw(win)
    carlist1.append(body)
    return carlist1

def draw_vehicle_roof(win, p1, p2, p3, cartype):
    carlist=[]
    dist = abs(p2.x -p1.x)
    if(cartype == 1): #Assuming 1 is a car, draws the car roof 
        roof = Polygon(Point(p1.x + dist/4,p2.y),Point(p2.x - abs(p2.x-p1.x)/4,p2.y),Point(p2.x - 3  * dist/8,p3.y), Point(p1.x + 3 * dist/8,p3.y)) #Finds values for points using width (abs(p2 - p1))
        roof.setFill("red")
        roof.draw(win)
        carlist.append(roof)
    elif(cartype == 2): #assuming 2 is a truck, draws the truck roof
        roof = Rectangle(Point(p1.x + dist/2, p2.y),Point(p2.x,p3.y)) #finds points to create the roof of a truck starting from hte middle to the far right
        roof.setFill("orange")
        roof.draw(win)
        carlist.append(roof)
    elif(cartype == 3): #ASsuming 3 is a cybertruck, draws the cybertruck roof
        
        roof = Polygon(Point(p1.x,p1.y + (dist) * 0.2),Point(p1.x +(dist*3) / 4, p1.y + dist * 0.3),Point(p2.x,p1.y + (dist* 0.2))) #builds the shape of the cyber trucks top which is a triangle 
        roof.setFill("grey")
        roof.draw(win)
        carlist.append(roof)
        window = Polygon(Point(p1.x + dist / 4 ,p1.y + ( dist * 0.2)),Point(p1.x +(dist *3) / 4, p1.y + (dist * 0.3) - (dist * 0.3 * 0.1)),Point(p2.x - dist/10,p1.y + (dist * 0.2) )) #builds the window of the cybertruck which starts at a point in the front and end somewhere between the middle and end of the truck(chose a point precisely between the two)
        window.setFill("black")
        window.draw(win)
        carlist.append(window)
    return carlist


def draw_truck(win,p1,p2,cartype):  #Added cartype parameter to give the option of either designing a cyber truck or a regular truck
    buslist=[]
    # buslist.extend(draw_car(win,p1,p2))
    # body1 = buslist.pop()
    # body1.setFill("yellow")           Does not work due to multiple objects. Can be fixed by popping out the objects and renaming maybe but too risky id assume
    # body1.draw(win)
    # buslist.append(body1)
    if cartype == 2: #To make the standard truck design provided by the requirements (location of both points clicked to make the body)
        tire_left1= Circle(Point(p1.x+abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
        tire_left1.setFill("black")
        tire_left1.draw(win)
        buslist.append(tire_left1)
        tire_right1 = Circle(Point(p2.x-abs(p2.x - p1.x)/4, p1.y),abs(p2.x - p1.x)/8) #builds the 2nd tire by finding the width using p2.x - p1.x
        tire_right1.setFill("black")
        tire_right1.draw(win)
        buslist.append(tire_right1)
        body1 = Rectangle(Point(p1.x,p1.y),Point(p2.x,p2.y)) #Builds the body using the two points clicked
        body1.setFill("yellow")
        body1.draw(win)
    elif cartype == 3:          #For cybertruck to be its typical color grey and only account for the distance and avoid height for the second point
        p2y = p1.y + (abs(p2.x - p1.x) * 0.2)
        
        # body1 = Rectangle(Point(p1.x,p1.y),Point(p2.x, p2y)) #Builds the body using the two points clicked
        body1 = Rectangle(Point(p1.x,p1.y),Point(p2.x, p2y))
        body1.setFill("grey")
        body1.draw(win)
        tire_left1= Circle(Point(p1.x+abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
        tire_left1.setFill("black")
        tire_left1.draw(win)
        buslist.append(tire_left1)
        tire_right1 = Circle(Point(p2.x-abs(p2.x - p1.x)/6, p1.y),abs(p2.x - p1.x)/8) #builds the 2nd tire by finding the width using p2.x - p1.x and pushing it a bit forward as seen in cyber truck designs
        tire_right1.setFill("black")
        tire_right1.draw(win)
        buslist.append(tire_right1)
        # draw_vehicle_roof(win,p1,p2,Point(0,0),3)
    
    buslist.append(body1)

    return buslist


def draw_buildings(win, p1_x,p1_y,p2_x,p2_y,color):
    shape=Rectangle(Point(p1_x,p1_y),Point(p2_x,p2_y))
    shape.setFill(color)
    shape.draw(win)

def createButtons(label, win, anchor, width, height,): #Set a label to design different button for cybertruck vs reg truck
    button_list = [ ]
    # label = ["Day", "Night", "Speed-Up", "Exit"]

    for i in range(len(label)):
        anchor1 = anchor.clone()
        anchor2 = anchor.clone()
        anchor2.move(width, height)
        newbutton = Rectangle(anchor1, anchor2)
        newbutton.setFill("gray")
        newbutton.draw(win)
        anchor1.move(width/2, height/2)
        newlabel = Text(anchor1, label[i])
        newlabel.setStyle("bold")
        newlabel.setTextColor("white")
        newlabel.draw(win)
        if len(label) <= 2:             #Used to set a random special newlabel to use create buttons for the specified button options.
            newlabel_special=newlabel
        elif i == 2 and len(label)> 2:
            newlabel_special = newlabel
        button_list.append(newbutton)
        anchor.move(width+1, 0)
            
        
        
    return button_list, newlabel_special    
            
        
            

    

def isHitBtn(pclick, btn):
    bp = btn.getP1()
    tp = btn.getP2()
    if bp.x <= pclick.x <= tp.x and bp.y <= pclick.y <= tp.y: #Obtain the 2 points from the rectangle button and then use those points x and y values and determine whether the point clicked is between them, then use that to determine true or false
        return True
    return False

def main():
    win = GraphWin("City View!", 800, 600)
    win.setCoords(0, 0, 40, 30)

    bg = Rectangle(Point(0,15), Point(40, 30))
    bg.setFill("light blue")
    bg.draw(win)

    ground = Rectangle(Point(0,6) , Point(40, 14))
    ground.setFill("light grey")
    ground.draw(win)
    temp=4

    # dash1 = Rectangle(Point(4,10),Point(8,10))
    # dash1.setOutline("white")
    # dash1.setWidth(5)
    # dash1.draw(win)

    # dash2 = dash1.clone()              #These dash objects are used to draw the dashes on the road using clone() and move(dx,dy) in graphics library
    # dash2.move(10,0)
    # dash2.draw(win)

    # dash3 = dash2.clone()
    # dash3.move(10,0)
    # dash3.draw(win)

    # dash4 = dash3.clone()
    # dash4.move(10,0)
    # dash4.draw(win)

    
    while temp<40: 
        gnd_lines = Rectangle(Point(temp,10),Point(temp + 4, 10))
        temp = temp + 4
        gnd_lines.setOutline("white")
        gnd_lines.setWidth(5)       #Used to create dash objects by making the original dash object and then cloning it and then moving the clone so that seperate identities are created
        gnd_lines.draw(win)
        gnd_lines.clone().move(6,0)
        temp = temp + 6

    sun = Circle(Point(37,27), 2)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(win)

    moon = sun.clone()
    moon.setFill("white")           #Drawing the moon
    moon.setOutline("white")
    # moon.draw(win)
    moonPhase = Circle(Point(37.75, 28), 1.5)
    moonPhase.setFill("navy")           #drawing the part to make a crescent moon
    moonPhase.setOutline("navy")
    # moonPhase.draw(win)
    with open('hw4_input.txt','r') as file:
     # reading each line in the file
        for line in file:
            parts = line.split()
            draw_buildings(win,parts[0],parts[1],parts[2],parts[3],parts[4])
        file.close()

    txtMsg1 = Text(Point(20, 29), "Sunny Day")
    txtMsg1.setStyle("bold")
    txtMsg1.setTextColor("orange")
    txtMsg1.draw(win)

    # === set text for asking user to click a point ===
    pntMsg = Point(20, 5)
    txtMsg = Text(pntMsg, "Please click the left bottom point of the car body.")
    txtMsg.setStyle("bold")
    txtMsg.setTextColor("red")
    txtMsg.draw(win)
    # === get the point from mouse ===
    p1 = win.getMouse()
    txtMsg.setText("Now click the upper right point of the car body.") #Obtaining the second point of the body of the car by changing the text
    p2 = win.getMouse()
    e1=draw_car(win, p1, p2)
    # === change the text to ask user to click another point ===
    txtMsg.setText("Now click the rooftop point of the car.")
    p3 = win.getMouse()
    e2=draw_vehicle_roof(win, p1, p2, p3, 1)
    txtMsg.setText("Please choose your truck you would like to display.")
    buttons, special_label = createButtons(["Cybertruck", "Truck"],win, Point(2,2), 4, 2)
    while True:
        
        pClick = win.checkMouse()
        if pClick is not None:
            if isHitBtn(pClick, buttons[0]): #CyberTruck
                buttons[0].undraw()                 #Undraw the buttons to clear the canvas (done for both clicks)
                buttons[1].undraw()
                txtMsg.setText("Now click the lower left location of the cybertruck body.")
                p4 = win.getMouse()
                txtMsg.setText("Now click a distance in front of the car to determine the length of the cybertruck.")        #second click determines size of cybertruck
                p5 = win.getMouse()
                e3 = draw_truck(win,p4,p5,3)                  #Draws the cybertruck due to value 3 in the draw_truck() command being the cybertruck
                txtMsg.undraw()
                e4 = draw_vehicle_roof(win,p4,p5,Point(0,0),3)#Gets the truck roof using the truck value 3 to draw the cyberrtruck roof. Note that the Point 6 value is set as Point(0,0) because there is no need for a third click
                
                break
            if isHitBtn(pClick,buttons[1]):
                buttons[0].undraw()
                buttons[1].undraw()                             
                txtMsg.setText("Now click the lower left point of the truck body.")     #runs the basic truck design process
                p4 = win.getMouse()
                txtMsg.setText("Now click the upper right point of the truck body.")
                p5 = win.getMouse()
                e3 = draw_truck(win,p4,p5,2)                  #Draws the truck
                txtMsg.setText("Now click the roof top point of the truck.")
                p6 = win.getMouse()
                txtMsg.undraw()
                e4 = draw_vehicle_roof(win,p4,p5,p6,2)#Gets the truck roof using the truck value 2 
                
                break
            
            
    
          


     
    
    buttons,special_label = createButtons(["Day", "Night", "Speed-Up", "Exit"],win, Point(2,2), 4, 2)
    
    gameState = 0 # 0 for sunny day, 1 for moon night, 2 for sunny windy day, 3 for moon windy night
    speed = 0.05 #This speed is a variable that you can tune to see differences in speed
    
    while True:
        sleep(0.005) #Moved to 0.005 to better see the cybertruck when its a smaller size
        for part in e3 + e4:
            part.move(speed,0)
        if e3[-1].getP1().x >= 40: #Gets the last object (the rectangle) from the list and use the very back point of it as the implementation to reset the truck to the beginning of the road
            for part in e3 + e4:
                part.move(-40 - abs(e3[-1].getP2().x - e3[-1].getP1().x ),0) #move it down 40 and the width of the truck
        pClick = win.checkMouse()
        if pClick is not None:
            if isHitBtn(pClick, buttons[3]): #Exit
                break

            elif isHitBtn(pClick, buttons[0]): #Day
                if(gameState == 1):
                    gameState = 0
                    moon.undraw()
                    moonPhase.undraw()          #If is night and becomes day, undraw moon and redraw sun and then change sky color
                    sun.draw(win)
                    bg.setFill("light blue")
                elif(gameState == 3):
                    speed = .3
                    gameState = 2
                    moon.undraw()               #if is night at medium speed and becomes day, undraw moon and redraw sun and change sky color and increase speed to .3
                    moonPhase.undraw()
                    sun.draw(win)
                    bg.setFill("light blue")
                    



            elif isHitBtn(pClick, buttons[1]): #Night
                if(gameState == 0):
                    gameState = 1
                    sun.undraw()
                    moon.draw(win)              #if is day and becomes night, undraw sun and draw moon and change skye color
                    moonPhase.draw(win)
                    bg.setFill("navy")
                elif(gameState == 2):
                    speed = 0.15
                    gameState = 3
                    sun.undraw()                #if is day at fast speed and becomes night, change speed to 0.15, undraw sun and draw moon and change sky color making the speed medium speed
                    moon.draw(win)
                    moonPhase.draw(win)
                    bg.setFill("navy")
                    

            elif isHitBtn(pClick, buttons[2]): #speed-up/slow down
                # if special_label.getText() == "Speed-Up":
                #     special_label.setText("Slow-Down")
                # else:
                #     special_label.getText() == "Speed-Up"
                if(gameState == 0):
                    gameState = 2                       #if is day and speed is clicked to speed up, change label to slow down and make car go fast
                    speed = .3
                    special_label.setText("Slow-Down")
                elif(gameState == 1):
                    gameState = 3                       #if is night and speed up is clicked, change label to slow down and make car go medium speed 
                    speed = 0.15
                    special_label.setText("Slow-Down")
                elif(gameState == 2):
                    gameState = 0                       #if is day and slow down is clicked, change label to speed up and make car go slow (0.05)
                    speed = 0.05
                    special_label.setText("Speed-Up")
                elif(gameState == 3):
                    gameState = 1                       #if is night and slow down is clicked, change label to speed up and make car go slow (0.05)
                    speed = 0.05
                    special_label.setText("Speed-Up")
                

                

            if gameState == 0: txtMsg1.setText("Sunny Day")
            elif gameState == 1: txtMsg1.setText("Moon Night")
            elif gameState == 2: txtMsg1.setText("Sunny Day, High Speed")
            elif gameState == 3: txtMsg1.setText("Moon Night, Medium Speed")

    
    win.close()

if __name__ == '__main__':
    main()
    

