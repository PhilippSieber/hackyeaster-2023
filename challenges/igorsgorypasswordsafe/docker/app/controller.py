from flask import Flask, render_template, redirect, url_for, request, flash, send_file, make_response
from flask_login import login_user, logout_user, login_required, LoginManager
import logging.config
from app import app
from users import *
from User import *
from passwords import *

app = Flask(__name__)

# ################
# Welcome page
# ################
@app.route('/')
def main():
    if current_user.is_authenticated:
        return redirect(url_for('show'))
    else:
        return redirect(url_for('login'))
  
# ################
# authentication  
# ################
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    login = request.form.get('login')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = loginUser(login, password)

    # check if user actually exists
    if not user: 
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    userClass = User(user['name'], user['login'], user['role'])
    login_user(userClass, remember=remember)
    return redirect(url_for('show'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    user = getUserByLogin(request.form.get('login'))
    # if this returns a user, then the email already exists in database
    if user:    
        flash('Login  already exists')
        return redirect(url_for('signup'))

    # create new user with the form data
    createUserFromForm(request.form)

    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main'))

# ################
# Passwords
# ################
@app.route('/show')
@login_required
def show():
    passwords = getPasswordsByLoginId()
    return render_template('passwords.html', passwords = passwords)

@app.route('/add')
@login_required
def add():
        return render_template('addPassword.html')
    
@app.route('/add', methods=['POST'])
@login_required
def add_post():
    createPassword(request.form)
    return redirect(url_for('show'))

@app.route('/search', methods=['GET'])
@login_required
def search():
    searchparameter = request.args.get('search')
    passwords = searchPasswordsByLoginId(searchparameter)
    return render_template('passwords.html', passwords = passwords)

@app.route('/get/<id>', methods=['GET'])
@login_required
def getPW(id):
    password = getPWForClipboard(id)
    response = make_response(password, 200)
    response.mimetype = "text/plain"
    return response

@app.route('/update', methods=['GET'])
@login_required
def update():
    password = getPasswordById(request.args.get('id'))
    if password: 
        return render_template('updatePassword.html', password = password)
    else:
        flash("No permission for this password")
        return redirect(url_for('show'))

@app.route('/update', methods=['POST'])
@login_required
def update_post():
    updatePassword(request.form)
    return redirect(url_for('show'))

@app.route('/delete', methods=['GET'])
@login_required
def delete():
    deletePassword(request.args.get('id'))
    return redirect(url_for('show'))

# ################
# favicon
# ################
@app.route('/favicon.ico')
def favicon():
    return send_file("static/favicon.ico")

# ################
# Main  
# ################
if __name__ == "__main__":    
    app.config['SECRET_KEY'] = '83j4K4iuopO9OLWxND4o'
    login_manager = LoginManager()
    login_manager.login_view = 'app.login'
    login_manager.init_app(app)
 
    @login_manager.user_loader
    def load_user(login):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        user = getUserByLogin(login)    
        userClass = User(user['name'], user['id'], user['role'])
        return userClass
   
    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
        ]
    )
    app.logger.info("App is started ...")
    app.run(debug=False, host='0.0.0.0')
