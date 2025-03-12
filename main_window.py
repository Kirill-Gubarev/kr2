from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QTableWidget,
    QHeaderView,
    QStackedWidget,
    QPushButton,
    QTableWidgetItem
)
from PySide6.QtCore import Qt
from db_manager import db_manager

class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__db_manager = db_manager()
        self.__db_manager.connect()

        self.setWindowTitle("employees")
        self.__ui_init()

        #self.__load_employee_table()

    def __ui_init(self):
        self.__centralWidget = QWidget()
        self.__main_layout = QVBoxLayout()
        self.__centralWidget.setLayout(self.__main_layout)
        self.setCentralWidget(self.__centralWidget)

        self.__button_layout = QHBoxLayout()
        self.__main_layout.addLayout(self.__button_layout)

        self.__stacked_widget = QStackedWidget()
        self.__main_layout.addWidget(self.__stacked_widget)

        self.__button_layout.addWidget(QPushButton("yemployees", clicked=lambda: self.__set_page("yemplyees", 0)))
        self.__button_layout.addWidget(QPushButton("tasks", clicked=lambda: self.__set_page("tasks", 1)))

        self.__create_employee_page()
        self.__create_tasks_page()

    def __set_page(self, name, id):
        self.setWindowTitle(name)
        self.__stacked_widget.setCurrentIndex(id)

    def __create_employee_page(self):
        self.__employee_table = QTableWidget(0,5)
        self.__employee_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.__employee_table.setHorizontalHeaderLabels(["name", "position", "salary", "hire date", "department"])
        header = self.__employee_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.__stacked_widget.addWidget(self.__employee_table)


    def __create_tasks_page(self):
        self.__tasks_table = QTableWidget(0,6)
        self.__tasks_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.__tasks_table.setHorizontalHeaderLabels(["name", "description", "status", "department", "project", "yemployee"])
        header = self.__tasks_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.__stacked_widget.addWidget(self.__tasks_table)

    def __load_employee_table(self):
        self.__table_insert(self.__employee_table, self.__db_manager.get_all_employees())

    def __table_insert(self, table: QTableWidget, data: list):
        row = table.rowCount()
        columns = table.columnCount()
        table.setRowCount(row + 1)

        for x in range(0, columns):
            table.setItem(row, x, self.__createItem(data[row][x]))

    def __createItem(self, item):
        tableItem = QTableWidgetItem(str(item))
        tableItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        return tableItem