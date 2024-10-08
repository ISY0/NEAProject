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
Datasetlist = []
with open(r'Downloads\NEANBADATASES.txt', 'r') as f:
    for line in f.readlines(2000000):
        data = [item.strip() for item in line.split(",")]
        Datasetlist.append(data)
def getppg(Playername):
    for x in range(0,20):
        if Datasetlist[x][3] == Playername:
            print(Datasetlist[x][27])

def getseason(Playername):
    if seasonlooper > 0:
        seasonlooper =-1
        result = getseason(Playername)
        print(result)
    else:
        for x in range(0,20):
            if Datasetlist[x][3] == Playername:
                print( Datasetlist[x][1])
    
                    
def getgames(Playername):
    for x in range(0,2000):
        if Datasetlist[x][3] == Playername :
            continue

getseason("Adolph Hoefer")
        


points = (20,21,14,16,21,23,25,28,30,30)
time = (2015,2016,2017,2018,2019,2020,2021,2022,2023,2024)
plt.plot(time,points,marker='x')
plt.xlabel("Year")
plt.ylabel("Points per game")
#plt.show()

