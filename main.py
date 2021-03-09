from flask import Flask, render_template, redirect
from forms.defence import DefenceForm
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/jobs')
def jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('jobs.html', title='Jobs', arr=jobs)


def main():
    db_session.global_init('db/mars_explorer.db')
    app.run()


if __name__ == '__main__':
    main()