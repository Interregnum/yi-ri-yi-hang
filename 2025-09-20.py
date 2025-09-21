# 示例：检查学生成绩是否达标
scores = [85, 92, 77, 61, 58]

# 判断是否所有学生都及格
all_passed = all(score >= 60 for score in scores)
print("所有学生都及格:", all_passed)

# 判断是否至少有一名学生满分
has_full = any(score == 100 for score in scores)
print("是否有学生满分:", has_full)

# 判断是否有学生不及格
has_failed = any(score < 60 for score in scores)
print("是否有学生不及格:", has_failed)
# 示例：检查学生成绩是否达标
scores = [85, 92, 77, 61, 58]

# 判断是否所有学生都及格
all_passed = all(score >= 60 for score in scores)
print("所有学生都及格:", all_passed)

# 判断是否至少有一名学生满分
has_full = any(score == 100 for score in scores)
print("是否有学生满分:", has_full)

# 判断是否有学生不及格
has_failed = any(score < 60 for score in scores)
print("是否有学生不及格:", has_failed)
