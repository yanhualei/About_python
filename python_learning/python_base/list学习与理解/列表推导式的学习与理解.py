
y = [[x for x in range(1,101)][i:i+3] for i in range(0,100,3)]

for a in y:
    print(a)

# 看着挺长的一句代码，别怕，兄弟，我们来拆一下就明白了
# [x for x in range(1,101)]  # 生成一个[1,2,3......100]的列表
# [i:i+3] for i in range(0,100,3)  # 这一句代码主要就是切片作用

# 所以我们这个列表推导式实现的功能就是：将1-100每搁3个元素切片一次