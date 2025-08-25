from pathlib import Path
read_path = Path("Mining using Apriori.txt")
write_path = Path("part1.txt")
FP = {}
with read_path.open("r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        # if i >= 5:  # 只读前5行
        #     break
        print(line.strip().split(";"))
        for itemset in line.strip().split(";"):
            if itemset not in FP:
                FP[itemset] = 1
            else:
                FP[itemset] += 1

print(FP)
contents = ""
for key, value in FP.items():
    if value > 771:
        contents += str(value)+":"+str(key)+"\n"
print(contents)
write_path.write_text(contents)