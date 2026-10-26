with open("source.txt", "r") as f1:
    data = f1.read()

with open("destination.txt", "w") as f2:
    f2.write(data)

print("Contents copied successfully to destination.txt")