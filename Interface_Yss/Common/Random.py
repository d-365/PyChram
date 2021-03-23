import random


##随机字符串
def random_str(num):
    chinese = "诗来源于生活是大海的闪光把与隔开就无法认识诗的内容本质在古今中外涌现出了人才"
    randomStr = ''.join(random.sample(chinese, num))
    return randomStr


##生成随机整数
def random_int(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    randInt = random.randint(range_start, range_end)
    return randInt


if __name__ == "__main__":
    six = random_int(6)
    print(six)
