# Flask & Babel & SCSS & SSR
- prebuild process
 - js -> babel -> minify
 - scss -> css -> minfiy 

## How To Run
- make virtualenv
```shell script
python3 -m venv venv
source venv/bin/activate
```

- install python dependency
```shell script
pip3 install -r requirements.txt
```

- install babel-cli globally
```shell script
npm install -g babel-cli
```

- install babel-preset-env locally
```shell script
npm install --save babel-preset-env
```

- run
```shell script
python3 app.py
```

## Reference
> [Flask-Assets](https://flask-assets.readthedocs.io/en/latest/)
> [StackOverflow - How to minify ES2016 or convert to ES2015 in flask?](https://stackoverflow.com/questions/55712578/how-to-minify-es2016-or-convert-to-es2015-in-flask)
> [Compiling Frontend JavaScript & Stylesheets Flask](https://hackersandslackers.com/flask-assets/)