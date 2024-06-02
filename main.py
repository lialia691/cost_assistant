from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
import sys
import sqlite3
import csv
class MaterialDataModel():
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file, timeout=30)
        self.conn.execute('PRAGMA journal_mode=WAL')  # 使用 WAL 模式
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
            area TEXT,
            materail_date DATE,                
            period TEXT,
            major TEXT,          
            UNIQUE(name,specification,period)
        )''')
        self.conn.commit()            

    def load_csv2db(self,csv_file):
        conn = sqlite3.connect(self.db_file, timeout=30)
        conn.execute('PRAGMA journal_mode=WAL')  
        cursor = conn.cursor()     
        with open(csv_file, 'r', encoding='gbk') as cf:
            csvreader = csv.reader(cf)
            next(csvreader)  # 跳过标题行
            try:
                for row in csvreader:         
                    self.cursor.execute("""
                    INSERT OR IGNORE INTO information_price    
                        (serial_number, name, specification, unit, price_excluding_tax, note,area, materail_date,period, major)        
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", row)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                raise e
            finally:
                conn.close()
    def close_connection(self):
        self.conn.close()
    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

uiLoader = QUiLoader()
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("价格助手")
        self.setGeometry(100, 50, 1100, 800)    #setGeometry方法的参数分别是窗口的x坐标、y坐标、宽度和高度。
      
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
        # 将模型设置到 TableView
        self.ui.tableView.setModel(self.query_model) 
        # 添加多选框信号和槽连接
        self.ui.checkBox_gushi_house.stateChanged.connect(self.search_material) 
        self.ui.checkBox_xinyang_house.stateChanged.connect(self.search_material)
        self.ui.checkBox_zhengzhou_house_month.stateChanged.connect(self.search_material)
        self.ui.checkBox_zhengzhou_house_quarter.stateChanged.connect(self.search_material)
        self.ui.checkBox_xinyang_road.stateChanged.connect(self.search_material)
        self.ui.checkBox_zhengzhou_road.stateChanged.connect(self.search_material)
        self.ui.checkBox_personal_data.stateChanged.connect(self.search_material)
        # 添加下拉框信号和槽连接
        self.ui.comboBox_gushi_house_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_xinyang_house_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_zhengzhou_house_mperiod.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_zhengzhou_house_qperiod.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_xinyang_road_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_zhengzhou_road_period.currentIndexChanged.connect(self.search_material)
        # 连接分页控件的信号和槽
        self.ui.pushButton_next.clicked.connect(self.on_next_page)
        self.ui.pushButton_previous.clicked.connect(self.on_previous_page)
        # 连接查询按钮的点击事件
        self.ui.pushButton.clicked.connect(lambda:self.search_material(reset_page=True))
        # 连接首页按钮的点击事件
        self.ui.pushButton_home.clicked.connect(self.go_to_first_page)
        # self.reset_query()       
        # self.search_material()
        # 连接导入数据按钮的点击事件
        self.ui.pushButton_import.clicked.connect(self.import_data)
        # 连接导出数据按钮的点击事件
        self.ui.pushButton_export.clicked.connect(self.export_data)
        # 连接导出所有数据按钮的点击事件
        self.ui.pushButton_export_all.clicked.connect(self.export_all_data)
        self.reset_query()
        self.search_material()
    def import_data(self):
        # 打开文件对话框选择 CSV 文件
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("CSV files (*.csv)")
        if file_dialog.exec():
            csv_files = file_dialog.selectedFiles()
            try:
                for csv_file in csv_files:
                    self.model.load_csv2db(csv_file)
                QMessageBox.information(self, "成功", "数据导入成功")
                self.search_material(reset_page=True)  # 重新加载数据
            except Exception as e:
                QMessageBox.critical(self, "错误", f"数据导入失败: {e}")
    def export_data(self):
        # 打开文件对话框选择保存位置
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("CSV files (*.csv)")
        file_dialog.setDefaultSuffix("csv")
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            try:
                # 获取当前查询的数据
                query = self.query_model.query()
                query.exec()
                data = []
                while query.next():
                    row = []
                    for i in range(query.record().count()):
                        row.append(query.value(i))
                    data.append(row)
                
                # 写入 CSV 文件
                with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    # 写入表头
                    headers = ["序号", "材料名称", "规格型号", "单位", "不含税价", "备注","地区","发布时间", "期数", "专业"]
                    csvwriter.writerow(headers)
                    # 写入数据
                    csvwriter.writerows(data)
                
                QMessageBox.information(self, "成功", "数据导出成功")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"数据导出失败: {e}")
    def export_all_data(self):
        # 打开文件对话框选择保存位置
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("CSV files (*.csv)")
        file_dialog.setDefaultSuffix("csv")
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            try:
                # 获取所有数据
                query = "SELECT * FROM information_price"
                data = self.model.query(query)
                
                # 写入 CSV 文件
                with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    # 写入表头
                    headers = ["序号", "材料名称", "规格型号", "单位", "不含税价", "备注","地区","发布时间", "期数", "专业"]
                    csvwriter.writerow(headers)
                    # 写入数据
                    csvwriter.writerows(data)
                
                QMessageBox.information(self, "成功", "所有数据导出成功")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"所有数据导出失败: {e}")
    def go_to_first_page(self):
        self.current_page = 1
        self.search_material()
    def reset_query(self):
        # 设置界面初始显示
        query_start = f"SELECT serial_number 序号, name 材料名称, specification 规格型号, unit 单位, price_excluding_tax 不含税价, note 备注,area 地区,materail_date 发布时间, period 期数 , major 专业 FROM information_price WHERE 1=1"
        # 初始每页条数
        self.current_page=1
        self.items_per_page = 500
        self.query_model.setQuery( query_start)
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
        checkBox_xinyang_road_checked = self.ui.checkBox_xinyang_road.isChecked()
        checkBox_zhengzhou_road_checked = self.ui.checkBox_zhengzhou_road.isChecked()
        checkBox_personal_data_checked = self.ui.checkBox_personal_data.isChecked()

        gushi_house_period = self.ui.comboBox_gushi_house_period.currentText()
        xinyang_house_period = self.ui.comboBox_xinyang_house_period.currentText()
        zhengzhou_house_mperiod = self.ui.comboBox_zhengzhou_house_mperiod.currentText()
        zhengzhou_house_qperiod = self.ui.comboBox_zhengzhou_house_qperiod.currentText()
        xinyang_road_period = self.ui.comboBox_xinyang_road_period.currentText()
        zhengzhou_road_period = self.ui.comboBox_zhengzhou_road_period.currentText()

        area_major_condition = []
        if checkBox_gushi_house_checked:
            area_major_condition.append(f"area = '固始' AND major = '房建' AND period = '{gushi_house_period}'")
        if checkBox_xinyang_house_checked:
            area_major_condition.append(f"area = '信阳' AND major = '房建' AND period = '{xinyang_house_period}'")
        if checkBox_zhengzhou_house_month_checked:
            area_major_condition.append(f"area = '郑州' AND major = '房建' AND period = '{zhengzhou_house_mperiod}'")
        if checkBox_zhengzhou_house_quarter_checked:
            area_major_condition.append(f"area = '郑州' AND major = '房建' AND period = '{zhengzhou_house_qperiod}'")
        if checkBox_xinyang_road_checked:
            area_major_condition.append(f"area = '信阳' AND major = '公路' AND period = '{xinyang_road_period}'")
        if checkBox_zhengzhou_road_checked:
            area_major_condition.append(f"area = '郑州' AND major = '公路' AND period = '{zhengzhou_road_period}'")
        if checkBox_personal_data_checked:
            area_major_condition.append("period = '私有'")
        # 从界面控件获取查询参数
        material_keywords = self.ui.lineEdit.text().strip().split()
        period_keywords = self.ui.lineEdit_period_keywords.text().strip().split() 
        where_clause_parts = []
        if area_major_condition:
            where_clause_parts.append("(" + " OR ".join(area_major_condition) + ")")
        if material_keywords:
            material_conditions = []
            for keyword in material_keywords:
                material_conditions.append(f"(name LIKE '%{keyword}%' OR specification LIKE '%{keyword}%')")
            where_clause_parts.append("(" + " AND ".join(material_conditions) + ")")  #搜索材料名称、项目特征关键词
        if period_keywords:
            period_conditions = []
            for period_keyword in period_keywords:
                period_conditions.append(f"(period LIKE '%{period_keyword}%')")
            where_clause_parts.append("(" + " OR ".join( period_conditions) + ")")
        where_clause = " AND ".join(where_clause_parts) if where_clause_parts else "1=1"
        return where_clause 
    def search_material(self,reset_page=False):
        if reset_page:
            self.current_page = 1  # 每次搜索时重置为第一页
        where_clause = self.build_where_clause()
        offset_value = (self.current_page - 1) * self.items_per_page
        query = f"""
            SELECT serial_number 序号, name 材料名称, specification 规格型号, unit 单位, 
                   price_excluding_tax 不含税价, note 备注, area 地区,materail_date 发布时间,period 期数, major 专业 
            FROM information_price 
            WHERE {where_clause} 
            LIMIT {self.items_per_page} OFFSET {offset_value}
        """
        self.query_model.setQuery(query)
        total_records = self.get_total_records(where_clause)
        self.ui.label_total_records.setText(f"总记录数: {total_records}")
        self.ui.label_current_page.setText(f"当前页: {self.current_page}") 
                                     
   

        
if __name__ == "__main__":
    app = QApplication([])
    window =MyMainWindow()
    window.show()
    sys.exit(app.exec())