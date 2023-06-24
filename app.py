from flask import Flask, request

app= Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"

@app.route("/op")
def hello_world2():
    pass
@app.route("/test/test")
def test2():
    data1 = int(request.args.get('x'))
    data2 = int(request.args.get('y'))
    data3 = data1+data2
    return "the sum is  {}".format(data3)

if __name__=="__main__":
    app.run(host="0.0.0.0")

