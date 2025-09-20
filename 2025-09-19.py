from collections import Counter

# 示例：统计文本中字符出现频率
text = "python makes coding fun and pythonic"
counter = Counter(text.replace(" ", ""))  # 去掉空格统计字符

# 输出每个字符出现次数
print("字符统计结果:")
for char, count in counter.items():
    print(f"{char}: {count}")

# 找出出现最多的 3 个字符
print("\n出现最多的 3 个字符:")
for char, count in counter.most_common(3):
    print(f"{char}: {count}")
