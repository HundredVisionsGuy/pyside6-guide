"""
list_widgets.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QListWidget,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("ListView WIdget")

        # TODO: create your list widget
        self.music_selection = QListWidget()

        # TODO: add items to your list widget
        self.music_selection.addItems(["Classical", "Rock", "Rap", "R&B", "Jazz"])
        self.music_selection.addItem("Ska")

        # Add signals to list widget
        self.music_selection.currentItemChanged.connect(self.index_changed)
        self.music_selection.currentTextChanged.connect(self.text_changed)

        # TODO: add a button to test getting input from the list widget
        select_button = QPushButton("Choose")
        select_button.setCheckable(False)
        select_button.clicked.connect(self.choose_genre)

        """
        Advanced TODO
        1. check out the docs at https://doc.qt.io/qt-6/qlistwidget.html
        2. explore the public methods
        3. check out the slots and signals
        4. customize your QListWidget
        5. style your QListWidget
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.music_selection)
        layout.addWidget(select_button)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


    # Process Selection
    def choose_genre(self):
        """gets selection and displays information"""
        genre = self.music_selection.currentItem().text()
        print("Do something with the selection")


    # List Widget Signals - in case you want to perform an action when the
    # user interacts with the list widget.
    def index_changed(self, index):  # Not an index, index is a QListWidgetItem
        print(index.text())

    def text_changed(self, text):  # text is a str
        test = self.music_selection.currentItem().text()
        print(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
