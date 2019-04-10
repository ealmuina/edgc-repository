import connexion
from flask import render_template, send_from_directory, abort

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<path:path>')
def send_file(path):
    if path.startswith('input/'):
        return send_from_directory('input', path[6:])
    elif path.startswith('kernel/'):
        return send_from_directory('kernel', path[7:])
    return abort(404)


def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=True)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    run_flask()
