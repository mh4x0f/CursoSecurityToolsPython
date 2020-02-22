import json
# exempo de JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# convertendo x:
y = json.loads(x)
print(y.keys())

# o resultado é um objeto dicionário 
print(y['age'])
