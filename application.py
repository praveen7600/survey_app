

import os
import re
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_mail import Mail, Message
from flask_session import Session
from tempfile import mkdtemp
from functools import wraps
from datetime import datetime

from priges import All, boys, girls, subjects
#from helpers import contestants, voters, voters_data


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



app.config["MAIL_DEFAULT_SENDER"] = "a4surveya4@gmail.com"
app.config["MAIL_PASSWORD"] = "hlkgefxfkvspcfbd"
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "a4surveya4"
mail = Mail(app)



db = SQL("sqlite:///survey.db")
not_voted = []
for name in db.execute("Select name from StudentD where SSNo in (Select SSNo from CompD where Completion = 0)"):
    not_voted.append(name['name'])


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=["GET", "POST"])
def index():
    session.clear()

    if request.method == "POST":
        print("in index post before", session)
        #print(request)
        voter_name = request.form.get("voter_name")
        print(voter_name)
        if voter_name not in All:
            return render_template("error.html", error_msg="No name in voters list")

        not_voted = []
        for name in db.execute("Select name from StudentD where SSNo in (Select SSNo from CompD where Completion = 0)"):
            not_voted.append(name['name'])

        if voter_name not in not_voted:
            session["user_id"] = voter_name
            time = str(datetime.now())
            #print(time)
            ssno=db.execute("select SSno from StudentD where name=?", session["user_id"])[0]['SSNo']
            db.execute("INSERT INTO logind (ssno, name, logintime) VALUES (?, ?, ?)", ssno, session["user_id"], time)

            return redirect("/result")

        else:
            #mail
            print("sending to", voter_name)
            body= "HI " + str(voter_name) + ",\n Your password is " + db.execute("select password from StudentD where name=?", voter_name)[0]['password'] +".\nDon't forget to vote."
            msg = Message(subject="A4 Class Survey",body=body, recipients=[db.execute("select mailID from StudentD where name=?",voter_name)[0]['mailID']])
            mail.send(msg)
            print("sent to", voter_name)
            session["temp_id"]= voter_name
            print("in index post after", session)
            return redirect("/verify")

    else:

        return render_template("index.html", voters=All, n = len(All))

@app.route("/verify", methods=["GET", "POST"])
def verify():


        if request.method == "POST":
            print("in verify post", session)
            try:
                session["temp_id"]
            except:
                return redirect("/")
            if session["temp_id"] not in not_voted:
                return redirect("/result")

            PW = request.form.get("pw")
            session["user_id"] = session["temp_id"]

            #print(PW, session["user_id"])
            if session["user_id"] not in All:
                session.clear()
                return render_template("error.html", error_msg="close this tab. TRY AGAIN")

            if PW != db.execute("select password from StudentD where name=?", session["user_id"])[0]['password']:
                session.clear()
                return render_template("error.html", error_msg="Wrong Password")



            time = str(datetime.now())
            #print(time)
            ssno=db.execute("select SSno from StudentD where name=?", session["user_id"])[0]['SSNo']
            db.execute("INSERT INTO logind (ssno, name, logintime) VALUES (?, ?, ?)", ssno, session["user_id"], time)
            #return redirect("/q6OnSub")
            return redirect("/q1enter")

        else:
            #session.clear()
            return render_template("verify.html")


@app.route("/q1enter", methods=["GET", "POST"])
@login_required
def q1enter():


    if session["user_id"] not in not_voted:
            return redirect("/result")

    if request.method == "POST":
        #return redirect("/result")
        voter_name = session["user_id"]
        voted_for = request.form.getlist("voted_for")
        #print(voted_for, "abab")

        if voter_name not in not_voted:
            return render_template("error.html", error_msg="You've already voted.")

        if len(voted_for) != 3:
            return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        for name in voted_for:
            if name not in All:
                return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        time = str(datetime.now())
        ssno=db.execute("select SSno from StudentD where name=?",voter_name)[0]['SSNo']
        if not db.execute("select q11 from rawsurveydata where ssno=?",ssno)[0]['Q11']:
            db.execute("UPDATE RawSurveyData set q11=?, q12=?, q13=? WHERE SSNO=?", voted_for[0], voted_for[1], voted_for[2],ssno)



            for name in voted_for:
                rank_data = db.execute("SELECT name FROM entertainer")
                #print(data)
                if name in [x['name'] for x in rank_data]:
                    db.execute("UPDATE entertainer SET count = count+1 WHERE name = ?", name)
                else:
                    db.execute("INSERT INTO entertainer (name, count) VALUES (?, ?)", name, 1)


        return redirect("/q2BoyRep")

    else:
        #print(session)
        #return redirect("/result")
        return render_template("q1enter.html", c=All, n= len(All))



