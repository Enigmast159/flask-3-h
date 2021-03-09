from flask import Flask, render_template, redirect
from forms.defence import DefenceForm
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


def main():
    db_session.global_init('db/mars_explorer.db')
    # app.run()


if __name__ == '__main__':
    main()
    session = db_session.create_session()
    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = 15
    jobs.collaborators = '2, 3'
    jobs.start_date = datetime.datetime.now()
    jobs.is_finished = False
    session.add(jobs)
    session.commit()