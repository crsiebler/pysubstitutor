clean:
	rm -rf build dist *.egg-info .pytest_cache .coverage htmlcov

build:
	docker build -t pysubstitutor .

coverage:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor coverage run --source pysubstitutor -m pytest

coverage-report:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor coverage report

coverage-html:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor coverage html
	open htmlcov/index.html

deploy:
	python3 -m build
	python3 -m twine upload dist/*

help:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor -h

run:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor --input=data/input/text_substitutions.plist --output=data/output/dictionary.txt --zip=data/output/PersonalDictionary.zip

run-md:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor --input=data/input/text_substitutions.plist --output=data/output/dictionary.md

test:
	docker run --rm --entrypoint "" -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor pytest tests