@app.route("/q2BoyRep", methods=["GET", "POST"])
@login_required
def q2BoyRep():


    if session["user_id"] not in not_voted:
            return redirect("/result")

    if request.method == "POST":
        #return redirect("/result")
        voter_name = session["user_id"]
        voted_for = request.form.getlist("voted_for")
        #print(voted_for, "abab")

        if voter_name not in not_voted:
            return render_template("error.html", error_msg="You've already voted.")

        if len(voted_for) != 3:
            return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        for name in voted_for:
            if name not in All:
                return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        ssno=db.execute("select SSno from StudentD where name=?",voter_name)[0]['SSNo']
        if not db.execute("select q21 from rawsurveydata where ssno=?",ssno)[0]['Q21']:
            db.execute("UPDATE RawSurveyData set q21=?, q22=?, q23=? WHERE SSNO=?", voted_for[0], voted_for[1], voted_for[2],ssno)



            for name in voted_for:
                rank_data = db.execute("SELECT name FROM dreamRep_B")
                #print(data)
                if name in [x['name'] for x in rank_data]:
                    db.execute("UPDATE dreamRep_B SET count = count+1 WHERE name = ?", name)
                else:
                    db.execute("INSERT INTO dreamRep_B (name, count) VALUES (?, ?)", name, 1)


        return redirect("/q3GirlRep")

    else:
        #print(session)
        #return redirect("/result")
        return render_template("q2BoyRep.html", c=boys, n= len(boys))

@app.route("/q3GirlRep", methods=["GET", "POST"])
@login_required
def q3GirlRep():


    if session["user_id"] not in not_voted:
            return redirect("/result")

    if request.method == "POST":
        #return redirect("/result")
        voter_name = session["user_id"]
        voted_for = request.form.getlist("voted_for")
        #print(voted_for, "abab")

        if voter_name not in not_voted:
            return render_template("error.html", error_msg="You've already voted.")

        if len(voted_for) != 3:
            return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        for name in voted_for:
            if name not in All:
                return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        ssno=db.execute("select SSno from StudentD where name=?",voter_name)[0]['SSNo']
        if not db.execute("select q31 from rawsurveydata where ssno=?",ssno)[0]['Q31']:
            db.execute("UPDATE RawSurveyData set q31=?, q32=?, q33=? WHERE SSNO=?", voted_for[0], voted_for[1], voted_for[2],ssno)



            for name in voted_for:
                rank_data = db.execute("SELECT name FROM dreamRep_G")
                #print(data)
                if name in [x['name'] for x in rank_data]:
                    db.execute("UPDATE dreamRep_G SET count = count+1 WHERE name = ?", name)
                else:
                    db.execute("INSERT INTO dreamRep_G (name, count) VALUES (?, ?)", name, 1)


        return redirect("/q4Seminar")

    else:
        #print(session)
        #return redirect("/result")
        return render_template("q3GirlRep.html", c=girls, n= len(girls))




@app.route("/q4Seminar", methods=["GET", "POST"])
@login_required
def q4Seminar():


    if session["user_id"] not in not_voted:
            return redirect("/result")

    if request.method == "POST":
        #return redirect("/result")
        voter_name = session["user_id"]
        voted_for = request.form.getlist("voted_for")
        #print(voted_for, "abab")

        if voter_name not in not_voted:
            return render_template("error.html", error_msg="You've already voted.")

        if len(voted_for) != 3:
            return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        for name in voted_for:
            if name not in All:
                return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        ssno=db.execute("select SSno from StudentD where name=?",voter_name)[0]['SSNo']
        if not db.execute("select q41 from rawsurveydata where ssno=?",ssno)[0]['Q41']:
            db.execute("UPDATE RawSurveyData set q41=?, q42=?, q43=? WHERE SSNO=?", voted_for[0], voted_for[1], voted_for[2],ssno)



            for name in voted_for:
                rank_data = db.execute("SELECT name FROM seminare")
                #print(data)
                if name in [x['name'] for x in rank_data]:
                    db.execute("UPDATE seminare SET count = count+1 WHERE name = ?", name)
                else:
                    db.execute("INSERT INTO seminare (name, count) VALUES (?, ?)", name, 1)


        return redirect("/q5mcq")

    else:
        #print(session)
        #return redirect("/result")
        return render_template("q4Seminar.html", c=All, n= len(All))


