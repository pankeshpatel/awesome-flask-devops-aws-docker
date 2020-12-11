# run.py is an entry point to our Flask App

# We're importing the app variable 
# from the app package that we've just created.

from app import app

if __name__ == "__main__":
    app.run(debug=True)