build:
	docker build -t pysubstitutor .

coverage:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor coverage run --source pysubstitutor -m pytest

coverage-report:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor coverage report

coverage-html:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor coverage html
	open htmlcov/index.html

help:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor python -m pysubstitutor -h

run:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor python -m pysubstitutor --input=data/input/text_substitutions.plist --output=data/output/table.md --zip=data/output/PersonalDictionary.zip

test:
	docker run -it --rm --name pysubstitutor -v ${PWD}:/usr/src/app -w /usr/src/app pysubstitutor pytest tests
