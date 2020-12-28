import settings

from utilities import create_app
from controllers.email_controller import ns_email as email_namespace

app, api = create_app()

api.add_namespace(email_namespace)

print("api : {0}", api.namespaces)

if __name__ == '__main__':
    print('Running in local mode, starting flask')
    app.run(debug=settings.FLASK_DEBUG)