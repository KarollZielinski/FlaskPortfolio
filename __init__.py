from flask import Flask

# create instance of flask 
app = Flask(__name__)

from portfolio import routes
app.run(debug=False,host='0.0.0.0')

