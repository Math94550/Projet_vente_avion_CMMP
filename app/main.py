from flask import Flask
from config import config

app = Flask(__name__)
app.config.update(config)

if __name__ == '__main__':
    app.run()

