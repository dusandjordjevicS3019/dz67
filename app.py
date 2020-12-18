from flask import Flask, render_template, request, url_for
import mysql.connector

# database init
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dz67"
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'S3019'


@app.route('/')
def index():
    return "Cao svete!"


@app.route('/raspored')
def raspored():
    mc = mydb.cursor()
    mc.execute("SELECT * FROM raspored")
    rezultat = mc.fetchall()
    return render_template("raspored.html", raspored=rezultat)


@app.route('/raspored/<nastavnik>')
def raspored_id(nastavnik):
    mc = mydb.cursor()
    mc.execute("SELECT * FROM raspored WHERE nastavnik='"+nastavnik+"'  ")
    render = mc.fetchall()
    return render_template("nastavnik.html", raspored_id=render)


@app.route('/ucionica/<vreme>')
def ucionica_id(vreme):
    mc = mydb.cursor()
    mc.execute("SELECT * FROM raspored WHERE vreme='"+vreme+"'  ")
    render2 = mc.fetchall()
    return render_template("ucionica.html", ucionica_id=render2)
