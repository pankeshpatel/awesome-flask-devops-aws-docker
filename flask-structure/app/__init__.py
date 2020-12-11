# Think of the __init__.py file as a contructor 
# that pulls all of the parts of our application together 
# into a package and then tells Python to treat it as a package!

# We are importing Flask and setting up our app variable
from flask import Flask 
app = Flask(__name__)


# Using this method, we can import multiple
# python files into our Flask Application
from app import views
from app import admin_views