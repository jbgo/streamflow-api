.PHONY: test
test:
	pytest

.PHONY: serve
serve:
	uvicorn main:app --reload
