from flask import Flask, render_template, request, url_for, flash, redirect
# import create_fake_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a7d221fcc7abdc1e3b7442b13bd060e69b70da9309c0b0c2'

@app.route('/')
def index():
    return render_template('index.html')

# START HERE NEXT TIME< GET WEBSITE INTAKE WORKING WITH CREATE FUNCTION

@app.route('/', methods=(['POST']))
def process_form():
    inputs = []
    category1 = request.form['category1']
    category2 = request.form['category2']
    category3 = request.form['category3']
    row_count = int(request.form['row_count'])

    flash([category1, category2, category3, row_count])
    return redirect(url_for('index'))
    return render_template('index.html')