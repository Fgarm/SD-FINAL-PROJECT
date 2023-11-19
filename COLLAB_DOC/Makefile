.PHONY: runserver makemigrations makemigrationapp migrate
runserver :
	python manage.py runserver --settings=COLLAB_DOC.local_settings
makemigrations :
	python manage.py makemigrations --settings=COLLAB_DOC.local_settings
# make makemigrationapp app=app
makemigrationapp :
	python manage.py makemigrations --settings=COLLAB_DOC.local_settings $(app)
migrate :
	python manage.py migrate --settings=COLLAB_DOC.local_settings