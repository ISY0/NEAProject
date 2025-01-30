from flask import Flask, render_template , request ,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="./templates", static_folder="./static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ukjbdjhtvlnzqsu9tnyi:9L1o8zMjcLcL1p5ouHWlNKLuhebLwi@bwkv4mjzmrnekdcjycl3-postgresql.services.clever-cloud.com:50013/bwkv4mjzmrnekdcjycl3'


db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = "Player"
    playerid = db.Column("playerid",db.Integer,primary_key=True,autoincrement=True)
    Firstname = db.Column("Firstname", db.String)
    Lastname = db.Column("Lastname", db.String)

    def __init__(self,playerid,Firstname, Lastname):
        self.playerid = playerid
        self.Firstname = Firstname
        self.Lastname = Lastname

    seasons = db.relationship('Season', back_populates='player')

    def __repr__(self):
        return f"{self.playerid} , {self.Firstname} , {self.Lastname}"
    
class Season(db.Model):
    __tablename__ = "Season"
    Season = db.Column("Season",db.Integer)
    playerid = db.Column(db.Integer, db.ForeignKey("Player.playerid"))
    Points_per_game = db.Column("Points_per_game",db.Float)
    rebounds = db.Column("Rebounds",db.Float)
    assists = db.Column("assists",db.Float)
    fgper = db.Column("fgper",db.Float)
    percent3p = db.Column("percent3p",db.Float)
    steals = db.Column("steals",db.Float)
    blocks = db.Column("blocks",db.Float)
    TOs = db.Column("TOs",db.Float)
    
    __table_args__ = (
        db.PrimaryKeyConstraint('Season', 'playerid'),
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
    player = db.relationship('Player', back_populates='seasons')

@app.route('/', methods=['POST' , 'GET'])
def index():
    Playernameinput = ""
    if request.method == 'POST':
        Playernameinput = request.form['Playerinput']
        names = Playernameinput.split(" ")
        Firstname , Lastname = names
        newplayer = Player(playerid=3460,Firstname=Firstname,Lastname=Lastname)
        try:
            db.session.add(newplayer)
            db.session.commit()
            return redirect('/')
        except:
            return "Couldnt commit new player to database"
    else:
        Players = Player.query.order_by(Player.playerid.desc()).limit(5).all()

        return render_template('index.html' , Players=Players)
@app.route('/delete/<int:playerid>')
def delete(playerid):
    deleteditem = Player.query.get_or_404(playerid)
    try :
        db.session.delete(deleteditem)
        db.session.commit()
        return redirect('/')
    except:
        return "An error deleting player"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
