#!/usr/bin/env python3
import pandas as pd
import numpy as np
fLog=open("ruby_2.log") #读取脚本所在当前目录的log
import re
pattern_r=re.compile(r' s -  ')
test_list=[]
for line in fLog:
    target=re.findall(pattern_r,line)
    if(target):
        #print(line)
        test_list.append(line)

list1=[]
list2=[]
for each in test_list:
    s1=each.split(' s -')[0]
    list1.append(s1[:-7])
    list2.append(s1[-7:])

s1=pd.Series(np.array(list1))
s2=pd.Series(np.array(list2))
df=pd.DataFrame({"name":s1,"result":s2})
miss_list=['so_k_nucleotidepreparing /tmp/fasta.output.100000','so_reverse_complementpreparing /tmp/fasta.output.2500000']
#df.replace('',np.nan)
df['name'][111]=miss_list[0]
df['name'][124]=miss_list[1]
df['name'][393]=miss_list[0]
df['name'][406]=miss_list[1]
df.to_csv("result.csv",encoding='utf-8',index=None,header=None)
print("----结果已经保存至当前目录result.csv----")
