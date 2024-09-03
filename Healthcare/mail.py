from flask import Flask, render_template, request, jsonify, redirect, session, flash, url_for
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functools import wraps
from flask_mail import Mail, Message
import random
import pickle
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/healthcare'  # MySQL database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Harhu2003'
db = SQLAlchemy(app)


# Define SQLAlchemy models for each table
class DiabetesData(db.Model):
    __tablename__ = 'diseasereport'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    # Add other necessary columns

class HeartDiseaseData(db.Model):
    __tablename__ = 'heart_disease_data'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    # Add other necessary columns

class ParkinsonsData(db.Model):
    __tablename__ = 'parkinsons_data'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    # Add other necessary columns


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String(10))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)



# Define a function to get the currently logged-in user (if any)
def get_current_user():
    if 'user_id' in session:
        user_id = session['user_id']
        return User.query.get(user_id)
    return None 

# Define a custom decorator to check if the user is logged in
def login_required(route_function):
    def wrapper(*args, **kwargs):
        if 'user_id' in session:
            return route_function(*args, **kwargs)
        else:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
    return wrapper

@app.route('/')
def home():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user:
            return render_template('index.html', username=user.username)
    
    return render_template('index.html')


### functions for email verification


# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'ps4759158@gmail.com'  # your email
app.config['MAIL_PASSWORD'] = 'opkwamfdedpgvsab'  # your email password (or app password)

mail = Mail(app)

# Generate random OTP
def generate_otp():
    return str(random.randint(1000, 9999))

email_to_otp_map = {}

sampleEmail = []

@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/send-otp', methods=['POST'])
def send_otp():
    email = request.form.get('email')
    otp = generate_otp()

    msg = Message('OTP Verification', sender='your-email@gmail.com', recipients=[email])
    msg.body = f'Your OTP for registration is: {otp}'

    try:
        mail.send(msg)
        email_to_otp_map[email] = otp
        sampleEmail.append(email)
        return 'OTP sent successfully.'
    except Exception as e:
        print(e)
        return 'Error occurred while sending OTP.'

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    email = request.form.get('email')
    entered_otp = request.form.get('otp')
    stored_otp = email_to_otp_map.get(email)

    if stored_otp and entered_otp == stored_otp:
        # OTP is correct, set a session variable to indicate successful verification
        session['otp_verified'] = True
        return redirect('/register')
    else:
        return 'Invalid OTP. Please try again.'


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if the user has successfully verified the OTP
    if not session.get('otp_verified'):
        flash('Please verify your email with the OTP first.', 'danger')
        return redirect('/verify')
    

    # Assuming sampleEmail is a variable passed to the template
    if sampleEmail and sampleEmail[0] is not None:
        Dmail = sampleEmail[0]
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = sampleEmail[0]
            phone_number = request.form['phone_number']
            birthdate = request.form['birthdate']
            gender = request.form['gender']
            username = request.form['username']
            password = request.form['password']

            existing_user = User.query.filter_by(username=username).first()

            if existing_user:
                flash('Username already exists. Please choose another one.', 'danger')
            else:
                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    birthdate=birthdate,
                    gender=gender,
                    username=username,
                    password=password
                )
                db.session.add(new_user)
                db.session.commit()
                flash('Registration successful. You can now log in.', 'success')
                
                # Clear the session to prevent flash messages from persisting
                session.pop('_flashes', None)

                return redirect(url_for('login'))

        return render_template('register.html')
    else:
        flash('Invalid email. Please provide a valid email.', 'danger')
        return redirect('/verify')  # Redirect to the verification page if email is not valid


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['user_id'] = user.id
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


