import json
# python dict
x = {
"name": "John",
"age": 30,
"city": "New York"
}
y = json.dumps(x)# convertendo para JSON:
# o resultado é uma stringjson:
print(y)
