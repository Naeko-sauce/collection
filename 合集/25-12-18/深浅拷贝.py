# 深浅拷贝是用来复制对象的
# 浅拷贝只会复制一层
# 深拷贝完整的复制整个对象
# ----
# 浅拷贝，引入内部模块
import copy
list = [1,2,3,4,5,6,7,8,9]

copy_list = copy.copy(list)

copy_list.append(999)
list[4] =1212
print(f"原来的列表{list}",id(list))
print(f"浅拷贝列表{copy_list}",id(copy_list))
# ----
# 深拷贝，引入内部模块
import copy
list1 = [1,2,3,4,5,6,7,8,9]

copy_list1 = copy.deepcopy(list1)

copy_list1.append(999)
list1[6] =121
print(f"原来的列表{list1}",id(list1))
print(f"深拷贝列表{copy_list1}",id(copy_list1))