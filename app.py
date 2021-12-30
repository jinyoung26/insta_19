from flask import Flask, render_template # 플라스크
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('main.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

   # 진영님 여기 바뀌었어요 ! 주석 추가
   # 브랜치 : 나만 보기 (형주) 1111