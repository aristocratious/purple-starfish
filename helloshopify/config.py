import os

class DefaultConfig(object):

    PROJECT = "Hello Shopify"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = True
    TESTING = False

    SECRET_KEY = 'secret key'

    SERVER_NAME = "https://00581725.ngrok.io"
    PREFERRED_URL_SCHEME = "https"

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/helloshopify.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    SHOPIFY_API_KEY = '8fbd25d888170e0ad7dde58427374a1e'
    SHOPIFY_SHARED_SECRET = 'b3f91f3c58a4561e69c5e753faa48fcb'
