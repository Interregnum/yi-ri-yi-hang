# 示例：统计分数及标记不及格的学生
scores = [88, 59, 73, 100, 45]

for idx, score in enumerate(scores, start=1):  # start=1 让索引从 1 开始
    status = "通过" if score >= 60 else "不及格"
    print(f"第 {idx} 位学生：分数={score}, 状态={status}")

# 传统写法 range(len(...)) 容易出错，可读性差
