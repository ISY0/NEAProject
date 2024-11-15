import numpy as np
from scipy.spatial import Delaunay
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String , Float , PrimaryKeyConstraint 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , relationship
import matplotlib.pyplot as plt
import sqlite3
import matplotlib.ticker as mtick
Base = declarative_base()
f = open(r'C:\Users\sises\OneDrive\Documents\Isaac\sampledataset.txt', 'r')
Dataset = f.read()   
Datasetlist = []
with open(r'C:\Users\sises\OneDrive\Documents\Isaac\sampledataset.txt', 'r') as f:
    for line in f.readlines():
        data = [item.strip() for item in line.split(",")]
        Datasetlist.append(data)
#the years for the season will be stored as the first year e.g 1980-1981 will be stored as 1980
def convertyeartoseason():
    for x in range(1,len(Datasetlist)):
        Month = Datasetlist[x][5]
        year = Datasetlist[x][1]
        if Month.find("JAN") != -1 or Month.find("FEB") != -1 or Month.find("MAR") != -1 or Month.find("APR") != -1 or Month.find("MAY") != -1:
            Datasetlist[x][1] == int(year)-1
            Datasetlist[x][5] == Month + "THE YEAR HAS BEEN ALTERED"
        else:
            pass

def getseasonsplayed(Playername):
    visitedyears = []
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) not in visitedyears:
            visitedyears.append(int(Datasetlist[x][1]))
    return visitedyears
def getteam(Playername,year):
    team = []
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            team.append(Datasetlist[x][4])
    return team[0]
            
def getnames():
    players = []
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] not in players:
            players.append(Datasetlist[x][3])
    return players
def getppg(Playername,year):
    gamectr = 0 
    pointctr = 0 
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            pointctr += int(Datasetlist[x][27])
            gamectr += 1
    try:
        pointspergame = pointctr/gamectr
    except ZeroDivisionError:
        pass
    else:
        return round(pointspergame,2)       
def getrebpg(Playername,year):
    gamectr = 0 
    rebctr = 0 
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][21] == "" :
                pass
            else:
                rebctr += int(Datasetlist[x][21])
                gamectr += 1
    try:
        rebspergame = rebctr/gamectr
    except ZeroDivisionError:
        pass
    else:
        return round(rebspergame,2) 
def getastpg(Playername,year):
    gamectr = 0 
    astctr = 0 
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][22] == "" :
                pass
            else:
                astctr += int(Datasetlist[x][22])
                gamectr += 1
    try:
        astspergame = astctr/gamectr
    except ZeroDivisionError:
        pass
    else:
        return round(astspergame,2)     
def getfgpercent(Playername,year):

    fgactr = 0 
    fgmctr = 0 
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][11] == "" or Datasetlist[x][10] == "":
                pass
            else:
                fgactr += int(Datasetlist[x][11])
                fgmctr += int(Datasetlist[x][10])
    try:
        fgapercent = (fgmctr / fgactr) * 100
    except ZeroDivisionError:
        pass
    else:
        return round(fgapercent,2) 
def get3ppercent(Playername,year):
    fg3actr = 0 
    fg3mctr = 0 
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][13] == "" or Datasetlist[x][14] == "":
                pass
            else:
                fg3actr += int(Datasetlist[x][14])
                fg3mctr += int(Datasetlist[x][13])
    try:
        fg3percent = (fg3mctr / fg3actr) * 100
    except ZeroDivisionError:
        pass
    else:
        return round(fg3percent,2) 
def getsteals(Playername,year):
    stealactr = 0 
    gamectr = 0 
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][23] == "" :
                pass
            else:
                stealactr += int(Datasetlist[x][23])
                
                gamectr += 1 
    try:
        stealpergame = (stealactr/ gamectr) 
    except ZeroDivisionError:
        pass
    else:
        return round(stealpergame,2)   
def getblocks(Playername,year):
    blockctr = 0 
    gamectr = 0 
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][24] == "" :
                pass
            else:
                blockctr += int(Datasetlist[x][24])
                
                gamectr += 1 
    try:
        blockspergame = (blockctr/ gamectr) 
    except ZeroDivisionError:
        pass
    else:
        return round(blockspergame,2) 
def getTOs(Playername,year):
    TOsctr = 0 
    gamectr = 0 
    for x in range(1,len(Datasetlist)):
        if Datasetlist[x][3] == Playername and int(Datasetlist[x][1]) == year:
            if Datasetlist[x][25] == "" :
                pass
            else:
                TOsctr += int(Datasetlist[x][25])
                gamectr += 1 
    try:
        TOspergame = (TOsctr / gamectr) 
    except ZeroDivisionError:
        pass
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
        team = getteam(Playername,x)
        year = x
        #need to add team
        boxscorelist.append([points,rebs,asts,fgper,percent3p,steals,blocks,TOs,year])
    return boxscorelist

