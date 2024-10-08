""""then create a interface to display data that can produce a graph and predict future trends
implementing sorts particularly a merge sort to order the statistic by number
binary search for players when using search bar 
tree for sorting names in alphabetical order 
class season with relationships to class player through team and 
analysis between use of database and classes to store data for 
potentially heat maps 
update tools for updating dataset
One player has multiple of instances of sesason class and one instance of stasts for sesason
python library for visualtions for heat maps for basektball 
timelines of a single player 
adding getname() function to the code 
working on relationships between classes"""
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import sqlite3
#reading the file for the dataset
f = open(r'Downloads\NEANBADATASES.txt', 'r')
Dataset = f.read() # setting the dataset to a variable

def getnames(start,end):
    logofcounter = 0
    isName = True
    words = ''
    processednames = []
    for counter in range(start,end):
    #searching through dataset for names by searching forte letrs
    #making sure the letters found are not part of a game fixture and are strictly only names
        if Dataset[counter].isupper() == True and Dataset[counter+1].isupper() == True and Dataset[counter+2].isupper() == True:
            isName = False
            logofcounter = counter
        if logofcounter + 9 == counter: # skipping over the letters where it is a game fixture 
            isName = True
        if Dataset[counter].isalpha() == True and isName == True:
            words = words + Dataset[counter]
            if Dataset[counter+1] == " " :
                words = words + " "
            if Dataset[counter+1] == ",":
                if words not in processednames:
                    print(words)  # Print the name
                    processednames.append(words)
                words = ""
    

class Season():
    def __init__(self):
        self.Seasonlist = []
        for x in range(1980,2020):
            self.Seasonlist = self.Seasonlist.append[x]
    #needs a method that produces each season a person played over time one by one(in a list)
class stats():
    def __init__(self,playername):
        self.playername = playername
def getaname(Playername):
    #create a function that finds each instance of a nmame and outputs the index
def getseason(Playername):
    indexofname = Dataset.find(Playername)
    commacounter = 0
    ctr = 2
    for x in range(0,40):
        if Dataset[indexofname-x] == "," and commacounter != ctr:
            commacounter += 1 
        if commacounter == ctr:
            indexofseason = x
            commacounter = 3
    season = Dataset[indexofname-indexofseason-4:indexofname -indexofseason]
    return season


                
def getppg(PlayerName):
        #needs to be looped over every game a person plays in a season using getseason()function
        season = getseason(PlayerName)
        for 
        ctr = 23
        commacounter = 0
        indexofname = Dataset.find(PlayerName)
        for x in range(0,100):
            if Dataset[indexofname+x] == "," and commacounter != ctr:
                commacounter += 1
            elif commacounter == ctr:
                indexofpoints = x
        if Dataset[indexofname+indexofpoints].isnumeric() == True and Dataset[indexofname+indexofpoints+2].isnumeric == True:
            points = Dataset[indexofname+indexofpoints:indexofname+indexofpoints+2] # need to make sure all outputs are numbers because some points are of different lengths
        else:
            points = Dataset[indexofname+indexofpoints]
        return points
                
class Player():
    def __init__(self,first,second):
        self.FirstName = first
        self.SecondName = second

getseason("Adolph Hoefer")
getppg("LeBron James")
f.close()


#def getppg(self,PlayerName):
        #needs to be looped over every game a person plays in a season 
       #ctr = 23
        #commacounter = 0
       # indexofname = Dataset.find(PlayerName)
        #for x in range(0,100):
            #if Dataset[indexofname+x] == "," and commacounter != ctr:
                #commacounter += 1
            ##elif commacounter == ctr:
                #indexofpoints = x
        #self.points = Dataset[indexofname+indexofpoints:indexofname+indexofpoints+2]
       #print(self.points)
                
points = (20,21,14,16,21,23,25,28,30,30)
time = (2015,2016,2017,2018,2019,2020,2021,2022,2023,2024)
plt.plot(time,points,marker='x')
plt.xlabel("Year")
plt.ylabel("Points per game")
plt.show()



"play"