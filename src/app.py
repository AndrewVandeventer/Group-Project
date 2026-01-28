# This is the main application file for the inventory management system.
# It will integrate the inventory management and data handling functionalities.
# The application will provide a user interface to interact with the inventory. 
#------------------------------------------------------------------------------------------
from flask import Flask, render_template

app = Flask(__name__)   

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True) 