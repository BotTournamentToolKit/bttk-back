from random import randint

# properties
matches_count = 0
ans = 0

# read
file = open("field.txt", "r")
matches_count = int(file.read())
file.close()

# solve
if matches_count % 4 == 0:
    ans = randint(1, 3)
else:
    ans = matches_count % 4

# write
file = open("turn.txt", "w")
file.write(str(ans))
file.close()
