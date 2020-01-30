from hookup_gui.utils.dialogs import *
from dotenv import load_dotenv
from distutils.util import strtobool
import pathlib
import json
import os


PROJECT_PATH = pathlib.Path(__file__).parent.parent
ASSETS_PATH = PROJECT_PATH / 'assets'
CONFIG_FILE = PROJECT_PATH / 'config.json'
DEV_CONFIG_FILE = PROJECT_PATH / 'dev_config.json'
ENV_FILE = PROJECT_PATH / '.env'
if ENV_FILE.exists():
    load_dotenv(dotenv_path=str(ENV_FILE))
DEBUG = os.getenv('DEBUG') or "False"


class Config:
    def __init__(self, cpath: pathlib.Path = CONFIG_FILE):
        if strtobool(DEBUG):
            cpath = DEV_CONFIG_FILE
        self.cpath = cpath
        self.config_dict = dict()
        self._load()

    def _load(self):
        with self.cpath.open('r') as cfg:
            self.config_dict = json.load(cfg)

    def _save(self):
        with self.cpath.open('w') as cfg:
            json.dump(self.config_dict, cfg)

    def get(self, key):
        return self.config_dict.get(key)

    def put(self, key, val):
        self.config_dict[key] = val
        self._save()


class ApiMap:
    def __init__(self, base):
        base = f"{base}/api"
        self.NGROK_URL = f"{base}/get_ngrok_url/"
        self.CURRENT_PAGE = f"{base}/page/get_current"
        self.PAGES = f"{base}/pages"
        self.SET_CURRENT_PAGE = f"{base}/page/set_current"
        self.GET_RECORD = f"{base}/record/list"
