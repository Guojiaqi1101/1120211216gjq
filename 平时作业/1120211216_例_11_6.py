def isTriangle(a, b, c):
	result = ""
	if a > 0 and b > 0 and c > 0:
		if a + b > c and a + c > b and b + c > a:
			if a == b and b == c:
				result ="等边三角形"
			elif a == b or b == c or a == c:
				result ="等腰三角形"
			elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
				result ="直角三角形"
			else:
				result ="普通三角形"
		else:
			result = "不能构成三角形"
	else:
		result ="错误的，三个边长必须为正数"
	return result
while True:
	a = eval(input("请输入一个数字a:"))
	b = eval(input("请输入一个数字b:"))
	c = eval(input("请输入一个数字c:"))
	result = isTriangle(a, b, c)
	print("a:{}, b:{},c:{}三条边构成的形状是{}".format(a, b, c, result))
