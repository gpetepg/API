"""For db migrations"""

from flask_rest_psql_docker import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


manager = Manager(create_app(config='development'))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
