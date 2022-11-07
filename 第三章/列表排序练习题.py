heights=[]
heights.append(178.9,)
heights.append(187.9,)
heights.append(166)
heights.append(166)
heights.append(178.3)
print(heights)
print(type(heights[2]))
print(type(heights[0]))


print("统计人数：",len(heights))
print(f'列表里面有{len(heights)}个值')
heights.sort(reverse=True)
#上面一步直接改变了heights，也可以直接打印print(heights.sort(reverse=True))
print(heights)