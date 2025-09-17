from pathlib import Path

# 定义路径（当前目录下的 data 文件夹）
data_dir = Path("data")

# 若目录不存在则创建
data_dir.mkdir(exist_ok=True)

# 在目录下创建文件并写入内容
file_path = data_dir / "example.txt"
file_path.write_text("Hello, pathlib!\nPython 路径操作更优雅。", encoding="utf-8")

# 读取文件内容
print("文件内容:")
print(file_path.read_text(encoding="utf-8"))

# 遍历目录下的所有文件
print("\n目录文件列表:")
for f in data_dir.iterdir():
    print("-", f.name)
