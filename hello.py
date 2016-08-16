from selenium import webdriver
from flask import Flask
from flask import render_template
from flask import request
import config
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World"

@app.route("/form")
def form():
    return render_template('form.html',name="Tim")

@app.route("/kill",methods=['POST'])
def kill():
    driver = webdriver.Chrome(executable_path='C:/Python/selenium/webdriver/chrome/chromedriver')
    driver.set_window_size(640, 480)
    driver.get('http://10.61.8.133:9999/shutdown')
    return "Hello";

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(port=config.server['port'],host=config.server['ip'])