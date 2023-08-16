FastAPI CRUD Project

- create python enviroment:
python3 -m venv .venv
source .venv/bin/activate

- install modules:
pip install -r requirements.txt

- docker container:
docker run --name app-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
docker start app-postgres

- run app:
uvicorn main:app --reload