import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if int(competition['numberOfPlaces']) > 0:
        if placesRequired <= 12:
            if int(club['points']) >= placesRequired:
                if placesRequired <= int(competition['numberOfPlaces']) and int(competition['numberOfPlaces']) > 0:
                    if placesRequired > 0:
                        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
                        club['points'] = int(club['points']) - placesRequired
                        flash('Great-booking complete!')
                    else:
                        flash('Sorry! select a number of places between 0 and 12')
                else:
                    flash('Sorry there is not enough places for your order')
            else:
                flash("sorry! you don't have enough points to make this order")
        else:
            flash('To ensure parity of places for each club, you may not order more than 12 places')
    else:
        flash('sorry! there are no more places available for this tournament')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
@app.route('/clubPoints', methods=['GET'])
def clubPoints():
    return render_template('points.html', clubs=clubs, competitions=competitions)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


# remote add oc 