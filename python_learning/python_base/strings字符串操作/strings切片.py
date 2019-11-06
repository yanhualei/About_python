# 字符串各种操作方法的学习与理解
str1 = "Ast123inrgstringlearningstarlearningtendxuexB"
# ---------------------------------------------------------------------------------------
print("字符串是否由字母或者数字组成:", str1.isalnum())  # 字符串至少有一个字符，并且所有字符都是字母或者数字，则返回True
print("str1是否只包含空格:", str1.isspace())  # 字符串只包含空格，则返回True
print("字符串是否全是字母:",str1.isalpha())  # 字符串至少有一个字符，并且所有字符都是字母，则返回True

print("字符串首字母是否都大写:", str1.istitle()) # 字符串是否标题化(每个单词的首字母大写)，则返回True
print("字符串是否全部小写:", str1.islower())  # 字符串全部为小写，返回True
print("字符串是否全部大写:",str1.isupper())  # 字符串全部大写，返回True
# ————————————————————————————————————————————
# 查找和替换
str2 = "learning"
print("检查str1是否以A开头，是则返回True：",str1.startswith("A"))
print("检查str1是否以B结尾，是则返回True：",str1.endswith("B"))
print("检查str2是否包含在str1中，是则返回对应的索引值,不是返回-1:",str1.find(str2))
print("将r全部替换为R：", str1.replace("r", "R", str1.count("r")))#
# ————————————————————————————————————————————
# 大小写字母转换
str4 = "study hard and make progress every day"
print("将str4每个首字母大写：",str4.title())
print("将str4全部小写：",str4.lower())
print("将str4全部大写：",str4.upper())
print("将str4大小写翻转：",str4.swapcase())
# ————————————————————————————————————————————
# 去除空白字符
str5 = "    梦想从这里起飞     "
print("str5:",str5)
print("str5去除两边的空格:",str5.strip())
# ————————————————————————————————————————————
# 拆分和连接
str6 = "1+2+3+4+5+6+7"
print("拆分str6：", str6.split("+"))  # 拆分结果为一个LIST
print("重新以-的方式组合：", "-".join(str6.split(("+"))))  # 可是对list和tuple操作，对字典只能操作keys

# ————————————————————————————————————————————
# 字符串的切片操作
num_str = "0123456789"
# 1. 截取从 2 ~ 5 位置 的字符串
print("截取从 2 ~ 5 位置 的字符串:", num_str[2:6])
# 2. 截取从 2 ~ 末尾 的字符串
print("截取从 2 ~ 末尾 的字符串:", num_str[2:])
# 3. 截取从 开始 ~ 5 位置 的字符串
print("截取从 开始 ~ 5 位置 的字符串:", num_str[0:6])
# 4. 截取完整的字符串
print("截取完整的字符串:", num_str[:])
# 5. 从开始位置，每隔一个字符截取字符串
print("从开始位置，每隔一个字符截取字符串:", num_str[::2])
# 6. 从索引 1 开始，每隔一个取一个
print("从索引 1 开始，每隔一个取一个:", num_str[1::2])
# 7. 截取从 2 ~ 末尾 - 1 的字符串
print("截取从第一个元素开始截取到最后一个字符串结束，但不包括第一个和最后一个元素 的字符串:", num_str[1:-1])
# 8. 截取字符串末尾两个字符
print("截取字符串末尾两个字符:", num_str[-2:])
# 9. 字符串的逆序（面试题）
print("字符串的逆序（面试题）:", num_str[::-1])

# 切片可同时从正序，逆序切，步长的正负由第一位决定，步长为正从左向右切，步长为负从右向左切
print("",num_str[0:-8:1])  # 从序列的第一个元素开始，切取到序列倒序index=8的元素，步长为1





