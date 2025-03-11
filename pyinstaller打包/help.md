```shell
# 安装
pip install -U pyinstaller

# 打包命令
# 添加数据文件:
# # # --add-data "../data/d0.csv:data: 将本地文件../data/d0.cv打包到应用程序sys._MEIPASS/data目录下
# # # --add-data "../extra:data": 将本地目录../extra下所有文件打包到应用程序sys._MEIPASS/data目录下
pyinstaller --onefile --add-data "../data/d0.csv:data"  --add-data "../extra:data" app.py
```