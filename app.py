from flask import Flask, render_template, abort, request
from forms import LoginForm, SignUpForm

app = Flask(__name__)

pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
        ]
# move to env file
app.config['SECRET_KEY'] = 'kra52wIzSm31YafqtyN4yUTAnai5bDRz'

users = [
            {"id": 1, "full_name": "Pet Rescue Team", "email": "team@pawsrescue.co", "password": "adminpass"},
        ]


@app.route('/home')
def home():
    return render_template("home.html", pets=pets)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/details/<int:pet_id>')
def details(pet_id):
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description=f"The pet with id: {pet_id} not found")
    return render_template("details.html", pet=pet)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login.html", message="Successfully Logged In")
        return render_template("login.html", form=form, message="Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())

    return render_template("login.html", form=form)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = {
            "id": len(users) + 1,
            "full_name": form.full_name.data,
            "email": form.email.data,
            "password": form.password.data
        }
        users.append(new_user)
        return render_template("signup.html", message="Successfully signed up")
    return render_template("signup.html", form=form)
