from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from BloomFilter import BloomFilter
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if request.method == 'POST':
        return render_template('login.html',value='Not found')
    else:
        if not session.get('logged_in'):
            return render_template('login.html',value=None)
        else:
            return str(bf.ProbabilityOfFalsePositives())
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    username = request.form['username']
    print username
    
    if bf.CheckIfInputIsPresent(username):
        #return "Username exists"
        return render_template('login.html',value="Username exists")
    else:
        bf.AddtoBitVector(username)
        return render_template('login.html',value="Username does not exists")
        #return "Username does not exist" 
    print bf.ProbabilityOfFalsePositives()
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
 
if __name__ == "__main__":
    bf = BloomFilter(100, 2)
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
