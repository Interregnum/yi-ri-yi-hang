from itertools import groupby
from operator import itemgetter

# 示例数据：(类别, 金额)
orders = [
    ("book", 12.9),
    ("toy", 30.0),
    ("book", 22.1),
    ("food", 8.5),
    ("toy", 15.0),
    ("food", 20.0),
    ("book", 13.0),
]

orders.sort(key=itemgetter(0))  # 关键点：先按类别排序，确保 groupby 正确分组

stats = []  # 收集聚合结果：(类别, 数量, 总额)
for cat, group in groupby(orders, key=itemgetter(0)):
    count, total = 0, 0.0
    for _, amount in group:  # 遍历当前类别的一组条目
        count += 1
        total += amount
    stats.append((cat, count, round(total, 2)))

# 按总额降序输出结果
for cat, count, total in sorted(stats, key=itemgetter(2), reverse=True):
    print(f"{cat:<5}  count={count:<2}  total={total}")
