

clean:
	-rm -rf build
	-rm -rf *~*
	-find . -name '*.pyc' -exec rm {} \;

# run unit tests
test: clean
	python manage.py migrate contacts
	python manage.py test contacts
