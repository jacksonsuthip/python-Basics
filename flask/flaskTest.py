from flask import Flask, render_template, request

# object(constructor)
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    # return "Home Page"
    return render_template('home.html')


@app.route('/details', methods=['POST', 'GET'])
def details():
    if request.method == 'POST':
        name = request.form.get('name')
        phno = request.form.get('phno')
        city = request.form.get('city')
        return render_template('details.html', Name=name, Phno=phno, City=city)


# checking current page is main
if __name__ == "__main__":
    app.run(debug=True, port=4000)
