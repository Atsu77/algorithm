'''
全ビット探索
'''

'''
みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。
財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。
'''

money = 3
items = (('みかん', 100), ('りんご',  200), ("ぶどう", 300))
n = len(items)
count = 0
for i in range(2**n):
    bag = []
    total_price = 0
    for j in range(n):
        if((i >> j) & 1):
            bag.append(items[j][0])
            total_price += items[j][1]
    if (total_price <= 300):
        print(total_price, bag)
        count += 1
    
print(count)

'''
0 2 9 0 といった数字同士の隙間に + か − を入れて特定の答え（今回の場合は 7）を導き出す
'''

n = [0, 2, 9, 0]
op_cnt = len(n) - 1
for i in range(2**op_cnt):
    op = ["-"] * op_cnt
    result = 0
    for j in range(op_cnt):
        if((i >> j) & 1):
            op[op_cnt - j -1] = "+"

    formula = ''
    for p_n, p_o in zip(n, op + [""]):
        formula += (str(p_n) + p_o)
    if eval(formula) == 7:
        print(formula + '=7')