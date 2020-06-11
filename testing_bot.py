with open("field.txt", "r") as f:
    n = f.read()

k = str(int(n) + 1)

with open("turn.txt", "w") as f:
    f.write(k)
