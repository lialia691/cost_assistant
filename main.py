from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox,QInputDialog,QComboBox
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
import sys
import sqlite3
import csv
import json
import xml.etree.ElementTree as ET

from mainwindow import Ui_MainWindow
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
            typeperiod TEXT,
            major TEXT,          
            UNIQUE(name,specification,area,materail_date, note)
        )''')    ####名称、规格型号、地区、发布时间、备注定字段唯一性
        self.conn.commit()            

    def load_csv2db(self, csv_file):
        conn = sqlite3.connect(self.db_file, timeout=30)
        conn.execute('PRAGMA journal_mode=WAL')  
        cursor = conn.cursor()     
        try:
            with open(csv_file, 'r', encoding='gbk') as cf:
                csvreader = csv.reader(cf)
                next(csvreader)  # 跳过标题行
                for row in csvreader:         
                    self.cursor.execute("""
                    INSERT OR  REPLACE INTO information_price    
                        (serial_number, name, specification, unit, price_excluding_tax, note, area, materail_date, typeperiod, major)        
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", row)
                self.conn.commit()
        except UnicodeDecodeError:
            try:
                with open(csv_file, 'r', encoding='utf-8') as cf:
                    csvreader = csv.reader(cf)
                    next(csvreader)  # 跳过标题行
                    for row in csvreader:         
                        self.cursor.execute("""
                        INSERT OR IGNORE INTO information_price    
                            (serial_number, name, specification, unit, price_excluding_tax, note, area, materail_date, typeperiod, major)        
                        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", row)
                    self.conn.commit()
            except UnicodeDecodeError as e:
                self.conn.rollback()
                raise e
        finally:
            conn.close()
    def close_connection(self):
        self.conn.close()
    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def clear_data(self, condition):
        """
        根据条件清除数据
        :SQL条件语句，例如 "name='example'"
        """
        query = f'DELETE FROM information_price WHERE {condition}'
        self.cursor.execute(query)
        self.conn.commit()        
    def load_xml2db(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()        
        project_name = root.attrib['Name']#提取项目名称        
        materail_date=root.attrib['MaterialPriceDate'] #提取时间
        # 提取工程地址
        area = ''
        attr_info = root.find('./ConstructionInfo/AttrInfo')
        if attr_info is not None:
            for item in attr_info.findall('AttrInfoItem'):
                if item.attrib.get('Name') == '工程地址':
                    area = item.attrib.get('Value', '')
                    break
        for unit_works in root.findall('.//UnitWorks'):
            major = unit_works.attrib.get('Name', '')#提取单位工程名称

            for xml_material in unit_works.findall('./LabourMaterialsEquipmentsMachinesSummary'):
                data = {
                    'serial_number': xml_material.attrib.get('Number', ''),
                    'name': xml_material.attrib.get('Name', ''),
                    'specification': xml_material.attrib.get('Specification', ''),
                    'unit': xml_material.attrib.get('Unit', ''),
                    'price_excluding_tax': float(xml_material.attrib.get('NoTaxPrice', 0)),
                    'note': project_name,
                    'area':area,
                    'materail_date':materail_date,
                    'typeperiod':'专有',
                    'major':major
                }            
                self.cursor.execute('''
                INSERT OR REPLACE INTO information_price
                (serial_number, name, specification, unit, price_excluding_tax, note, area, materail_date, typeperiod, major)
                VALUES 
                (:serial_number, :name, :specification, :unit, :price_excluding_tax, :note, :area, :materail_date, :typeperiod, :major)
                ''', data)    
        self.conn.commit()






class CustomComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            current_index = self.currentIndex()
            if current_index != -1:
                self.removeItem(current_index)
        elif event.key() == Qt.Key_PageUp:
            self.move_current_item_to_top()
        elif event.key() == Qt.Key_PageDown:
            self.move_current_item_to_bottom()
        else:
            super().keyPressEvent(event)

    def move_current_item_to_top(self):
        current_index = self.currentIndex()
        if current_index != -1:
            item_text = self.itemText(current_index)
            self.removeItem(current_index)
            self.insertItem(0, item_text)
            self.setCurrentIndex(0)
    def move_current_item_to_bottom(self):
        current_index = self.currentIndex()
        if current_index != -1:
            item_text = self.itemText(current_index)
            self.removeItem(current_index)
            self.addItem(item_text)
            self.setCurrentIndex(self.count() - 1)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("造价助手1.1")   #设置软件名称
        self.setGeometry(100, 50, 1100, 800)    #setGeometry方法的参数分别是窗口的x坐标、y坐标、宽度和高度。
        # 创建数据库模型
        self.dtmodel = MaterialDataModel("materials.db")
        self.dtmodel.create_table()
            # 初始化当前数据库
        self.current_db = "materials.db"
        # 设置标题栏图标
        self.setWindowIcon(QIcon('image/app_icon.png'))  # 替换为你的图标路径
        # 连接到 SQLite 数据库
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.current_db)
        self.db.open()
        # 创建 QSqlQueryModel
        self.query_model  = QSqlQueryModel(self)  
        # 将模型设置到 TableView
        self.ui.tableView.setModel(self.query_model) 
        # 显示表头
        headers = ["序号", "名称", "规格型号", "单位", "不含税价", "备注", "地区", "发布时间", "类别", "专业"]
        for i, header in enumerate(headers):
            self.query_model.setHeaderData(i, Qt.Horizontal, header)
        # 添加多选框信号和槽连接
        self.ui.checkBox_gushi_house.stateChanged.connect(self.search_material) 
        self.ui.checkBox_xinyang_house.stateChanged.connect(self.search_material)
        self.ui.checkBox_zhengzhou_house_month.stateChanged.connect(self.search_material)
        self.ui.checkBox_zhengzhou_house_quarter.stateChanged.connect(self.search_material)
        self.ui.checkBox_xinyang_road.stateChanged.connect(self.search_material)
        self.ui.checkBox_zhengzhou_road.stateChanged.connect(self.search_material)
        self.ui.checkBox_other1.stateChanged.connect(self.search_material)
        self.ui.checkBox_other2.stateChanged.connect(self.search_material)

        self.ui.checkBox_personal_data.stateChanged.connect(self.search_material)


        # 替换 QComboBox 为 CustomComboBox
        self.replace_comboboxes()
        # 添加下拉框信号和槽连接
        self.ui.comboBox_gushi_house_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_xinyang_house_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_zhengzhou_house_mperiod.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_zhengzhou_house_qperiod.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_xinyang_road_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_zhengzhou_road_period.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_other1.currentIndexChanged.connect(self.search_material)
        self.ui.comboBox_other2.currentIndexChanged.connect(self.search_material)

        # 连接分页控件的信号和槽
        self.ui.pushButton_next.clicked.connect(self.on_next_page)
        self.ui.pushButton_previous.clicked.connect(self.on_previous_page)
        # 连接查询按钮的点击事件
        self.ui.pushButton.clicked.connect(lambda:self.search_material(reset_page=True))
        # 连接首页按钮的点击事件
        self.ui.pushButton_home.clicked.connect(self.go_to_first_page)
        # 连接导入数据按钮的点击事件
        self.ui.pushButton_import.clicked.connect(self.import_data)
        # 连接导出数据按钮的点击事件
        self.ui.pushButton_export.clicked.connect(self.export_data)
        # 连接导出所有数据按钮的点击事件
        self.ui.pushButton_export_all.clicked.connect(self.export_all_data)
        # 添加价格目录按钮
        self.ui.pushButton_price_catalog.clicked.connect(self.show_price_catalog)
        # 添加清除部分数据按钮
        self.ui.pushButton_clear_partial_data.clicked.connect(self.clear_partial_data)

        self.reset_query()
        self.search_material()
            # 加载保存的选项
        self.load_options()
    def replace_comboboxes(self):
        combo_boxes = [
            'comboBox_gushi_house_period',
            'comboBox_xinyang_house_period',
            'comboBox_zhengzhou_house_mperiod',
            'comboBox_zhengzhou_house_qperiod',
            'comboBox_xinyang_road_period',
            'comboBox_zhengzhou_road_period',
            'comboBox_other1',
            'comboBox_other2',
        ]        
        for combo_name in combo_boxes:
            old_combo = getattr(self.ui, combo_name)
            new_combo = CustomComboBox(self)
            # 复制原有的项目到新的 CustomComboBox
            for i in range(old_combo.count()):
                new_combo.addItem(old_combo.itemText(i))
            
            # 设置当前选中的项
            new_combo.setCurrentIndex(old_combo.currentIndex())
            
            # 替换原有的 QComboBox
            old_combo.parentWidget().layout().replaceWidget(old_combo, new_combo)
            old_combo.deleteLater()
            
            # 更新 UI 中的引用
            setattr(self.ui, combo_name, new_combo)
            
            # 重新连接信号
            new_combo.currentIndexChanged.connect(self.search_material)
        
    def closeEvent(self, event):
        # 在窗口关闭时保存选项
        self.save_options()
        event.accept()
    def load_options(self):
        try:
            with open("options.json", "r") as file:
                options = json.load(file)
                for combo_name, items in options.items():
                    combo_box = getattr(self.ui, combo_name)
                    combo_box.clear()  # 清除现有项目
                    combo_box.addItems(items)  # 按保存的顺序添加项目
        except FileNotFoundError:
            # 如果文件不存在，添加一些初始选项
            initial_options = {
                "comboBox_gushi_house_period": ["可添加", ],
                "comboBox_xinyang_house_period": ["可添加",],
                "comboBox_zhengzhou_house_mperiod": ["可添加", ],
                "comboBox_zhengzhou_house_qperiod": ["可添加", ],
                "comboBox_xinyang_road_period": ["可添加", ],
                "comboBox_zhengzhou_road_period": ["可添加", ],
                "comboBox_other1": ["可按类别添加", ],
                "comboBox_other2": ["可按类别添加", ],
            }
            for combo_name, items in initial_options.items():
                combo_box = getattr(self.ui, combo_name)
                combo_box.addItems(items)

    def save_options(self):
        options = {}
        combo_boxes = [
            "comboBox_gushi_house_period",
            "comboBox_xinyang_house_period",
            "comboBox_zhengzhou_house_mperiod",
            "comboBox_zhengzhou_house_qperiod",
            "comboBox_xinyang_road_period",
            "comboBox_zhengzhou_road_period",
            "comboBox_other1",
            "comboBox_other2",
        ]
        for combo_name in combo_boxes:
            combo_box = getattr(self.ui, combo_name)
            # 获取所有选项，包括用户输入的新选项
            options[combo_name] = [combo_box.itemText(i) for i in range(combo_box.count())]
            # 添加当前编辑的文本（如果有）
            current_text = combo_box.currentText()
            if current_text and (current_text not in options[combo_name]):
                options[combo_name].insert(0, current_text)
        with open("options.json", "w") as file:
            json.dump(options, file)
    def import_data(self):
        # 打开文件对话框选择 CSV 文件
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Data files (*.csv *.xml)")
        if file_dialog.exec():
            files = file_dialog.selectedFiles()
            try:
                for file in files:
                    if file.lower().endswith('.csv'):
                        self.dtmodel.load_csv2db(file)
                    elif file.lower().endswith('.xml'):
                        self.dtmodel.load_xml2db(file)
                    else:
                        raise ValueError(f"不支持的格式: {file}")
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
                    headers = ["序号", "名称", "规格型号", "单位", "不含税价", "备注","地区","发布时间", "类别", "专业"]
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
                data = self.dtmodel.query(query)
                
                # 写入 CSV 文件
                with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    # 写入表头
                    headers = ["序号", "名称", "规格型号", "单位", "不含税价", "备注","地区","发布时间", "类别", "专业"]
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
        query_start = f"SELECT serial_number 序号, name 名称, specification 规格型号, unit 单位, price_excluding_tax 不含税价, note 备注,area 地区,materail_date 发布时间, typeperiod 类别 , major 专业 FROM information_price WHERE 1=1"
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
        self.dtmodel.cursor.execute(query)
        return self.dtmodel.cursor.fetchone()[0]   
    
    def build_where_clause(self):
        checkBox_gushi_house_checked = self.ui.checkBox_gushi_house.isChecked()
        checkBox_xinyang_house_checked = self.ui.checkBox_xinyang_house.isChecked()
        checkBox_zhengzhou_house_month_checked = self.ui.checkBox_zhengzhou_house_month.isChecked()
        checkBox_zhengzhou_house_quarter_checked = self.ui.checkBox_zhengzhou_house_quarter.isChecked()
        checkBox_xinyang_road_checked = self.ui.checkBox_xinyang_road.isChecked()
        checkBox_zhengzhou_road_checked = self.ui.checkBox_zhengzhou_road.isChecked()
        checkBox_checkBox_other1_checked = self.ui.checkBox_other1.isChecked()
        checkBox_checkBox_other2_checked = self.ui.checkBox_other2.isChecked()
        checkBox_personal_data_checked = self.ui.checkBox_personal_data.isChecked()

        gushi_house_period = self.ui.comboBox_gushi_house_period.currentText()
        xinyang_house_period = self.ui.comboBox_xinyang_house_period.currentText()
        zhengzhou_house_mperiod = self.ui.comboBox_zhengzhou_house_mperiod.currentText()
        zhengzhou_house_qperiod = self.ui.comboBox_zhengzhou_house_qperiod.currentText()
        xinyang_road_period = self.ui.comboBox_xinyang_road_period.currentText()
        zhengzhou_road_period = self.ui.comboBox_zhengzhou_road_period.currentText()
        other1_period = self.ui.comboBox_other1.currentText()
        other2_period = self.ui.comboBox_other2.currentText()

        typeperiod_condition = []
        if checkBox_gushi_house_checked:
            typeperiod_condition.append(f"typeperiod = '{gushi_house_period}'")
        if checkBox_xinyang_house_checked:
            typeperiod_condition.append(f"typeperiod  = '{xinyang_house_period}'")
        if checkBox_zhengzhou_house_month_checked:
            typeperiod_condition.append(f"typeperiod  = '{zhengzhou_house_mperiod}'")
        if checkBox_zhengzhou_house_quarter_checked:
            typeperiod_condition.append(f"typeperiod = '{zhengzhou_house_qperiod}'")
        if checkBox_xinyang_road_checked:
            typeperiod_condition.append(f"typeperiod  = '{xinyang_road_period}'")
        if checkBox_zhengzhou_road_checked:
            typeperiod_condition.append(f"typeperiod = '{zhengzhou_road_period}'")
        if checkBox_checkBox_other1_checked:
            typeperiod_condition.append(f"typeperiod = '{ other1_period}'")
        if checkBox_checkBox_other2_checked:
            typeperiod_condition.append(f"typeperiod = '{ other2_period}'")        
        if checkBox_personal_data_checked:
            typeperiod_condition.append("typeperiod = '专有'")

        # 从界面控件获取查询参数
        material_keywords = self.ui.lineEdit.text().strip().split()
        typeperiod_keywords = self.ui.lineEdit_period_keywords.text().strip().split() 
        where_clause_parts = []
        if typeperiod_condition:
            where_clause_parts.append("(" + " OR ".join(typeperiod_condition) + ")")
        if material_keywords:
            material_conditions = []
            for keyword in material_keywords:
                material_conditions.append(f"(name LIKE '%{keyword}%' OR specification LIKE '%{keyword}%')")
            where_clause_parts.append("(" + " AND ".join(material_conditions) + ")")  #搜索名称、项目特征关键词
        if typeperiod_keywords:
            period_conditions = []
            for period_keyword in typeperiod_keywords:
                period_conditions.append(f"(typeperiod  LIKE '%{period_keyword}%')")
            where_clause_parts.append("(" + " OR ".join( period_conditions) + ")")
        where_clause = " AND ".join(where_clause_parts) if where_clause_parts else "1=1"
        return where_clause 
    def search_material(self,reset_page=False):
        if reset_page:
            self.current_page = 1  # 每次搜索时重置为第一页
        where_clause = self.build_where_clause()
        offset_value = (self.current_page - 1) * self.items_per_page
        query = f"""
            SELECT serial_number 序号, name 名称, specification 规格型号, unit 单位, 
                   price_excluding_tax 不含税价, note 备注, area 地区,materail_date 发布时间,typeperiod 类别, major 专业 
            FROM information_price 
            WHERE {where_clause} 
            LIMIT {self.items_per_page} OFFSET {offset_value}
        """
        self.query_model.setQuery(query)
        total_records = self.get_total_records(where_clause)
        self.ui.label_total_records.setText(f"总记录数: {total_records}")
        self.ui.label_current_page.setText(f"当前页: {self.current_page}") 
                                     
#----------------------------------------------------------------------------
#添加价格目录
    def show_price_catalog(self):
        query = "SELECT DISTINCT area, typeperiod, materail_date FROM information_price ORDER BY area"
        self.dtmodel.cursor.execute(query)
        results = self.dtmodel.cursor.fetchall()
        details = [f"{area}: {typeperiod} - {materail_date}" for area, typeperiod, materail_date in results]
        QMessageBox.information(self, "价格目录", "\n".join(details))
    def clear_partial_data(self):
        column_mapping = {
            "名称": "name",
            "规格型号": "specification",
            "单位":"unit",
            "不含税价":"price_excluding_tax",
            "备注":"note",
            "地区":"area",
            "发布时间":"materail_date",
            "类别":"typeperiod",
            "专业": "major",
        }
        # 获取用户输入的条件
        condition, ok = QInputDialog.getText(self, "清除指定数据", "请输入清除条件（例如类别='专有'）:")
        if ok and condition:
            for chinese_name, english_name in column_mapping.items():
                condition = condition.replace(chinese_name, english_name)
            try:
                self.dtmodel.clear_data(condition)
                QMessageBox.information(self, "成功", "数据清除成功")
                self.search_material(reset_page=True)  # 重新加载数据
            except Exception as e:
                QMessageBox.critical(self, "错误", f"数据清除失败: {e}")


def start():
    app = QApplication([])
    app.setStyle('WindowsVista')  # 设置为 Windows Vista 风格
    window =MyMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    start()