from flask import Flask
import signal

app = Flask(__name__)

def exit_gracefully(*args):
    print("Doing cleanup actions here")

signal.signal(signal.SIGTERM, exit_gracefully)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'


if __name__ == "__main__":
    app.run()
