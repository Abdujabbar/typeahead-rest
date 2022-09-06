Typeahead rest api
---------------------------


Installation
---------------------------
Create virtual environment with the command:

`
python -m venv .venv
`

then activate

`
source .venv/bin/activate
`


After activation you need install requirements

`
pip install -r requirements.txt
`

That's all, next look how you run


How to run
-------------------------
`
python run.py 8000 data/words_alpha.txt 
`

Usage: http://localhost:8000/<query>

`
curl http://localhost:8000/hel
`