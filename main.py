from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
import sys
import sqlite3
import csv

def csv_to_sqlite(csv_file_path, db_file_path):
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    # 检查表是否存在，如果不存在则创建
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS information_price (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        serial_number TEXT,
        name TEXT,
        specification TEXT,
        unit TEXT,
        price_excluding_tax REAL,
        note TEXT,
        materail_date DATE,
        area TEXT,
        period TEXT,
        major TEXT,           
        UNIQUE(name,specification,period)
    )''')
    
    with open(csv_file_path, 'r', encoding='gbk') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # 跳过标题行
        for row in csvreader:         
            cursor.execute("""
            INSERT OR IGNORE INTO information_price    
                (serial_number, name, specification, unit, price_excluding_tax, note, materail_date,area,period, major)        
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", row)
    conn.commit()
    conn.close()


uiLoader = QUiLoader()
class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        # 初始化每页50条
        self.current_page=1
        self.items_per_page = 50
        # 使用 QUiLoader 加载 UI
        self.ui = uiLoader.load('mainwindow.ui', self)
        # 连接到 SQLite 数据库
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("materials.db")
        self.db.open()
        # 创建 QSqlQueryModel
        self.model = QSqlQueryModel(self)        
        # 初始显示
        self.load_data_from_database()
        # 将模型设置到 TableView
        self.ui.tableView.setModel(self.model)
        # 添加多选框信号和槽连接
        self.ui.checkBox_gushi_house.stateChanged.connect(self.search_materials) 
        self.ui.checkBox_xinyang_house.stateChanged.connect(self.search_materials)
        self.ui.checkBox_zhengzhou_house_month.stateChanged.connect(self.search_materials)
        self.ui.checkBox_zhengzhou_house_quarter.stateChanged.connect(self.search_materials)
        self.ui.checkBox_other_house.stateChanged.connect(self.search_materials)
        self.ui.checkBox_xinyang_road.stateChanged.connect(self.search_materials)
        self.ui.checkBox_zhengzhou_road.stateChanged.connect(self.search_materials)
        self.ui.checkBox_other_road.stateChanged.connect(self.search_materials)
        # 添加下拉框信号和槽连接
        self.ui.comboBox_gushi_house_period.currentIndexChanged.connect(self.search_materials)
        self.ui.comboBox_xinyang_house_period.currentIndexChanged.connect(self.search_materials)
        self.ui.comboBox_zhengzhou_house_mperiod.currentIndexChanged.connect(self.search_materials)
        self.ui.comboBox_zhengzhou_house_qperiod.currentIndexChanged.connect(self.search_materials)
        self.ui.comboBox_other_house_qperiod.currentIndexChanged.connect(self.search_materials)
        self.ui.comboBox_xinyang_road_period.currentIndexChanged.connect(self.search_materials)
        self.ui.comboBox_zhengzhou_road_period.currentIndexChanged.connect(self.search_materials)
        self.ui.comboBox_other_road_period.currentIndexChanged.connect(self.search_materials)


        # 连接分页控件的信号和槽
        self.ui.pushButton_next.clicked.connect(self.on_next_page)
        self.ui.pushButton_previous.clicked.connect(self.on_previous_page)
        # 连接查询按钮的点击事件
        self.ui.pushButton.clicked.connect(self.search_materials)

    def load_data_from_database(self,where_clause="1=1"):
        # 设置初始显示
        query = f"SELECT serial_number 序号, name 材料名称, specification 规格型号, unit 单位, price_excluding_tax 不含税价, note 备注, period 期数 FROM information_price WHERE {where_clause}"
        self.query_database(query)  # 从第一页开始加载

    def query_database(self, query):       #设置ui汉字表头,页数
        self.model.setHeaderData(0, Qt.Horizontal, '序号')
        self.model.setHeaderData(1, Qt.Horizontal, '材料名称')
        self.model.setHeaderData(2, Qt.Horizontal, '规格型号')
        self.model.setHeaderData(3, Qt.Horizontal, '单位')
        self.model.setHeaderData(4, Qt.Horizontal, '不含税价')
        self.model.setHeaderData(5, Qt.Horizontal, '备注')
        self.model.setHeaderData(6, Qt.Horizontal, '期数')
        offset_value = (self.current_page - 1) * self.items_per_page
        query = f"{query} LIMIT {self.items_per_page} OFFSET {offset_value}"        
        self.model.setQuery(query)
 
    def on_next_page(self):
        where_clause = "1=1"  # 这里需要根据实际的搜索条件来构建
        total_records = self.get_total_records(where_clause)
        if self.current_page * self.items_per_page < total_records:
            self.current_page += 1
            self.search_materials(where_clause)


    def on_previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            # 同上，传入查询条件
            where_clause = "1=1"  # 根据需要构建查询条件
            self.search_materials(where_clause)
    def get_total_records(self, where_clause):
           pass     
    def search_materials(self, where_clause="1=1"):
        # 获取多选框的状态
        checkBox_gushi_house_checked= self.ui.checkBox_gushi_house.isChecked()
        checkBox_xinyang_house_checked = self.ui.checkBox_xinyang_house.isChecked()
        checkBox_zhengzhou_house_month_checked=self.ui.checkBox_zhengzhou_house_month.isChecked()
        checkBox_zhengzhou_house_quarter_checked=self.ui.checkBox_zhengzhou_house_quarter.isChecked()
        checkBox_other_house_checked=self.ui.checkBox_other_house.isChecked()
        checkBox_xinyang_road_checked = self.ui.checkBox_xinyang_road.isChecked()
        checkBox_zhengzhou_road_checked=self.ui.checkBox_zhengzhou_road.isChecked()
        checkBox_other_road_checked=self.ui.checkBox_other_road.isChecked()
        # 获取下拉框的选中值
        gushi_house_period = self.ui.comboBox_gushi_house_period.currentText()
        xinyang_house_period = self.ui.comboBox_xinyang_house_period.currentText()
        zhengzhou_house_mperiod = self.ui.comboBox_zhengzhou_house_mperiod.currentText()
        zhengzhou_house_qperiod = self.ui.comboBox_zhengzhou_house_qperiod.currentText()
        other_house_period = self.ui.comboBox_other_house_qperiod.currentText()
        xinyang_road_period = self.ui.comboBox_xinyang_road_period.currentText()
        zhengzhou_road_period = self.ui.comboBox_zhengzhou_road_period.currentText()
        other_road_period = self.ui.comboBox_other_road_period.currentText()
        # 构建地区专业查询条件
        area_major_condition = []
        if checkBox_gushi_house_checked:
            area_major_condition.append(f"area = '固始' AND major = '房建' AND period = '{gushi_house_period}'")
        if checkBox_xinyang_house_checked:
            area_major_condition.append(f"area = '信阳' AND major = '房建' AND period = '{xinyang_house_period}' ")
        if checkBox_zhengzhou_house_month_checked:
            area_major_condition.append(f"area = '郑州' AND major = '房建' AND period = '{zhengzhou_house_mperiod}' ")
        if checkBox_zhengzhou_house_quarter_checked:
            area_major_condition.append(f"area = '郑州' AND major = '房建' AND period = '{zhengzhou_house_qperiod}' ")
        if checkBox_other_house_checked:  #待扩展+++++++++++++++++++++++++
            area_major_condition.append(f"area = '其他' AND major = '房建' AND period = '{other_house_period}'")        
        if checkBox_xinyang_road_checked:
            area_major_condition.append(f"area = '信阳' AND major = '公路' AND period = '{xinyang_road_period}' ")
        if checkBox_zhengzhou_road_checked:
            area_major_condition.append(f"area = '郑州' AND major = '公路' AND period = '{zhengzhou_road_period}' ")
        if checkBox_other_road_checked:
            area_major_condition.append(f"area = '其他' AND major = '公路' AND period ='{other_road_period}' ")        
        # 从界面控件获取查询参数
        material_name = self.ui.lineEdit.text()
        where_clause_parts = []
        if area_major_condition:
            where_clause_parts.append("(" + " OR ".join(area_major_condition) + ")")
        if material_name.strip():
            where_clause_parts.append(f"(name LIKE '%{material_name}%' OR specification LIKE '%{material_name}%')")
        where_clause = " AND ".join(where_clause_parts) if where_clause_parts else "1=1"
        query = f"SELECT serial_number, name, specification, unit, price_excluding_tax, note, period FROM information_price WHERE {where_clause}"
        results=self.query_database(query)
        
if __name__ == "__main__":
    # csv_to_sqlite("固始信息价.csv", "materials.db")  # 导入 CSV 数据到 SQLite
    # csv_to_sqlite("郑州信阳信息价.csv", "materials.db")
    app = QApplication([])
    window =MyMainWindow()
    window.show()
    sys.exit(app.exec_())