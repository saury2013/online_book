from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from app import create_app,db

app = create_app()



manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # manager.run()
    # db.create_all(app=app)
    app.run(debug=True)