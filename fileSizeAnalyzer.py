import os

folder = input("enter folder path")

totalSize = round(0,2)

for file in os.listdir(folder):
    print(file)
    size = os.path.getsize(folder)
    print(size)
    totalSize += size

print(f"Total Size: {totalSize} bytes")
print(f"{totalSize / (1024 * 1024)} MB")
