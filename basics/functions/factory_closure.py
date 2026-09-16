def temp1(num):
    def temp2(x):
        return x ** num
    return temp2

func1 = temp1(2)
func2 = temp1(3)

print(func1(2))
print(func1(3))