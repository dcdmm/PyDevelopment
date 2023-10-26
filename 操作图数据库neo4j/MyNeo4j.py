from neo4j import GraphDatabase


class MyNeo4j:

    def __init__(self, uri, user, password, database=None):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.database = database

    def close_cons(self):
        """关闭数据连接"""
        self.driver.close()

    def execute_query(self, query):
        """执行cypher查询,并返回结果"""
        query_result = self.driver.execute_query(query, database_=self.database)
        return query_result


if __name__ == "__main__":
    uri = "neo4j://localhost:7687"
    user = "neo4j"
    password = "qwe3r123456"
    database = "neo4j"  # 数据库名称
    app = MyNeo4j(uri, user, password, database)
    app.close_cons()
