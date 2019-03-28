How to start
============

- ``$ . setup.env`` Sets environment variables
- ``$ make`` Sets up VE
- ``$ . ve/bin/activate`` Source the VE
- ``$ docker-compose up --build -d`` Build the images
- Check ``localhost 5000``
- Upload ``test_input.csv``
- Query ``http://localhost:5000/api`` or check ``http://localhost:5000/api/people/1`` to see the input.

Now to migrate, follow this syntax.

- ``docker exec <container-name/id of app> python3 manage.py db migrate <command>``

Run these 3 commands:

- ``python3 manage.py db init``
- ``python3 manage.py db migrate``
- ``python3 manage.py db upgrade``

Insert test data locally.

- ``docker exec <container-name/id of app> bash``
- ``$ cd flask_rest_psql_docker/database``
- ``$ python3 insert_to_psql.py`` (Make sure your host machine's psql is off.)

Docker
============

Useful Docker commands:

- http://blog.baudson.de/blog/stop-and-remove-all-docker-containers-and-images

Check ENVVARS

- ``docker exec -ti <image_id>  env | sort``

CHECK HOSTS

- ``docker exec -ti <image_id> cat "/etc/hosts"``

Kill all containers

- ``docker stop $(docker ps -aq)``

PSQL
============

https://www.youtube.com/watch?v=aHbE3pTyG-Q

``docker exec -it <image_id> psql testdb -U postgres test``

psql commands:

- ``\dt`` Show relations
- ``\l`` List of databases
- ` ``\q`` Quit

Extensions
============

- flask-script/flask-migrate : for DB migrations
- flask-restplus : swagger/api
- flask-marshmallow : serialization (needs marshmallow-sqlalchemy)
- flask-sqlalchemy : db/ORM (needs psycopg2 for psql)

ToDo:
============
Circle CI
WSGI
Cookiecutter functionality?
Unit testing?