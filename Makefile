

reset-db:
	docker-compose run web python cli.py reset-db

run:
	docker-compose run web python cli.py start
