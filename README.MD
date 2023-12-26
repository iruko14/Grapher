# Installing environmental requirements

To set the app you need to run these commands in the console (Windows):

```sh
python3 -m venv enviroment
.\enviroment\Scripts\activate
pip3 install -r requirements.txt
```

# Run app

```sh
python3 main.py
```

# Run docker

```sh
docker-compose build
docker-compose up -d
docker-compose ps
docker-compose exec grapher.csv bash
```

# Stop docker

```sh
docker-compose down
```