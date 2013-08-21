

clean:
	-rm -rf build
	-rm -rf *~*
	-find . -name '*.pyc' -exec rm {} \;

# run unit tests
test: clean
	python manage.py reset contacts
	python manage.py syncdb --noinput
	python manage.py migrate contacts
	python manage.py migrate middleware
	python manage.py test contacts
