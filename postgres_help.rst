================================================
Trouble Shooting PSQL
================================================

Refer to README for useful links and troubleshooting.

Postgresql Installation and Configuration
------------------------------------------------

.. code-block:: console

 brew install postgresql

- Go to the ``postgres.conf`` file located here ``/usr/local/var/postgres/``

.. code-block:: console

 change #listen_addresses = 'localhost'`` to ``listen_addresses = '*'

- Go to the ``pg_hba.conf`` file also located in ``/usr/local/var/postgres/`` and Inject these statements to the IPv4 section.

.. code-block:: console

 host    all             all             172.17.0.0/16         trust
 host    all             all             10.0.0.0/8            trust

- We want to run this next command in another window. The goal is to see if our default port is broadcasting/listening generally from ``port 5432``.

.. code-block:: console

 netstat -n -a -f inet | grep 5432

- We should see a result like such in the terminal:

.. code-block:: console

 tcp4       0      0  *.5432                 *.*                    LISTEN

----

Connect to remote DB
================================================

psql -h <host> -d <db-name> -U <username>

This should prompt your password

Create User
------------------------------------------------

CREATE USER <username> WITH PASSWORD '<password>';

Useful commands for navigating postgresql (psql)
------------------------------------------------
- ``brew services start postgresql`` : To start server
- ``brew services stop postgresq`` : To stop server
- ``\l`` : List all databases
- ``\du`` :  List all users
- ``\q`` : Quit postgresql
- ``create <user> with password 'PASSWD' superuser;`` : Create superuser with a password
- ``create database <databaseName>`` : Create database
- ``drop user <username>;`` : Drop user
- ``drop database <databaseName>;`` : Drop database
- ``postgres -D /usr/local/var/postgres`` : Check postgresql logs