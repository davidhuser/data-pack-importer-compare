init:
	pip install pipenv
	pipenv install --dev
test:
	ypython setup.py test