from hookup_gui.utils.dialogs import *
import pathlib


PROJECT_PATH = pathlib.Path(__file__).parent.parent
ASSETS_PATH = PROJECT_PATH / 'assets'


class ApiMap:
    def __init__(self, base):
        base = f"{base}/api"
        self.NGROK_URL = f"{base}/get_ngrok_url/"
        self.CURRENT_PAGE = f"{base}/page/get_current"
        self.PAGES = f"{base}/pages"
        self.SET_CURRENT_PAGE = f"{base}/page/set_current"
        self.GET_RECORD = f"{base}/record/list"
