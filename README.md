# AI Clothes Store (this is temporary name)
## The Plot
Welcome to my pet project — a stylish clothing web store where you can generate any print you like. All rights reserved by me (for now)...

## Some boring tech stuff (mostly for myself so I don't forget)
- Initialize initial DB data `python manage.py init_db`
- Built dev docker images `docker-compose build`
- Run dev docker containers `docker-compose up`
- Open web container bash `docker-compose exec web bash`

*In prod there is no need to run separate container with DB as I use [Railway](https://railway.com/) for
hosting it, so simply run container with the django project. Also set env vars for prod DB*

- Build prod docker image `docker build -t ai_clothes_store_image .`
- Run prod docker container `docker run ai_clothes_store_image`

## Disclaimer
Development is ongoing.
