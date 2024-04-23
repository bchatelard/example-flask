from flask import Flask
import signal, logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

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
