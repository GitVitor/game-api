# Game API  

This project contains a simple Read-only API writen in Python with Flask.
The main goal of this project is to develop a Back For Front API with routes that provide resources related to Steam`s games.

The dataset used in this project was Downloaded from Kaggle.

## Package managament - Poetry

This project use Poetry as Package manager to control the repository's dependencies. Poetry generate a lock file that ensure the exact same version of each dependency will be installed everywhere.

## Database - MongoDB Atlas

This project connect to MongoDB database to consume. (Don't try to find credentials on this project :P)

## Environment variables

File [Config](./game_api/infra/config.py) contais all required environment variables. 


## Run local

To run project locally use the command: `poetry run flask --app game_api run`

### Debug

To debug with vscode you must connect your vscode to currently poetry virtual environment. To do it, you must manually specify the interpreter. 

