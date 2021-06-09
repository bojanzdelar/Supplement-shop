from flaskext.mysql import MySQL, pymysql

mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
