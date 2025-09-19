# 示例：将学生姓名与分数绑定输出
names = ["Alice", "Bob", "Cathy", "David"]
scores = [90, 58, 77, 100]

for name, score in zip(names, scores):
    status = "及格" if score >= 60 else "不及格"
    print(f"{name} 的分数: {score}, 状态: {status}")

# zip 会在最短序列结束时停止
# 若需要对齐长度，可结合 itertools.zip_longest 使用
