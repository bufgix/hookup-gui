from PySide2.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QSizePolicy, QLineEdit
)
from PySide2.QtCore import Qt
from enum import Enum


class WIN_EVENT(Enum):
    CLOSE = "CLOSE"


class ConfirmDialog(QDialog):
    def __init__(self, msg, parent=None):
        super().__init__(parent)
        self.status = False
        self.setWindowTitle("Confirm")
        layout = QVBoxLayout()
        layout_2 = QHBoxLayout()
        label = QLabel(msg)
        close_btn = QPushButton("Cancel")
        close_btn.clicked.connect(lambda: self._trigger(False))
        ok_btn = QPushButton("Yes")
        ok_btn.clicked.connect(lambda: self._trigger(True))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        layout_2.addWidget(ok_btn)
        layout_2.addWidget(close_btn)
        layout.addLayout(layout_2)
        self.setLayout(layout)
        self.resize(300, 100)
        self.setStyleSheet("""
        background-color: '#424242';
        color: 'white'
        """)
        self.exec_()

    def _trigger(self, code: bool):
        self.status = code
        self.close()

    def get_result(self):
        return self.status


class NotifyDialog(QDialog):
    def __init__(self, msg):
        super().__init__()
        self.setWindowTitle("Info")
        layout = QVBoxLayout()
        label = QLabel(msg)
        label.setAlignment(Qt.AlignCenter)

        btn = QPushButton("Ok")
        btn.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,
                                      QSizePolicy.Preferred))
        btn.clicked.connect(self.close)

        layout.addWidget(label)
        layout.addWidget(btn)
        self.setLayout(layout)
        self.resize(300, 100)
        self.setStyleSheet("""
        background-color: '#424242';
        color: 'white'
        """)
        self.exec_()


class InputDialog(QDialog):
    def __init__(self, title: str, msg: str, default: str = ""):
        super().__init__()
        self.interaction = False
        self.data = default
        self.setWindowTitle(title)
        layout = QVBoxLayout()

        label = QLabel(msg)
        line_edit = QLineEdit()
        line_edit.setText(default)
        line_edit.textChanged.connect(lambda msg: self.handle(msg))

        btn = QPushButton("OK")
        btn.clicked.connect(self.exit_btn)

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(btn)

        self.setLayout(layout)

        self.exec_()

    def handle(self, val):
        self.interaction = True
        self.data = val

    def exit_btn(self):
        self.interaction = True
        self.close()

    def get_data(self):
        return self.data

    def closeEvent(self, event):
        if not self.interaction:
            self.data = WIN_EVENT.CLOSE
