# Projects

## Build the docker:

```
 docker build -t my-jenkins-food_image .
 ```

## Run the Image: 
```
docker run --name jenkins-food --restart=on-failure --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro --publish 8080:8080 --publish 50000:50000 my-jenkins-food_image
 ```


## Go to:
```
https://localhost:8080/
```

## Get the password:
```
 docker exec jenkins-food cat /var/jenkins_home/secrets/initialAdminPassword
```

## Enter the container:
```
docker exec -it jenkins-food /bin/bash
```



