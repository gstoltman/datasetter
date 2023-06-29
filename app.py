from flask import Flask, render_template, request, url_for, flash, redirect, Response
import pandas as pd
from main import generate_data, category_dict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=(['GET', 'POST']))
def process_form():
    category1 = request.form['category1']
    category2 = request.form['category2']
    category3 = request.form['category3']
    category4 = request.form['category4']

    category_list = [category1, category2, category3, category4]
    row_count = int(request.form['row_count'])

    global list_of_lists 
    list_of_lists = [[category_dict[category1], 
                      category_dict[category2], 
                      category_dict[category3], 
                      category_dict[category4]]]
    for row in range(row_count):
        generated_data = generate_data(category_list)
        list_of_lists.append(generated_data)

    return render_template('index.html', matrix=list_of_lists)
    return redirect(url_for('index'))

@app.route('/export', methods=['POST'])
def export_csv():
    # Sample data to export
    df = pd.DataFrame(list_of_lists)

    # Create a response object with CSV content
    response = Response(df.to_csv(index=False), mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    return response


if __name__ == '__main__':
    app.run()