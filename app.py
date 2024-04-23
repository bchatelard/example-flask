from flask import Flask
import signal, logging
from logging.config import dictConfig


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

def exit_gracefully(*args):
    logging.warn("Doing cleanup actions here")

signal.signal(signal.SIGTERM, exit_gracefully)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'


if __name__ == "__main__":
    logging.warn("launching app")
    app.run()
