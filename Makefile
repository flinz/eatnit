MANAGE=python manage.py
PROJECT_NAME=eatnit
FLAKE8_OPTS=--exclude=.git,migrations --max-complexity=10 --ignore=E501,F403
SETTINGS=--settings=eatnit.settings.dev

test:
	$(MANAGE) test --where=. $(SETTINGS)

lint:
	flake8 $(FLAKE8_OPTS) .

clean:
	rm -rf .coverage cover nosetests.xml coverage.xml
	rm -rf $(PROJECT_NAME)/static/CACHE
	find . -name '*.pyc' -exec rm '{}' ';'

update:
	$(MAKE) clean
	$(MANAGE) syncdb
	$(MANAGE) migrate
	$(MANAGE) collectstatic --noinput