engine = create_engine("sqlite:///mydb.db",echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

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
        return f"{self.playerid} , {self.Firstname} , {self.Lastname}"
    seasons = relationship('Season', back_populates='player')
    def getpointsperyear(self,session,Playerfname,Playersname):
        pointlist = []
        results = session.query(Player,Season).join(Season, Player.playerid == Season.playerid).filter(Player.Firstname==Playerfname, Player.Lastname == Playersname).all()
        for player, season in results:
            pointlist.append([player.Firstname, player.Lastname, season.Points_per_game , season.Season])
        return pointlist
    def getrebs(self,session,Playerfname,Playersname):
        results = session.query(Player,Season).join(Season, Player.playerid == Season.playerid).filter(Player.Firstname==Playerfname, Player.Lastname == Playersname).all()
        for player, season in results:
            print(f"{player.Firstname} {player.Lastname} averaged {season.rebounds} rebounds in {season.Season}")
    def getasts(self,session,Playerfname,Playersname):
        results = session.query(Player,Season).join(Season, Player.playerid == Season.playerid).filter(Player.Firstname==Playerfname, Player.Lastname == Playersname).all()
        for player, season in results:
            print(f"{player.Firstname} {player.Lastname} averaged {season.assists} assists in {season.Season}")
    def getfgper(self,session,Playerfname,Playersname):
        results = session.query(Player,Season).join(Season, Player.playerid == Season.playerid).filter(Player.Firstname==Playerfname, Player.Lastname == Playersname).all()
        for player, season in results:
            print(f"{player.Firstname} {player.Lastname} averaged {season.fgper} FG% in {season.Season}")
    def get3ppercent(self,session,Playerfname,Playersname):
        results = session.query(Player,Season).join(Season, Player.playerid == Season.playerid).filter(Player.Firstname==Playerfname, Player.Lastname == Playersname).all()
        for player, season in results:
            print(f"{player.Firstname} {player.Lastname} averaged {season.percent3p} 3P% in {season.Season}")
    def getsteals(self,session,Playerfname,Playersname):
        results = session.query(Player,Season).join(Season, Player.playerid == Season.playerid).filter(Player.Firstname==Playerfname, Player.Lastname == Playersname).all()
        for player, season in results:
            print(f"{player.Firstname} {player.Lastname} averaged {season.steals} steals in {season.Season}")
    def getblocks(self,session,Playerfname,Playersname):
        results = session.query(Player,Season).join(Season, Player.playerid == Season.playerid).filter(Player.Firstname==Playerfname, Player.Lastname == Playersname).all()
        for player, season in results:
            print(f"{player.Firstname} {player.Lastname} averaged {season.blocks} blocks in {season.Season}")
    def getTOs(self,session,Playerfname,Playersname):
        results = session.query(Player,Season).join(Season, Player.playerid == Season.playerid).filter(Player.Firstname==Playerfname, Player.Lastname == Playersname).all()
        for player, season in results:
            print(f"{player.Firstname} {player.Lastname} averaged {season.TOs} Turnovers in {season.Season}")
    def getseasons(self,session,Playerfname,Playersname):
        seasonlist = []
        results = session.query(Player,Season).join(Season, Player.playerid == Season.playerid).filter(Player.Firstname==Playerfname, Player.Lastname == Playersname).all()
        for player, season in results:
            seasonlist.append(season.Season)
        return seasonlist
    

class Season(Base):
    __tablename__ = "Season"
    Season = Column("Season",Integer)
    playerid = Column(Integer, ForeignKey("Player.playerid"))
    Points_per_game = Column("Points_per_game",Float)
    rebounds = Column("Rebounds",Float)
    assists = Column("assists",Float)
    fgper = Column("fgper",Float)
    percent3p = Column("percent3p",Float)
    steals = Column("steals",Float)
    blocks = Column("blocks",Float)
    TOs = Column("TOs",Float)
    #team = Column("Team",String)

    __table_args__ = (
        PrimaryKeyConstraint('Season', 'playerid'),
    )
    def __init__(self, Season, playerid, Points_per_game, rebounds, assists, fgper, percent3p, steals, blocks, TOs,team):
        self.Season = Season
        self.playerid = playerid
        self.Points_per_game = Points_per_game
        self.rebounds = rebounds
        self.assists = assists
        self.fgper = fgper
        self.percent3p = percent3p
        self.steals = steals
        self.blocks = blocks
        self.TOs = TOs
        self.team = team
    player = relationship('Player', back_populates='seasons')
engine = create_engine("sqlite:///mydb.db",echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

def datainput():
    convertyeartoseason()
    playeridctr = 0 
    namelist = getnames()
    for Playername in namelist:
        first_last = Playername.split(" ")
        if len(first_last)==2:
            pass
        elif len(first_last) ==1:
            first_last.append(" ")
        playeridctr += 1 
        playerinstance = Player(playeridctr,first_last[0],first_last[1])
        session.add(playerinstance)
        session.commit()
        boxscore = getboxscore(Playername)
        seasons = getseasonsplayed(Playername)
        for x in range(len(seasons)):
            seasoninstance = Season(boxscore[x][8],playeridctr,boxscore[x][0],boxscore[x][1],boxscore[x][2],boxscore[x][3],boxscore[x][4],boxscore[x][5],boxscore[x][6],boxscore[x][7],boxscore[x][8])
            session.add(seasoninstance)
        session.commit()

if not session.query(Player).first():
    datainput()

def query(first,last):
    player = session.query(Player).filter_by(Firstname=first, Lastname=last).first()
    session.commit()
    
    points = player.getpointsperyear(session,first,last)
    for x in range(0,len(points)):
        print(points[x])
    player.getasts(session,first,last)

def model(first,last):
    player = session.query(Player).filter_by(Firstname=first, Lastname=last).first()
    points = []
    time = []
    fetchpoints = player.getpointsperyear(session,first,last)
    for x in range(0,len(fetchpoints)):
        points.append(fetchpoints[x][2])
        time.append(fetchpoints[x][3])
    plt.plot(time,points,marker='x',markerfacecolor='blue')
    plt.xlabel("Year")
    plt.ylabel("Points per game")
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    plt.title(f"{first} {last}'s Points Per Game over time ")
    plt.show()

model("Michael","Jordan")

