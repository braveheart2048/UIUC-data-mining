"""Apriori算法中用到的子函数放在这里"""

"""
计算t_FP的support
"""
def get_sup(t_FP, read_path):
    sup = 0
    s = t_FP.split(";")
    with read_path.open("r", encoding="utf-8") as f:
        for line in f:
            itemsets = line.strip().split(";")
            if set(s).issubset(set(itemsets)):
                sup += 1
    return sup

"""
检查potentialFP，也就是个由k-itemsets组成的k+1-itemsets是不是符合Apriori性质
也就是查看potentialFP中所有k-itemsets是不是在当前已挖掘出的frequent pattern当中
"""
def check_potentialFP(potentialFP, FP):
    s = potentialFP.split(";")
    """获取字符串 s 的所有长度为 n-1 的子串"""
    n = len(s)
    if n <= 1:  # 如果字符串长度 <= 1，无 n-1 长度子串
        return True
    for i in range(n):
        # 跳过第 i 个字符，获取剩余 n-1 个字符的子串
        substring = s[:i] + s[i + 1:]
        substring = ";".join(substring)
        if substring not in FP:
            return False
    return True

"""
此函数通过已挖掘出的frequent pattern去组合k+1-itemsets
然后使用check_potentialFP函数进行筛选
最后通过get_sup函数计算support，看看是否满足
此函数返回k+1-frequent itemsets
"""
def join_FP(FP, read_path, min_support):
    t_FP = {}
    for i,itemi in enumerate(FP):
        for j,itemj in enumerate(FP):
            if j <= i:
                continue
            else:
                t_itemi = itemi.split(";")
                t_itemj = itemj.split(";")
                if len(t_itemi)!=1 and len(t_itemj)!=1 and t_itemi[:-1] != t_itemj[:-1]:
                    continue
                potentialFP = itemi+";"+t_itemj[-1]
                if check_potentialFP(potentialFP, FP):
                    t_FP_sup = get_sup(potentialFP, read_path)
                    if t_FP_sup > min_support:
                        t_FP[potentialFP] = t_FP_sup
    return t_FP