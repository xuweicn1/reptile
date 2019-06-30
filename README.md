[toc]

# 爬虫方法

## DuiTang

- duitang_find:find查找链接

```
label = urllib.parse.quote(label)  # 中文转url编码
while page.find(startpart, end) != -1
```
- duitang_json:结构化查找

## LaGou

- lagou-sqlite：数据保存sqlite
- lagou-mongo：数据保存mongodb
- getthreading：多线程查询
- getmultiprocessing：多进程查询