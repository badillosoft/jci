import sys
import json

data = json.loads(sys.argv[1])

a = float(data["a"])
b = float(data["b"])

print(a + b)

