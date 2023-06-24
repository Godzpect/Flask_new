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
    data = request.args.get('x')
    return "this is a data from input {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")