@login_required
@app.route('/update-profile', methods=['POST'])
def update_profile():
    current_user = get_current_user()
    if current_user:
        # Access the data sent from the front-end
        updated_username = request.json.get('username')
        updated_email = request.json.get('email')
        updated_firstName = request.json.get('first_name')
        updated_lastName = request.json.get('last_name')
        updated_phoneNumber = request.json.get('phone_number')
        updated_birthdate = request.json.get('birthdate')
        updated_gender = request.json.get('gender')
        updated_password = request.json.get('password')  # Note: Handle password securely

        # Update the user details in the database
        current_user.username = updated_username
        current_user.email = updated_email
        current_user.first_name = updated_firstName
        current_user.last_name = updated_lastName
        current_user.phone_number = updated_phoneNumber
        current_user.birthdate = updated_birthdate
        current_user.gender = updated_gender
        # Update more fields as needed

        # Commit changes to the database
        db.session.commit()

        # Return a success message or updated user details
        return jsonify({
            'message': 'Profile updated successfully',
            'user': {
                'username': current_user.username,
                'email': current_user.email,
                'first_name': current_user.first_name,
                'last_name': current_user.last_name,
                'phone_number': current_user.phone_number,
                'birthdate': current_user.birthdate,
                'gender': current_user.gender
                # Add more fields as needed
            }
        })
    else:
        return jsonify({'message': 'User not logged in'})


@login_required
@app.route('/profile')
def profile():
    current_user = get_current_user()  # Assuming this function retrieves the current user
    if current_user:
        # Fetch disease reports for the current user
        diabetes_reports = DiabetesData.query.all()
        heart_disease_reports = HeartDiseaseData.query.all()
        parkinsons_reports = ParkinsonsData.query.all()
        return render_template('profile.html', user=current_user, 
                               diabetes_reports=diabetes_reports,
                               heart_disease_reports=heart_disease_reports,
                               parkinsons_reports=parkinsons_reports)
    else:
        flash('Please log in to view your profile.', 'warning')
        return redirect(url_for('login'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/check-username', methods=['POST'])
def check_username():
    username = request.json.get('username')

    # Perform a check in your database to see if the username is already taken
    # Replace the following with your actual logic to check username availability
    is_available = not User.query.filter_by(username=username).first()

    return jsonify({'available': is_available})
    
@app.route('/check-username-react', methods=['POST'])
def check_username_react():
    username = request.json.get('username')

    # Perform a check in your database to see if the username is already taken
    # Replace the following with your actual logic to check username availability
    is_available = not User.query.filter_by(username=username).first()

    return jsonify({'available': is_available})
    

# #############################################################################################################################################



# Function to connect to the database
def connect_to_db():
    conn = mysql.connector.connect(host='localhost', user='root', password='', database='healthcare')
    return conn

# Function to generate diabetes response
def generate_response_diabetes(urination, thirst, weight_loss, hunger, fatigue, vision, tingling, sores, infections, family_history, age):
    response = "Type of Diabetes: [type of diabetes]\nRisk of Future Diabetes: [risk of future diabetes]\nReaction Emoji: [reaction emoji]"
    return response

# Flask route to render the HTML template
@app.route('/diabetes')
@login_required
def index():
    return render_template('diabetes.html')

# Flask route to handle form submission
@app.route('/submit-diabetes-data', methods=['POST'])
def submit_diabetes_data():
    # Connect to the database
    conn = connect_to_db()
    cursor = conn.cursor()

    # Extract data from the form submission
    urination = request.form['urination']
    thirst = request.form['thirst']
    weight_loss = request.form['weightLoss']
    hunger = request.form['hunger']
    fatigue = request.form['fatigue']
    vision = request.form['vision']
    tingling = request.form['tingling']
    sores = request.form['sores']
    infections = request.form['infections']
    family_history = request.form['familyHistory']
    age = request.form['age']

    # Call the function to generate the response
    response = generate_response_diabetes(urination, thirst, weight_loss, hunger, fatigue, vision, tingling, sores, infections, family_history, age)

    # Insert data into the database
    sql = "INSERT INTO diseasereport (urination, thirst, weight_loss, hunger, fatigue, vision, tingling, sores, infections, family_history, age, response) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (urination, thirst, weight_loss, hunger, fatigue, vision, tingling, sores, infections, family_history, age, response)
    cursor.execute(sql, values)
    conn.commit()

    # Close database connection
    cursor.close()
    conn.close()

    # Return a response
    return jsonify({'success': True, 'message': 'Data stored successfully'})



@app.route('/heart_disease')
# @login_required
def heart_disease():
    return render_template('heart_disease.html')

@app.route('/parkinsons')
# @login_required
def parkinsons():
    return render_template('parkinsons.html')

if __name__ == '__main__':
    app.run(debug=True)
