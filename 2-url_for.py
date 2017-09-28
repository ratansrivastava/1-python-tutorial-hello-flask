from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin/')
def hello_admin():
  return "Hello admin"
  
 @app.route('/guest/<guest>')
 def hello_guest():
  return "Hello %s " %guest
  
if __name__ == '__main()__':
  app.run(host="0.0.0.0",port=80,debug=True)
