How to start
============

- ``$ . setup.env``
- ``$ make``
- ``$ docker-compose up --build -d``
- ``$ cd flask_rest_psql_docker/database``
- ``$ python3 insert_to_psql.py`` (Make sure your host machine's psql is off.)
- Check ``localhost 5000``

Docker
============

Docker commands:
- http://blog.baudson.de/blog/stop-and-remove-all-docker-containers-and-images 

You can also set envvar is the docker-compose file like so.

    environment:
          - POSTGRES_USER=${POSTGRES_USER}
          - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
          - POSTGRES_DB=${POSTGRES_DB}

Check ENVVARS

``docker exec -ti <image_id>  env | sort``

CHECK HOSTS

``docker exec -ti <image_id> cat "/etc/hosts"``

Kill all containers

``docker stop $(docker ps -aq)``

PSQL
============

https://www.youtube.com/watch?v=aHbE3pTyG-Q

``docker exec -it <image_id> psql -U postgres``

Curl

``docker-compose exec app curl postgres:5432``






