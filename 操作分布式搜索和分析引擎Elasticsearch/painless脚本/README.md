Accessing document fields and special variables(参考: https://www.elastic.co/guide/en/elasticsearch/reference/7.11/modules-scripting-fields.html)

### funnction_score查询时script_score/script中获取"content"字段(text类型)数据:
* 方式一:
```markdown
"mappings": {
    "properties": {
        "content": {
            "type": "text"
        }
    }
}
doc['content'].value // 报错

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
doc['content.raw'].value // 此时正确
```

* 方式二(推荐使用方式一;Accessing the _source field is much slower than using doc-values. ):
```markdown
"mappings": {
    "properties": {
        "content": {
            "type": "text"
        }
    }
}
params._source.content // 正确
```

