### docker部署

```shell
docker pull neo4j:4.4.15-community
docker run -d -p 7474:7474 -p 7687:7687 --env NEO4J_AUTH=neo4j/qwer123456 -v /home/neo4j/data:/data -v /home/neo4j/logs:/logs neo4j:4.4.15-community
```

#### 修改配置
```shell
vim conf/neo4j

// 修改dbms.connector.bolt.listen_address为:
dbms.connector.bolt.listen_address=0.0.0.0:7687  
// 修改dbms.connector.http.listen_address
dbms.connector.http.listen_address=0.0.0.0:7474

// 末尾添加
dbms.connectors.default_listen_address=0.0.0.0

// 重启容器
```