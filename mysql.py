# MySQLdbのインポート
import MySQLdb
 
# データベースへの接続とカーソルの生成
connection = MySQLdb.connect(
    host='localhost',
    user='tsutsutaku',
    passwd='P0c0i224.',
    db='news')
cursor = connection.cursor()
 
# ここに実行したいコードを入力します
 

cursor.execute("""SELECT * FROM students""")

for row in cursor:
    print(row)
# 保存を実行
connection.commit()
 
# 接続を閉じる
connection.close()