from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
import sys
import sqlite3
import csv
class MaterialDataModel():
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor() 
    def create_table(self):
        self.cursor.execute('''
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
        self.conn.commit()            

    def load_csv2db(self,csv_file):       
        with open(csv_file, 'r', encoding='gbk') as cf:
            csvreader = csv.reader(cf)
            next(csvreader)  # 跳过标题行
            for row in csvreader:         
                self.cursor.execute("""
                INSERT OR IGNORE INTO information_price    
                    (serial_number, name, specification, unit, price_excluding_tax, note, materail_date,area,period, major)        
                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", row)
        self.conn.commit()
    def close_connection(self):
        self.conn.close()
    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

uiLoader = QUiLoader()
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("材料价助手")
        self.setGeometry(100, 50, 900, 800)    #setGeometry方法的参数分别是窗口的x坐标、y坐标、宽度和高度。
      
        self.model = MaterialDataModel("materials.db")
        self.model.create_table()
        # 使用 QUiLoader 加载 UI
        self.ui = uiLoader.load('mainwindow.ui', self)
        # 连接到 SQLite 数据库
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("materials.db")
        self.db.open()
        # 创建 QSqlQueryModel
        self.query_model  = QSqlQueryModel(self)  
        #设置界面汉字表头,页数
        self.query_model.setHeaderData(0, Qt.Horizontal, '序号')
        self.query_model.setHeaderData(1, Qt.Horizontal, '材料名称')
        self.query_model.setHeaderData(2, Qt.Horizontal, '规格型号')
        self.query_model.setHeaderData(3, Qt.Horizontal, '单位')
        self.query_model.setHeaderData(4, Qt.Horizontal, '不含税价')
        self.query_model.setHeaderData(5, Qt.Horizontal, '备注')
        self.query_model.setHeaderData(6, Qt.Horizontal, '期数')
        self.query_model.setHeaderData(6, Qt.Horizontal, '专业')
        # 将模型设置到 TableView
        self.ui.tableView.setModel(self.query_model) 
        # 添加多选框信号和槽连接
        self.ui.checkBox_gushi_house.stateChanged.connect(self.search_material) 
        self.ui.checkBox_xinyang_house.stateChanged.connect(self.search_material)
        self.ui.checkBox_zhengzhou_house_month.stateChanged.connect(self.search_material)
        self.ui.checkBox_zhengzhou_house_quarter.stateChanged.connect(self.search_material)
        self.ui.checkBox_other_house.stateChanged.connect(self.search_material)
        self.ui.checkBox_xinyang_road.stateChanged.connect(self.search_material)
        self.ui.checkBox_zhengzhou_road.stateChanged.connect(self.search_material)
        self.ui.checkBox_other_road.stateChanged.connect(self.search_material)
        # 添加下拉框信号和槽连接
        self.ui.comboBox_gushi_house_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_xinyang_house_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_zhengzhou_house_mperiod.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_zhengzhou_house_qperiod.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_other_house_qperiod.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_xinyang_road_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_zhengzhou_road_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_other_road_period.currentIndexChanged.connect(self.search_material)
        # 连接分页控件的信号和槽
        self.ui.pushButton_next.clicked.connect(self.on_next_page)
        self.ui.pushButton_previous.clicked.connect(self.on_previous_page)
        # 连接查询按钮的点击事件
        self.ui.pushButton.clicked.connect(lambda:self.search_material(reset_page=True))
        # 连接首页按钮的点击事件
        self.ui.pushButton_home.clicked.connect(self.go_to_first_page)
        self.reset_query()
        self.reset_query()
        self.search_material()
    def go_to_first_page(self):
        self.current_page = 1
        self.search_material()
    def reset_query(self):
        # 设置界面初始显示
        query_start = f"SELECT serial_number 序号, name 材料名称, specification 规格型号, unit 单位, price_excluding_tax 不含税价, note 备注, period 期数 , major 专业 FROM information_price WHERE 1=1"
        # 初始每页条数
        self.current_page=1
        self.items_per_page = 500
        self.query_model.setQuery( query_start)
        # self.search_material()
    def on_next_page(self):
        where_clause = self.build_where_clause()
        total_records = self.get_total_records(where_clause)
        if self.current_page * self.items_per_page < total_records:
            self.current_page += 1
            self.search_material()


    def on_previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.search_material()
    def get_total_records(self, where_clause):
        query = f"SELECT COUNT(*) FROM information_price WHERE {where_clause}"
        self.model.cursor.execute(query)
        return self.model.cursor.fetchone()[0]   
    
    def build_where_clause(self):
        checkBox_gushi_house_checked = self.ui.checkBox_gushi_house.isChecked()
        checkBox_xinyang_house_checked = self.ui.checkBox_xinyang_house.isChecked()
        checkBox_zhengzhou_house_month_checked = self.ui.checkBox_zhengzhou_house_month.isChecked()
        checkBox_zhengzhou_house_quarter_checked = self.ui.checkBox_zhengzhou_house_quarter.isChecked()
        checkBox_other_house_checked = self.ui.checkBox_other_house.isChecked()
        checkBox_xinyang_road_checked = self.ui.checkBox_xinyang_road.isChecked()
        checkBox_zhengzhou_road_checked = self.ui.checkBox_zhengzhou_road.isChecked()
        checkBox_other_road_checked = self.ui.checkBox_other_road.isChecked()

        gushi_house_period = self.ui.comboBox_gushi_house_period.currentText()
        xinyang_house_period = self.ui.comboBox_xinyang_house_period.currentText()
        zhengzhou_house_mperiod = self.ui.comboBox_zhengzhou_house_mperiod.currentText()
        zhengzhou_house_qperiod = self.ui.comboBox_zhengzhou_house_qperiod.currentText()
        other_house_period = self.ui.comboBox_other_house_qperiod.currentText()
        xinyang_road_period = self.ui.comboBox_xinyang_road_period.currentText()
        zhengzhou_road_period = self.ui.comboBox_zhengzhou_road_period.currentText()
        other_road_period = self.ui.comboBox_other_road_period.currentText()

        area_major_condition = []
        if checkBox_gushi_house_checked:
            area_major_condition.append(f"area = '固始' AND major = '房建' AND period = '{gushi_house_period}'")
        if checkBox_xinyang_house_checked:
            area_major_condition.append(f"area = '信阳' AND major = '房建' AND period = '{xinyang_house_period}'")
        if checkBox_zhengzhou_house_month_checked:
            area_major_condition.append(f"area = '郑州' AND major = '房建' AND period = '{zhengzhou_house_mperiod}'")
        if checkBox_zhengzhou_house_quarter_checked:
            area_major_condition.append(f"area = '郑州' AND major = '房建' AND period = '{zhengzhou_house_qperiod}'")
        if checkBox_other_house_checked:
            area_major_condition.append(f"area = '其他' AND major = '房建' AND period = '{other_house_period}'")
        if checkBox_xinyang_road_checked:
            area_major_condition.append(f"area = '信阳' AND major = '公路' AND period = '{xinyang_road_period}'")
        if checkBox_zhengzhou_road_checked:
            area_major_condition.append(f"area = '郑州' AND major = '公路' AND period = '{zhengzhou_road_period}'")
        if checkBox_other_road_checked:
            area_major_condition.append(f"area = '其他' AND major = '公路' AND period = '{other_road_period}'")
        # 从界面控件获取查询参数
        material_name = self.ui.lineEdit.text()
        where_clause_parts = []
        if area_major_condition:
            where_clause_parts.append("(" + " OR ".join(area_major_condition) + ")")
        if material_name.strip():
            keywords = material_name.strip().split()
            keyword_conditions = []
            for keyword in keywords:
                keyword_conditions.append(f"(name LIKE '%{keyword}%' OR specification LIKE '%{keyword}%')")
            where_clause_parts.append("(" + " AND ".join(keyword_conditions) + ")")
        where_clause = " AND ".join(where_clause_parts) if where_clause_parts else "1=1"
        return where_clause 
    def search_material(self,reset_page=False):
        if reset_page:
            self.current_page = 1  # 每次搜索时重置为第一页
        where_clause = self.build_where_clause()
        offset_value = (self.current_page - 1) * self.items_per_page
        query = f"""
            SELECT serial_number 序号, name 材料名称, specification 规格型号, unit 单位, 
                   price_excluding_tax 不含税价, note 备注, period 期数, major 专业 
            FROM information_price 
            WHERE {where_clause} 
            LIMIT {self.items_per_page} OFFSET {offset_value}
        """
        self.query_model.setQuery(query)
        total_records = self.get_total_records(where_clause)
        self.ui.label_total_records.setText(f"总记录数: {total_records}")
        self.ui.label_current_page.setText(f"当前页: {self.current_page}") 
                                     
   

        
if __name__ == "__main__":
    # csv2sqlite("固始信息价.csv", "materials.db")  # 导入 CSV 数据到 SQLite
    # csv2sqlite("郑州信阳信息价.csv", "materials.db")
    app = QApplication([])
    window =MyMainWindow()
    window.show()
    sys.exit(app.exec())