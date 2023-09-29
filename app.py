from flask import Flask
from datetime import date
from datetime import datetime
 

app = Flask(__name__)

 

@app.route('/')
def show_current_date():
    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return f"Сьогоднішня дата: {current_date}"

 

if __name__ == '__main__':
    app.run()