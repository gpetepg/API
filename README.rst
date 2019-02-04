How to start
============

``. setup.env``
``$ make``

Docker
============

http://blog.baudson.de/blog/stop-and-remove-all-docker-containers-and-images

``docker-compose up --build -d``

You can also set envvar is the docker-compose file like so.

    environment:
          - POSTGRES_USER=${POSTGRES_USER}
          - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
          - POSTGRES_DB=${POSTGRES_DB}

Check ``localhost 5000``

Check ENVVARS

``docker exec -ti <image_id>  env | sort``

CHECK HOSTS

``docker exec -ti <image_id> cat "/etc/hosts"``

PSQL
============

https://www.youtube.com/watch?v=aHbE3pTyG-Q

``docker exec -it <image_id> psql testdb -U testusr``





