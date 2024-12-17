# Rentomatic

A demo implementation of a clean architecture in Python.

The goal of the "Rent-o-Matic" project is to create a simple search engine for a room renting company. Objects in the dataset (rooms) are described by some attributes and the search engine shall allow the user to set some filters to narrow the search. The system exposes a REST API and works with three types of storage system: in-memory database, Postgres, MongoDB.

This is a repository with implementation of the book "Clean Architectures in Python" by Leonardo Giordani, published by Leanpub.

You can download the book [here](https://leanpub.com/clean-architectures-in-python).

## 🚀 Starting

These instructions will help you to clone de project and run it in your machine and test.

### 📋 Prerequisite

- [Python](https://www.python.org/)

- [Docker: Will need it to run the application](https://docs.docker.com/get-docker/)

- [docker-compose: Necessary to up the container](https://docs.docker.com/compose/install/)


### 🔧 Instalação

Clone the repository:


```
 git clone https://github.com/GiovaniBoff/rentomatic
```

Installing dependecies:

```
 pip install -t requeriments.txt
```

Running the database:
```
 python manage.py init-postgres

```
Running the application:

## ⚙️ Running the tests

To run the unit test for the application, run the following command:
```
 python manage.py test
```

To run the integration test for the application, run the following command:
```
 python manage.py test -- --integration
```

## 🛠️ Build with

* [Python](https://www.python.org/) - Language used.
* [Postgres](https://www.mysql.com/) - Database used.
* [Docker](https://docs.docker.com/get-docker) - Used to manage containers.


---
⌨️ with ❤️ for [Giovani Boff](https://github.com/GiovaniBoff) 😊
