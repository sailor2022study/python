grade = 70

data = [60, 70, 80, 90, 100]
print("是否及格：", grade >= 60)
print("是否不及格：", grade <= 60)
print("是否等于100：", grade==100)
print("是否不满分：", grade!=100)
print("是否属于中等成绩：", grade>=70 and grade<= 90)
print("是否成绩很顺口：", grade==66 or grade==77 or grade==88)
print("判断成绩是否及格并且是否是0结尾：", grade>=60 and grade in data )