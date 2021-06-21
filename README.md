# Aermetric test project

### Installation
To run the project you need to install docker and docker-compose from official repos

1. Install docker
   
```shell
# Quick docker intallation

$ curl -fsSL https://get.docker.com -o get-docker.sh

$ sh get-docker.sh
```

2. Install docker-compose, follow official guide for installation [here](https://docs.docker.com/compose/install/)

### Run project
1. Create folder secrets in root of the project and add **app.env**, **postgres.env**
```
# Your projetc structure should look something like this
aermetric -
    app 
    configs
    secrets -
        app.env
        postgres.env
```
   
2. Run following command (add optional -d option to run it in daemon mode)

```shell
$ docker-compose up --build
```

3. Visit 127.0.0.1/metrics/:unique_id to see chronicle and its events 
