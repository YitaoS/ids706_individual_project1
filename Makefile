PYTHON_FILES := src tests
FILES_TO_REMOVE = *.png report.md

.PHONY: install format lint run report

install:
	pip install --upgrade pip
	pip install .[dev]

format:
	# Automatically format code using black
	black $(PYTHON_FILES)
	
lint:
	ruff check $(PYTHON_FILES)

run:
	python3 src/script.py

deploy:
	git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
	git config --local user.name "github-actions[bot]"
	git add ./*.md
	git add ./*.png
	git commit -m "Add report and images"

test:
	PYTHONPATH=src pytest -s tests
	pytest --nbval descriptive_statistics.ipynb

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.png" -delete
	rm -f report.md
	@git rm $(FILES_TO_REMOVE)

check-format:
	black --check $(PYTHON_FILES)

ci: lint format check-format test
