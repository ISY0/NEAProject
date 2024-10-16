
import numpy as np
from scipy.spatial import Delaunay
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String , Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt
import sqlite3
#reading the file for the dataset
Base = declarative_base()
f = open(r'C:\Users\sises\OneDrive\Documents\Isaac\NEANBADATASES1.txt', 'r')
Dataset = f.read() # setting the dataset to a variable
Datasetlist = []
with open(r'C:\Users\sises\OneDrive\Documents\Isaac\NEANBADATASES1.txt', 'r') as f:
    for line in f.readlines():
        data = [item.strip() for item in line.split(",")]
        Datasetlist.append(data)
def getseasonsplayed(Playername):
    visitedyears = []
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) not in visitedyears:
            visitedyears.append(int(Datasetlist[x][1]))
    return visitedyears
def getnames():
    players = []
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] not in players:
            players.append(Datasetlist[x][3])
    return players
def getppg(Playername,year):
    gamectr = 0 
    pointctr = 0 
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            pointctr += int(Datasetlist[x][27])
            gamectr += 1
    try:
        pointspergame = pointctr/gamectr
    except ZeroDivisionError:
        print("No games played")
    else:
        return round(pointspergame,2) 

        
def getrebpg(Playername,year):
    gamectr = 0 
    rebctr = 0 
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            rebctr += int(Datasetlist[x][21])
            gamectr += 1
    try:
        rebspergame = rebctr/gamectr
    except ZeroDivisionError:
        print("No games played")
    else:
        return round(rebspergame,2) 

def getastpg(Playername,year):
    gamectr = 0 
    astctr = 0 
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            astctr += int(Datasetlist[x][22])
            gamectr += 1
    try:
        astspergame = astctr/gamectr
    except ZeroDivisionError:
        print("No games played")
    else:
        return round(astspergame,2) 
    
def getfgpercent(Playername,year):
    fgactr = 0 
    fgmctr = 0 
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][11] == "" or Datasetlist[x][10] == "":
                pass
            else:
                fgactr += int(Datasetlist[x][11])
                fgmctr += int(Datasetlist[x][10])
    try:
        fgapercent = (fgmctr / fgactr) * 100
    except ZeroDivisionError:
        print("No games played")
    else:
        return round(fgapercent,2) 

def get3ppercent(Playername,year):
    fg3actr = 0 
    fg3mctr = 0 
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][13] == "" or Datasetlist[x][14] == "":
                pass
            else:
                fg3actr += int(Datasetlist[x][14])
                fg3mctr += int(Datasetlist[x][13])
    try:
        fg3percent = (fg3mctr / fg3actr) * 100
    except ZeroDivisionError:
        print("No games played")
    else:
        return round(fg3percent,2) 
def getsteals(Playername,year):
    stealactr = 0 
    gamectr = 0 
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][23] == "" :
                pass
            else:
                stealactr += int(Datasetlist[x][23])
                
                gamectr += 1 
    try:
        stealpergame = (stealactr/ gamectr) 
    except ZeroDivisionError:
        print("No games played")
    else:
        return round(stealpergame,2) 
    
def getblocks(Playername,year):
    blockctr = 0 
    gamectr = 0 
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][24] == "" :
                pass
            else:
                blockctr += int(Datasetlist[x][24])
                
                gamectr += 1 
    try:
        blockspergame = (blockctr/ gamectr) 
    except ZeroDivisionError:
        print("No games played")
    else:
        return round(blockspergame,2) 
def getTOs(Playername,year):
    TOsctr = 0 
    gamectr = 0 
    for x in range(0,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][25] == "" :
                pass
            else:
                TOsctr += int(Datasetlist[x][25])
                gamectr += 1 
    try:
        TOspergame = (TOsctr / gamectr) 
    except ZeroDivisionError:
        print("No games played")
    else:
        return round(TOspergame,2) 

def getboxscore(Playername):
    seasonlist = getseasonsplayed(Playername)
    boxscorelist = [] 
    for x in seasonlist:  
        points = getppg(Playername,x)
        rebs = getrebpg(Playername,x)
        asts = getastpg(Playername,x)
        fgper = getfgpercent(Playername,x)
        percent3p = get3ppercent(Playername,x)
        steals = getsteals(Playername,x)
        blocks = getblocks(Playername,x)
        TOs = getTOs(Playername,x)
        year = x
        boxscorelist.append([points,rebs,asts,fgper,percent3p,steals,blocks,TOs,year])
    return boxscorelist

print(getnames())

""""
class Player(Base):
    __tablename__ = "Player"
    playerid = Column("playerid",Integer,primary_key=True)
    Firstname = Column("Firstname", String)
    Lastname = Column("Lastname", String)

    def __init__(self,playerid,Firstname, Lastname):
        self.playerid = playerid
        self.Firstname = Firstname
        self.Lastname = Lastname
    def __repr__(self):
        return f("{self.playerid} , {self.Firstname} , {self.Lastname}")
class Season(Base):
    __tablename__ = "Season"
    Season = Column("Season",Integer,primary_key=True)
    playerid = Column(Integer, ForeignKey("Player.playerid"),primary_key=True)
    Points_per_game = Column("Points_per_game",Float)
    def __init__(self,Season,playerid,Points_per_game):
        self.Season = Season
        self.playerid = playerid
        self.Points_per_game = Points_per_game

engine = create_engine("sqlite:///mydb.db",echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

LeBronJames = Player(0,"LeBron","James")
LebronJames2016 = Season(2016,0,26)
LebronJames2015 = Season(2015,0,23)
session.add(LeBronJames)
session.add(LebronJames2016)
session.add(LebronJames2015)
session.commit()
"""

points = (20,21,14,16,21,23,25,28,30,30)
time = (2015,2016,2017,2018,2019,2020,2021,2022,2023,2024)
plt.plot(time,points,marker='x')
plt.xlabel("Year")
plt.ylabel("Points per game")
#plt.show()
