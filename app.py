import os
from flask import Flask, jsonify,redirect, url_for,request
app = Flask(__name__)

@app.route('/')
def hello():
    abhi = "<html><body><form action = " "http://localhost:5000/register"" method = ""post""><p>Enter Name:</p><p><input type = ""text"" name = ""nm"" /></p><p><input type = ""submit"" value = ""submit"" /></p></form></body></html>"
    return abhi

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/register',methods = ['POST', 'GET'])
def login():
   uid=1
   path="/mnt/"
   comm="mkdir " + path + str(uid)
   os.system(comm)
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      usjer = request.args.get('nm')
      return redirect(url_for('success',name = user))



if __name__== "__main__":
    app.run(debug=True) 