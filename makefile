run:
	uvicorn main:app 


pylint:
	@echo 'Start pylint'
	pylint main.py
	@echo 'End pylint'
