from flask import Flask, render_template, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:')
db =

@app.route('/')
def main():
   return render_template("main.html")

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
