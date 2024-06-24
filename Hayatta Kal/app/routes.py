
from app.models import User
from app import app ,db
from flask import  render_template ,request,redirect,url_for,flash
from app.forms import Registration


@app.route('/')
def home():
    users=User.query.all()
    return render_template("compla.html",users=users)


@app.route('/register', methods=['GET','POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        user = User(username=form.username.data , complaint=form.complaint.data , age=form.age.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Complaint created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('complaint_form.html',title='Register ', form=form)
