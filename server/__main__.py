#!/usr/bin/env python3

import connexion
from server import encoder


HOST = "localhost"


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Explorando Marte'})
    app.run(host=HOST, port=8080)


if __name__ == '__main__':
    main()
