.PHONY: test
test:
	/bin/bash -c 'source .env.test && pytest'

.PHONY: serve
serve:
	/bin/bash -c 'source .env && uvicorn main:app --reload'
