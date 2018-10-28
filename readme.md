

## DOCKER BUILD

docker build .

export PORT=8080
docker run -p 8080:8080 >>image<<

## Query the running docker image

curl -i -X GET http://localhost:8080/status

curl -i -X GET "http://localhost:8080/recommendation?city=paris&date_in=20181201&date_out=20181208&group_size=2"

!Current version is not parallelized.


## Heroku specific

heroku container:push web -a twocasasbackend

heroku container:release web -a twocasasbackend


curl -i -X GET "https://twocasasbackend.herokuapp.com/recommendation?city=paris&date_in=20181201&date_out=20181208&group_size=2"
