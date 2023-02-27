-yay!
-Notes!

Resource: a path, ex- /movies
    hard to define because it's a thing
    a subject or an entity that your app controls or manages or is in some way responsible for
    Amazon has:
    - registries, lists
    - orders
    - user accounts
    - products
    - deliveries
    - movies, streaming stuff

Database:

Schema
    * Table (like excell)
        - rows, tuple, record
        - columns, fields, attributes
        - unique ID: primary key

install sqlite3
run apt install sqlite3 and it should work
list of commands
- sqlite3 name_of_file.db --create the file/database
- .schema -- print out all of the schema
- CREATE TABLE movies (id INTEGER PRIMARY KEY, name TEXT, rating INTEGER, genre TEXT);
- INSERT INTO movies (name, rating, genre) VALUES ("Avatar", 7, "Action");
- SELECT * FROM movies;
- SELECT rating, name FROM movies;
