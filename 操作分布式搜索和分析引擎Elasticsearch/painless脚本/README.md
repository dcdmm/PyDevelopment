### 主要参考

* Painless Scripting Language(https://www.elastic.co/guide/en/elasticsearch/reference/7.11/modules-scripting-painless.html)
* Accessing document fields and special variables(https://www.elastic.co/guide/en/elasticsearch/reference/7.11/modules-scripting-fields.html)


### painless脚本获取"content"字段(text类型)数据:
* doc-values:
```markdown
"mappings": {
    "properties": {
        "content": {
            "type": "text"
        }
    }
}
"script": {
    "source": """
    doc['content'].value # 报错
    """""
}


修改如下:
"mappings": {
    "properties": {
        "content": {
            "type": "text",
            "fields": {
                "raw": {
                    "type": "keyword"
                }
            }
        }
    }
}

"script": {
    "source": """
    doc['content.raw'].value # 此时正确
    """""
}
```

* _source(Accessing the _source field is much slower than using doc-values):
```markdown
"mappings": {
    "properties": {
        "content": {
            "type": "text"
        }
    }
}

"script": {
    "source": """
    params._source.content # 正确
    """""
}
```

