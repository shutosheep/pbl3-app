# pbl3-app

This is the source code of group I's demo application.

Here is a screenshot of the app.

![screenshot](screenshot.png)

## Setup

### Git clone this repo

```
git clone https://github.com/shutosheep/pbl3-app
cd pbl3-app/
```

### Setup frontend

Make sure you have installed Node.js and `npm` command is avilable. \
I recommend installing Node.js with [nvm](https://github.com/nvm-sh/nvm).

```
cd frontend/
npm i
cd ..
```

### Setup backend

```
cd backend/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
deactivate
cd ..
```

## Run the application

Open 2 terminals and run these commands

```
cd frontend/
npm run dev
```

```
cd backend/
source env/bin/activate
flask run
```
