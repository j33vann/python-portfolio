from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/<string:pageName>')
def htmlPage(pageName):
    return render_template(pageName)

def database(data):
  with open('database.txt', mode='a') as db:  
    email= data['email']
    subject= data['subject']
    message= data['message']
    db.write(f'\n{email}, {subject}, {message}')

def databasecsv(data):
    with open('database.csv', mode='a') as databasecsv:
        email= data['email']
        subject= data['subject']
        message= data['message']
        dbwriter = csv.writer(databasecsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        dbwriter.writerow([email, subject, message])

@app.route('/submitForm', methods=['POST', 'GET'])
def submitForm():
    if request.method == 'POST':
        data = request.form.to_dict()
        database(data)
        databasecsv(data)
        return redirect('/thankyou.html')
    else:
        print('someth9inig went wrong')

