优化方向:增加ai界面
 nuitka --standalone --windows-disable-console --mingw64 --nofollow-imports --show-memory --show-progress --enable-plugin=pyside6 --include-data-files=mainwindow.ui=mainwindow.ui --include-data-files=image/app_icon.png=image/app_icon.png --include-data-files=materials.db=materials.db --output-dir=o main.py
价格助手1.0
一、项目简介
价格助手是一个桌面应用程序，用于管理和查询材料价格信息,包含信息价和市场价。用户可以通过导入 CSV 文件将数据加载到数据库中，并通过多种条件进行查询和导出数据。
二、使用方法
1、查询数据
通过勾选多选框和选择下拉框中的选项来设置查询条件。
点击“查询”按钮进行查询。
查询结果将显示在表格中。
2、导入数据
点击“导入数据”按钮。
选择要导入的 CSV 文件。
数据将被加载到数据库中，并显示在表格中。
3、导出数据
点击“导出数据”按钮。
选择保存位置和文件名。
当前查询结果将导出为 CSV 文件。
4、导出所有数据
点击“导出所有数据”按钮。
选择保存位置和文件名。
所有数据将导出为 CSV 文件。