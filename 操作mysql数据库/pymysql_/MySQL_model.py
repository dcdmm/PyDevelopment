import pymysql


class MysqlDB:
    def __init__(self, host, password, database, user='root', port=3306, charset='utf8'):
        # Host where the database server is located.
        self.host = host
        # Password to use.
        self.password = password
        # Database to use, None to not use a particular one.
        self.database = database
        # Username to log in as. (default: 'root')
        self.user = user
        # MySQL port to use, default is usually OK. (default: 3306)
        self.port = port
        # Charset to use. (default: 'utf8')
        self.charset = charset
        # Establish a connection to the MySQL database
        self.connector = pymysql.connect(host=host, user=user, password=password, db=database, port=port,
                                         charset=charset)

    def fetch_data(self, sql):
        """
        获取数据---查询操作

        Parameters
        ---------
        sql : str
            MySQL语句

        Returns
        -------
        data : tuple
            查询结果
        columns: list
            查询结果的列名
        """
        cur = self.connector.cursor()
        # Execute a query.
        # Returns:  Number of affected rows.
        row_count = cur.execute(sql)
        print(row_count, " of affected rows!")
        # Fetch all the rows.
        data = cur.fetchall()
        columns = [col[0] for col in cur.description]
        cur.close()
        return data, columns

    def change_data(self, sql, args=None):
        """
        修改数据---增、删、改

        Parameters
        ---------
        sql : str
            MySQL语句

        args : tuple list
            其Sequence of sequences or mappings. It is used as parameter.
        """
        cur = self.connector.cursor()
        self.connector.ping(reconnect=True)
        row_count = cur.execute(sql, args=args)
        # print(row_count, " of affected rows!")
        # Commit changes to stable storage
        self.connector.commit()
        cur.close()

    def change_many_data(self, sql, args, batch_size=None):
        """
        批量修改数据---批量增、删、改

        Parameters
        ---------
        sql : str
            MySQL语句(使用%s作为占位符)

        args : list[tuple]
            参数列表,每个元素为一条记录对应的参数元组

        batch_size : int, optional
            每批次处理的记录数,默认None表示一次性处理全部
        """
        cur = self.connector.cursor()
        self.connector.ping(reconnect=True)
        if batch_size is None:
            cur.executemany(sql, args)
        else:
            for i in range(0, len(args), batch_size):
                cur.executemany(sql, args[i:i + batch_size])
        self.connector.commit()
        cur.close()

    def close_con(self):
        """关闭数据连接"""
        self.connector.close()

    def rollback(self):
        """Roll back the current transaction"""
        self.connector.rollback()
