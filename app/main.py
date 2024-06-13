from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    joke = get_joke_of_the_day()
    return render_template('index.html', joke=joke)

def get_joke_of_the_day():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if response.status_code == 200:
        return response.json()['joke']
    else:
        return "No joke available right now, sorry!"

if __name__ == '__main__':
    app.run()