import time,datetime,struct,MySQLdb

host = 'localhost'
port = 3306
user = 'root'
passwd = '1jcsTOeast'
database = 'only_test'

timestr = "".join(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

def MysqlInsert():
	mysql_conn = MySQLdb.connect(host, user, passwd, database)
	cur = mysql_conn.cursor()
	sqlStr = 'INSERT INTO test_user'
	sqlStr = sqlStr + '(name, depart, createtime) '
	sqlStr = sqlStr + 'VALUES'
	sqlStr = sqlStr + ' (\"SARA\",\"ART\",\"%s\");'%timestr
	print sqlStr
	cur.execute(sqlStr)
	mysql_conn.commit()
	cur.close()
	mysql_conn.close()

def MysqlDelete():
    mysql_conn = MySQLdb.connect(host, user, passwd, database)
    cur = mysql_conn.cursor()
    sqlStr = 'delete from test_user where'
    sqlStr = sqlStr + ' id < 10'
    print sqlStr
    cur.execute(sqlStr)
    mysql_conn.commit()
    cur.close()
    mysql_conn.close()


if __name__ == '__main__':
    MysqlInsert()
    #MysqlDelete()