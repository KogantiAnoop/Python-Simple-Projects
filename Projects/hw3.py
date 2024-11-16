import matplotlib.pyplot as plt
from matplotlib_venn import venn3

def main():
    CE = 0
    civE = 0
    ME = 0
    EE = 0
    other= 0

    #variables for the Venn Diagram to seperate
    CE1, ME1, EE1 = 0, 0, 0
    CEME,CEEE, MEEE = 0, 0, 0
    CEEEME = 0

    Civ2, EE2, ME2 = 0,0,0
    CivEE2, CivME2, EEME2 = 0,0,0
    CivEEME = 0
    
    Civ3, CE3, EE3 = 0,0,0
    CivCE3, CivEE3, CEEE3 = 0,0,0
    CivCEEE = 0
    
    yes = True
    while yes == True: #allows for a loop to continue when a file that is asked to be located cant be located. Turns to False when found and cancels the while statement
        file1 = input("Please enter the file name and include .txt!: ")
        fname = file1[:len(file1)-4] #used for future part to name the output file
        try:
            with open(file1, 'r') as file: #reads the file named
                l = file.readlines()  #returns each line in the file as a list
                yes = False
        except:
            print("can't find the input file.") #incase nothing found

    for k in l:
        cut = k.strip().split(" ; ")[1:] #basically splitting apart a double list to get the single list(1 line) so that it can cut apart to get the different parts with the nested loop
        #Following is for the ven diagram to determine the literals values to put per each 3 way point in it
        isCE = "Computer Engineering" in cut
        isEE = "Electrical Engineering" in cut
        isME = "Mechanical Engineering" in cut
        iscivE = "Civil Engineering" in cut
        for part in cut:

            if "Computer Engineering" in part: #Following portion to just ultimately get the amount of each major with if else to viabley obtain the other majors category with a nested for loop
                CE = 1 +CE 
                
            elif "Electrical Engineering" in part:
                EE = 1 +EE
                
            elif "Civil Engineering" in part:
                civE = 1 +civE
                
            elif "Mechanical Engineering" in part:
                ME = 1 + ME
                
            else:
                other = 1 + other


        #Venn Diagram for CE, EE, ME
        if isCE and not isEE and not isME:
            CE1 += 1
        elif isEE and not isCE and not isME:
            EE1 += 1
        elif isME and not isCE and not isEE: #Basically Pseudocode version of saying that per line, if it has x value and doesnt have this value and doesnt have that value, then add to that point of the venn diagra
            ME1 += 1                         #Same throughout for all three graphs, avoiding the use of the values that arent in accordance with the values in the graph(ex: this doesnt implement other or civE)
        elif isCE and isEE and not isME:
            CEEE += 1
        elif isCE and isME and not isEE:
            CEME += 1
        elif isME and isEE and not isCE:
            MEEE += 1
        elif isCE and isEE and isME:
            CEEEME += 1

        #Venn Diagram for Civil, EE, ME
        if iscivE and not isEE and not isME:
            Civ2 += 1
        elif isEE and not iscivE and not isME:
            EE2 += 1
        elif isME and not iscivE and not isEE:
            ME2 += 1
        elif iscivE and isME and not isEE:
            CivME2 += 1
        elif iscivE and isEE and not isME:
            CivEE2 += 1
        elif isEE and isME and not iscivE:
            EEME2 += 1
        elif iscivE and isEE and isME:
            CivEEME += 1

        #Venn Diagram for Civil, CE, EE
        if isCE and not iscivE and not isEE:
            CE3 += 1
        elif iscivE and not isCE and not isEE:
            Civ3 += 1
        elif isEE and not iscivE and not isCE:
            EE3 += 1
        elif isEE and iscivE and not isCE:
            CivEE3 += 1
        elif isEE and isCE and not iscivE:
            CEEE3 += 1
        elif iscivE and isCE and not isEE:
            CivCE3 += 1
        elif isCE and iscivE and isEE:
            CivCEEE += 1
    
    #print("Civil Engineering:", 1)
    #print("Computer Engineering:", 2)
    #print("Electrical Engineering:", 3)   For my reference
    #print("Mechanical Engineering:", 4)
    #print("Other Majors:", 0)
    
    with open(fname + "_output.txt", "w") as out: #form the output file and name and write it with "w"
        for k in l: # same idea as before
            name = str(k.strip().split(" ; ")[:1]).strip("['").strip("']")           
            maj = k.strip().split(" ; ")[1:]
        
            for num in maj:
                if "Computer Engineering" in num: # using f string to concatonate list parts properly with a string value
                    name = f"{name} 2"
                
                elif "Electrical Engineering" in num:
                    name = f"{name} 3"
                
                elif "Civil Engineering" in num: #if in statement as an alternate to javas .contains() to find if that is located in the portion of the list
                    name = f"{name} 1"
                
                elif "Mechanical Engineering" in num:
                    name = f"{name} 4"
                
                else:
                    name = f"{name} 0"
            out.write(f"{name}\n") #adds together to make the full file output list of people
        out.write(f"The number of Civil Engineering students: {civE}\n")
        out.write(f"The number of Computer Engineering students: {CE}\n") #output required by prompt
        out.write(f"The number of Electrical Engineering students: {EE}\n")
        out.write(f"The number of Mechanical Engineering students: {ME}\n")
        #out.write(f"Other Majors: {other}\n")
    
    cat = ["Civil Engineering", "Computer Engineering", "Electrical Engineering", "Mechanical Engineering", "Other"] # #seperating the values of x and y as well as colors of each graph
    val = [civE, CE, EE, ME, other]
    colors = ["cyan", "blue", "purple", "red", "green"]
    plt.bar(cat,val,color = colors) #connecting the values x y and color together to make the bar graph with matplotlib
    plt.xlabel("Student Majors")
    plt.ylabel("No. of Students Enrolled") #visual requirements (x,y, title)
    plt.title("Enrolled Student Information")
    for i in range(len(cat)): #to set up the numbers above each graph to get the specific values
        plt.text(i,val[i],val[i],ha = "center", va = "bottom")

    
    #plotting the first VD (CE, EE, ME)
    plt.figure()
    venn3(subsets=(CE1, EE1, CEEE, ME1, CEME, MEEE, CEEEME), set_labels=("Computer Engineering", "Electrical Engineering", "Mechanical Engineering"))#placing values in correct locations according to documentation to obtain proper graph in equivalence to the assignment pictures
    plt.title("Overlap between Civil, Electrical, and Mechanical Engineering")
    
    #plotting the 2nd venn diagram 
    plt.figure()
    venn3(subsets=(Civ2, EE2, CivEE2, ME2, CivME2, EEME2, CivEEME), set_labels=("Civil Engineering", "Electrical Engineering", "Mechanical Engineering"))
    plt.title("Overlap between Civil, Electrical, and Mechanical Engineering")

    #plotting the 3rd venn diagram
    plt.figure()
    venn3(subsets=(Civ3, CE3, CivCE3, EE3, CivEE3, CEEE3, CivCEEE),set_labels=("Civil Engineering", "Computer Engineering", "Electrical Engineering")) 
    plt.title("Overlap between Civil, Computer, and Electrical Engineering")
    plt.show()
    
main()
