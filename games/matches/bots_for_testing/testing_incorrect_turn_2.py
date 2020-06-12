# read
file = open("field.txt", "r")
matches_count = int(file.read())
file.close()

# write
file = open("turn.txt", "w")
file.write(str(matches_count + 1))
file.close()
