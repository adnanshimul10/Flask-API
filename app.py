### Building url Dynamically
### Variable Rules and URL Building

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my Youtube Channel'

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is  "+ str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is  "+ str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result, score=marks))



if __name__=='__main__':
    app.run(debug=True)
