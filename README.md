##Cloning the app
```` bash
$ git clone https://github.com/amisdun/redis_app.git
$ cd redis_app/
````
##Build and Run App
```` bash
$ docker-compose build
$ docker-compose up
````
##API's
````
http://localhost:8000/api/communicate/server1
http://localhost:8000/api/communicate/server2
````

##Instructions
```` javascript
1. make a (Get) request with one of the api endpoint to listen to incoming message
2. make a (Post) request with the other endpoint passing a message as a parameter Eg  { message: "hello word"}, to the listening endpoint.
````  