@app.route("/q5mcq", methods=["GET", "POST"])
@login_required
def q5mcq():


    if session["user_id"] not in not_voted:
            return redirect("/result")

    if request.method == "POST":
        voter_name = session["user_id"]
        voted_for = request.form.getlist("voted_for")
        #print(voted_for, "abab")

        if voter_name not in not_voted:
            return render_template("error.html", error_msg="You've already voted.")

        if len(voted_for) != 1:
            return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        ssno=db.execute("select SSno from StudentD where name=?",voter_name)[0]['SSNo']
        db.execute("INSERT INTO mcq1 values (?, ?)",ssno, voted_for[0])

        db.execute("UPDATE gatecls SET count = count+1 WHERE val = ?", voted_for[0])


        return redirect("/q6OnSub")

    else:
        #print(session)
        #return redirect("/result")
        return render_template("q5mcq.html")



@app.route("/q6OnSub", methods=["GET", "POST"])
@login_required
def q6OnSub():


    if session["user_id"] not in not_voted:
            return redirect("/result")

    if request.method == "POST":
        #return redirect("/result")
        voter_name = session["user_id"]
        voted_for = request.form.getlist("voted_for")
        #print(voted_for, "abab")
        print(voted_for)
        if voter_name not in not_voted:
            return render_template("error.html", error_msg="You've already voted.")

        if len(voted_for) != 1:
            return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        for name in voted_for:
            if name not in subjects:
                return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

        ssno=db.execute("select SSno from StudentD where name=?",voter_name)[0]['SSNo']
        db.execute("UPDATE RawSurveyData set q6=? WHERE SSNO=?", voted_for[0], ssno)

        db.execute("UPDATE onlinesub SET count = count+1 WHERE name = ?", voted_for[0])
        db.execute("UPDATE COMPD set completion=1 where ssno= ?", ssno)

        #mail
        print("sending to", voter_name)
        body= "HELLO " + str(voter_name) + ",\nYou've successfully voted.\nThank you from \n\t\t-ArunBalaji \n\t\t-AnthonyPriges \n\t\t-Praveen"
        msg = Message(subject="A4 CLASS SURVEY",body=body, recipients=[db.execute("select mailID from StudentD where name=?",voter_name)[0]['mailID']])
        mail.send(msg)
        print("sent to", voter_name)



        return redirect("/result")

    else:
        #print(session)
        #return redirect("/result")
        return render_template("q6OnSub.html", c=subjects, n= len(subjects))




# @app.route("/votepage", methods=["GET", "POST"])
# @login_required
# def votepage():


#     if session["user_id"] not in not_voted:
#             return redirect("/result")

#     if request.method == "POST":
#         #return redirect("/result")
#         voter_name = session["user_id"]
#         voted_for = request.form.getlist("voted_for")
#         #print(voted_for, "abab")

#         if db.execute("SELECT * FROM votes WHERE name=?", voter_name):
#             return render_template("error.html", error_msg="You've already voted.")

#         if len(voted_for) != 3:
#             return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

#         for name in voted_for:
#             if name not in contestants:
#                 return render_template("error.html", error_msg="Close the tab. TRY AGAIN cheater.")

#         time = str(datetime.now())

#         db.execute("INSERT INTO votes (name, v1, v2, v3, datetime) VALUES (?, ?, ?, ?, ?)", voter_name, voted_for[0], voted_for[1], voted_for[2], time)

#         for name in voted_for:
#             rank_data = db.execute("SELECT name FROM rank")
#             #print(data)
#             if name in [x['name'] for x in rank_data]:
#                 db.execute("UPDATE rank SET votes = votes+1 WHERE name = ?", name)
#             else:
#                 db.execute("INSERT INTO rank (name, votes) VALUES (?, ?)", name, 1)

#         #mail
#         print("sending to", voter_name)
#         body= "HELLO " + str(voter_name) + ",\nYou've successfully voted."
#         msg = Message(subject="2nd Yr REP ELECTION",body=body, recipients=[voters_data[voter_name]["mail"]])
#         mail.send(msg)
#         print("sent to", voter_name)

#         return redirect("/result")

#     else:
#         #print(session)
#         #return redirect("/result")
#         return render_template("votepage.html", c=contestants, n= len(contestants))


@app.route("/result", methods=["GET", "POST"])
@login_required
def result():

    show_results = False
    session.clear()

    if show_results:
        q1 = db.execute("select name,count from entertainer order by count desc")[:5]
        q2 = db.execute("select name,count from dreamRep_B order by count desc")[:3]
        q3 = db.execute("select name,count from dreamRep_G order by count desc")[:3]
        q4 = db.execute("select name,count from seminare order by count desc")[:5]
        q5 = db.execute("select val,count from gatecls order by count desc")
        q6 = db.execute("select name,count from onlinesub order by count desc")

        #print(q1,q2,q3,q4,q6,sep="\n")


 #       return render_template("result.html", ent=q1)
        return render_template("result.html", ent=q1, rb=q2, rg=q3, sem=q4, gcls=q5, sub=q6)

    else:
        return render_template("preresult.html")

