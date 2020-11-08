from flask import render_template
import config

# Create the application instance
connex_app = config.connex_app

connex_app.add_api("openapi.yml") 

# Create a URL route in our application for "/"
@connex_app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template("home.html")

# If we're running in stand alone mode, run the application
if __name__ == "__main__":
    connex_app.run(port="5001",debug=True)