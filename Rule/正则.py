# #!/usr/bin/python
# import re
# s = "骨髓瘤细胞症状不会正常的功能性抗体，而是引起称为检查单克隆蛋白的异常免疫球蛋白检查的原因"
# a = "骨髓瘤细胞"
# b = "异常免疫球蛋白检查"
# # rule = re.compile('骨髓瘤细胞.*[引起,产生].*异常免疫球蛋白')
# rule = []
# rule.append(re.compile(r''+a+''+'.*[引起,产生].*'+b))
# # rule.append(re.compile(r'.*采用.*'+'[' + a + ',' + b + ']' + '.*'))
# print(rule)
# for r in rule:
#     res = r.findall(s)
# if len(res)==0:
#     print(11)
# else:
#     print(res)
l= [1,2,3,1,2,3,1]
print(l.rindex(2))