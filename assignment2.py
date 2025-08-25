from pathlib import Path
from utils import *

# 支持度阈值
min_support = 771
# 要挖掘的原始文档
read_path = Path("Mining using Apriori.txt")
# 结果文档，存储了itemsets和对应的support
write_path = Path("part2.txt")
# 使用字典存储挖掘结果
FP = {}
# 挖掘出frequent 1-itemset
with read_path.open("r", encoding="utf-8") as f:
    for line in f:
        for itemset in line.strip().split(";"):
            if itemset not in FP:
                FP[itemset] = 1
            else:
                FP[itemset] += 1
    FP = {k: v for k, v in FP.items() if v >= min_support}

# 循环挖掘出frequent k+1-itemsets
kp1FP = FP
while kp1FP:
    # 假设FP为frequent k-itemsets，则kp1FP为frequent k+1-itemsets
    kp1FP = join_FP(kp1FP, read_path, min_support)
    FP.update(kp1FP)
    print(kp1FP)

# 挖掘结果写入指定路径
contents = ""
for key, value in FP.items():
    contents += str(value)+":"+str(key)+"\n"
write_path.write_text(contents)


