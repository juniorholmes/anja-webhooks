import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    ANJA_MODERATOR_BOT_TOKEN = os.environ.get('ANJA_MODERATOR_BOT_TOKEN') or 'you-will-never-guess'