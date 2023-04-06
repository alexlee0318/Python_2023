# 웹서버 만들기- templates폴더 내 html파일 연결
# (*약속: 폴더생성할 때 이름끝에 s 붙이기 - templates)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')    # http://localhost:5000/
def hello():
    return '''
        <h1>Hello world!!!</h1>
        <hr>
        <p> 디버그 모드에서는 변경 사항이 발생하면 자동적으로 서버가 재실행됩니다.</p>
    '''
@app.route('/chart')
def chart():
    return render_template('chart.html')   # templates 폴더> chart.html 파일

@app.route('/clock')
def clock():
    return render_template('clock.html')   # templates 폴더 > clock.html 파일


if __name__ == '__main__':
    app.run(debug=True)
