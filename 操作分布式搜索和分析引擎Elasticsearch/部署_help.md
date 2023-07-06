### docker单机部署

1. pull

```shell
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.11.2 
docker pull docker.elastic.co/kibana/kibana:7.11.2
```

2. docker compose

```yaml
version: "3.8"
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.11.2
    ports:
      - "9200:9200"
      - "9300:9300"
    environment:
      discovery.type: single-node
    volumes:
      - data01:/usr/share/elasticsearch/data
    networks:
      - overlay

  kibana:
    image: docker.elastic.co/kibana/kibana:7.11.2
    ports:
      - "5601:5601"
    environment:
      ELASTICSEARCH_HOSTS: '["http://elasticsearch:9200"]'  # kibana默认值
    depends_on:
      - elasticsearch
    networks:
      - overlay

volumes:
  data01:

networks:
  overlay:
```