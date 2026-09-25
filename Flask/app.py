from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
    # return render_template('home.html',name="akshit")

@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        print(username)

    return render_template('login.html')
# def about():
#     return "<h1> this is about page <h1/>"

if __name__ == "__main__":
    app.run(debug=True) 