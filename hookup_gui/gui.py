from PySide2.QtWidgets import (QApplication, QMainWindow,
                               QListWidgetItem)
from PySide2.QtGui import QFont, QIcon
from hookup_gui.utils import (
    ApiMap, ConfirmDialog, NotifyDialog, InputDialog,
    ASSETS_PATH, WIN_EVENT, Config
)
from hookup_gui.ui.view import Ui_MainWindow
import requests
import sys
import json


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, api_map: ApiMap, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.api_map = api_map
        self.setWindowTitle("Hookup GUI")
        self.line_edit_ngrok_url.setReadOnly(True)
        self.tabWidget.currentChanged.connect(self.tab_change)
        self.tabWidget.setCurrentIndex(0)
        self.refresh_icon.clicked.connect(self.get_results)
        self.configure_icons()
        self.list_widget_results.isWrapping()
        self.list_view_pages.itemDoubleClicked.connect(
            self.set_current_page)  # pages item handler
        self.get_ngrok_url()
        self.configure_tab_prepare()
        self.page_cache = dict()

    def configure_icons(self):
        self.refresh_icon.setIcon(QIcon(str(ASSETS_PATH / 'refresh.svg')))
        self.tabWidget.setTabIcon(0, QIcon(str(ASSETS_PATH / 'cogs.png')))
        self.tabWidget.setTabIcon(1, QIcon(str(ASSETS_PATH / 'result.png')))

    def configure_tab_prepare(self):
        self.get_current_page()
        self.get_pages()

    def results_tab_prepare(self):
        self.get_results()

    def get_ngrok_url(self):
        data = requests.get(self.api_map.NGROK_URL)
        self.line_edit_ngrok_url.setText(data.json())

    def get_current_page(self):
        data = requests.get(self.api_map.CURRENT_PAGE).json()
        self.label_current_page_name.setText(data['name'])
        self.text_browser_current_page_soruce.setPlainText(data['source'])

    def get_pages(self):
        self.list_view_pages.clear()
        data = requests.get(self.api_map.PAGES).json()
        self.page_cache = data
        for page in data:
            item = QListWidgetItem(page['name'])
            item.setFont(QFont("Ubuntu", 18))
            self.list_view_pages.addItem(item)

    def set_current_page(self):
        item_title = self.list_view_pages.currentItem().text()
        if ConfirmDialog(f"{item_title} will be your current page. Are you sure?").get_result():
            response = requests.post(self.api_map.SET_CURRENT_PAGE, json={
                'currentPage': self.list_view_pages.currentItem().text()},
                headers={"Content-Type": "application/json"})
            data = response.json()

            self.label_current_page_name.setText(data['name'])
            self.text_browser_current_page_soruce.setPlainText(data['source'])
            NotifyDialog(data['msg'])

    def tab_change(self, tab_index):
        if tab_index == 0:
            self.configure_tab_prepare()
        else:
            self.results_tab_prepare()

    def get_results(self):
        self.list_widget_results.clear()
        data = requests.get(self.api_map.GET_RECORD)

        for result in data.json():
            res = result['data']
            res['site_name'] = result['pageName']
            item = QListWidgetItem(json.dumps(
                res, indent=4, sort_keys=True))
            self.list_widget_results.addItem(item)


def run_gui():
    app = QApplication([])
    config = Config()
    server_ip = InputDialog(
        "SERVER IP", "Please type yout server IP",
        default=config.get('server_address')).get_data()
    if server_ip != WIN_EVENT.CLOSE:
        config.put('server_address', server_ip)
        win = MainWindow(ApiMap(server_ip))
        win.show()
        sys.exit(app.exec_())
