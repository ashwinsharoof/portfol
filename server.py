from flask import Flask, render_template, request
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.csv', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message= data["message"]
        csv_writer = csv.writer(database, newline='', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        print(data)
        write_to_file(data)
        return 'Thank you form submitted'



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)