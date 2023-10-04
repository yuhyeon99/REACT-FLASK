from flask import Flask

app = Flask(__name__)

@app.route('/users')
def users():
    # users 데이터를 Json 형식으로 반환한다
    return {"members": [{"id":1, "name":"yuhyeon"}, {"id":2,"name":"mango"}]}

if __name__ == "__main__":
    app.run(debug = True)