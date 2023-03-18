### docker部署

```shell
docker pull neo4j:4.4.15-community

docker run -d -p 7474:7474 -p 7687:7687 --env NEO4J_AUTH=neo4j/qwer123456 
-v /home/neo4j/data:/data
-v /home/neo4j/logs:/logs
-v /home/neo4j/conf:/var/lib/neo4j/conf 
-v /home/neo4j/import:/var/lib/neo4j/import 
neo4j:4.4.15-community
```