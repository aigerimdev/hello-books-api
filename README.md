# Hello Books API

Wave 03: Connecting the Database, Read and Create Endpoints
Database Setup
Complete the following setup steps of the Solar System API repo:

Activate the virtual environment
Create the database solar_system_development
Every member of the group must create the database on their computer
Setup the Planet model with the attributes id, name, and description, and one additional attribute
Create a migration to add a table for the Planet model and then apply it.
Confirm that the planet table has been created as expected in postgres.
RESTful Endpoints: Create and Read
Create or refactor the following endpoints, with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

...with new valid planet data and get a success response, so that I know the API saved the planet data
...to get all existing planets, so that I can see a list of planets, with their id, name, description, and other data of the planet.