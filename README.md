# Clone repository on desktop
Open console and run:

    git clone https://github.com/kirillsev1/SecondPartAtom_hard

# HOW INSTALL
    sudo apt-get update

    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# How run
Fill the .env file with your data

To run docker, run three commands in a terminal:

    docker volume create --name=grafana_data
    docker-compose build
    docker-compose up

# Project containers
Project has three docker containers: graphql, postgres, grafana
## graphql

Python container which makes request on GraphQL service
and receives data in json format form. 

Example of data:

    query = {
    launches {
        mission_name
        rocket {
          rocket_name
          rocket_type
        }
        launch_date_local
      }
    }

Then this data writes into database

## postgres
postgres database container which stores saved data received from a GraphQL 
service. It contains three tables: rockets, missions, launches with 
relevant information for each table

Example table(rockets):

 id |     name     |  type  
----|--------------|--------
  1 | Falcon 1     | rocket
  2 | Falcon 9     | rocket
  3 | Falcon Heavy | rocket

## grafana
Grafana is data visualization software system. 
The project is used to visualize the data mart

To run grafana on device:

    Go to localhost:3000

    Fill the field user with admin

    Fill the feild password with admin

    Then creating password could be passed

    Find icon with four squares

    Then chouse "Bowse"

    Open Data in folder General

## .env
### postgres
    DATABASE - name of database
    DB_USER - database user
    DB_PASSWORD - user password
    DB_PORT - database port
