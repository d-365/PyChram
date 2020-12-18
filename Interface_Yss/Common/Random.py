import random

##随机字符串
def random_str(num):
    chinese = "诗来源于生活诗是生活大海的闪光。把诗与生活隔开就无法认识诗的内容本质在古今中外涌现出了许许\
              诗的范围是全部的生活和自然诗人观照森罗万象他的观照是如同思想家对这些森罗万象的概念一样多方面\
              有生活的地方就有诗的歌唱诗的领域象生活一样广阔无垠"
    randomStr = ''.join(random.sample(chinese, num))
    return randomStr

##生成随机整数
def random_int(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    randInt = random.randint(range_start, range_end)
    return randInt
