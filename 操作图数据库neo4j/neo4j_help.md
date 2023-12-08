### 社区版docker单机部署

```shell
docker pull neo4j:4.4.15-community

docker run -d -p 7474:7474 -p 7687:7687 --env NEO4J_AUTH=neo4j/qwer123456 
-v /home/neo4j/data:/data
-v /home/neo4j/logs:/logs
-v /home/neo4j/conf:/var/lib/neo4j/conf 
-v /home/neo4j/import:/var/lib/neo4j/import 
neo4j:4.4.15-community
```

### Cypher语法参考

#### 支持的数据类型:

* 字符串
* 数值:整形/浮点型
* 布尔值:True/False
* 字符串列表
* 数值列表:[1.4, 12.4, 51]
* 布尔值列表

* https://neo4j.com/docs/cypher-cheat-sheet/5/auradb-enterprise#_equijoins
* https://neo4j.com/docs/cypher-manual/current/introduction/