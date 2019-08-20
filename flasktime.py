from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
import datetime

app = Flask(__name__)
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')


@app.route('/')
def time():
    timezones = ["LOC", "YEKT", "MSK", "VLAT"]
    selected_timezone = request.args.get("select")
    time = datetime.datetime.now()
    if selected_timezone == "YEKT":
        time = time + datetime.timedelta(hours=+5)
    elif selected_timezone == "MSK":
        time = time + datetime.timedelta(hours=+3)
    elif selected_timezone == "VLAT":
        time = time + datetime.timedelta(hours=+10)

    return template.render(
        time=time.time(),
        timezones=timezones,
        selected_timezone=selected_timezone
    )


if __name__ == "__main__":
    app.run(debug=True)
