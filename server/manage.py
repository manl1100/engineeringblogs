from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command(
    'runserver', Server(host='0.0.0.0', port='8888', use_debugger=True))


@manager.command
def create_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()
