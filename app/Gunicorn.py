from flask.ext.script import Command, Option


class GunicornServer(Command):
    """Run the app within Gunicorn"""

    def __init__(self, host='127.0.0.1', port=5000, **options):
        super(GunicornServer, self).__init__()
        self.port = port
        self.host = host
        self.server_options = options

    def get_options(self):
        options = (
            Option('--gunicorn-host',
                   dest='host',
                   default=self.host),

            Option('--gunicorn-port',
                   dest='port',
                   type=int,
                   default=self.port))

        return options

    def run(self, host, port):
        from . import create_app

        app = create_app()

        return app.run(host=host, port=port)
