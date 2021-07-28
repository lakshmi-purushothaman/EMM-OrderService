# Orders Service

## Prerequisites

### Install Docker
This service is packaged to run with all dependencies installed within a Docker container. The docker image is based on Python 3.9 and install Docker following commands (as instructed by the [Docker Install](https://docs.docker.com/get-docker/))

## Running the App
To run open a shell
```bash
$ docker-compose build -d
```

## App Testing
This will open the docker shell and you can run one of the following commands:

Run the entire test suite
```bash
$ docker-compose run orderserviceapp sh
$ pytest 
```
To exit the shell
``bash
$ exit
```
## API Usage
To browse through the API's exposed use [API Doc](http://localhost:5000/)
