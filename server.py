import argparse

import connexion
from flask import send_from_directory, abort

import task

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


@app.route('/<path:path>')
def send_file(path):
    allowed_dirs = ['input', 'kernel', 'scripts']
    for d in allowed_dirs:
        if path.startswith('%s/' % d):
            return send_from_directory(d, path[len(d) + 1:])
    return abort(404)


def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=True)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-greedy', action='store_false')
    args = parser.parse_args()

    task.GREEDY_TASKS = args.no_greedy

    run_flask()
