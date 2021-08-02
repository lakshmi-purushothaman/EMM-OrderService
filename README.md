# Orders Service

## Prerequisites

### Install Docker
This service is packaged to run with all dependencies installed within a Docker container. The docker image is based on Python 3.9 and install Docker following commands (as instructed by the [Docker Install](https://docs.docker.com/get-docker/))

## Running the App
To run open a shell
```bash
$ docker-compose up
```

## App Testing
This will open the docker shell and you can run one of the following commands:

Run the entire test suite
```bash
$ docker-compose run orderserviceapp sh
$ pytest 
```
To exit the shell
```bash
$ exit
```
## App Datastore
App uses Sqlite as it's datastore

## Initial Data Load
App uses two tables for reference data
```bash
* ProductCatalog - Which is the catalog for the products that you can place a order 
    (Defaulted to "Apples" and "Oranges" on application startup) and the cost of the product
* Offer - This is the master for all the offers on the products that you can place an order. Currently:
    * Apples are offered at "Buy one get one free"
    * Oranges are offered at "3 for the price of 2"
```
## API Usage
To browse through the API's exposed use [API Doc](http://localhost:5000/)

The offers are automatically applied to the successfull order. The "discountedunits" field in the order response represents the number of units added after applying the offer. 



