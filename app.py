from flask import Flask, render_template
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:')
db =

@app.route('/apply')
def main():
   return render_template("post.html")

@app.route('/mypage')
def main():
   return render_template("mypage.html")

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)