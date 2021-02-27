#CalBMIv3.py
height,weight = eval(input("请输入身高(m)和体重(kg),用英文逗号隔开："))
print(height,weight)
BMI= weight / pow(height,2)

print("BMI数值为:{:.2f}".format(BMI))
cn,world='',''
if BMI<18.5:
    cn,world = "偏瘦","偏瘦"
elif 18.5<=BMI<=24:
    cn,world = '正常','正常'
elif 24<=BMI<25:
    cn,world = '偏胖','正常'
elif 25<=BMI<28:
    cn,world='偏胖','偏胖'
elif 28<=BMI<30:
    cn,world='肥胖','偏胖'
else:
    cn,world='肥胖','肥胖'
print("BMI指标为：国内'{0}',国际'{1}'".format(cn,world))
input('Press <Enter>')
