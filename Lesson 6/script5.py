import re

content = open('content.txt','r').read()
pattern = 'id=(\d+),num=(\d+)'

# print re.findall(pattern,content,re.I|re.S)

# print re.finditer(pattern,content,re.I|re.S)
# it = iter(re.finditer(pattern,content,re.I|re.S))
# print next(it).group(1)

# print re.sub(pattern,"ARM",string)

# matched = re.findall(pattern,string)
# print matched
# for i in matched:
#     print i

# match = re.match(pattern,string) #
# if match:
#     print 'match'
# else:
#     print 'not match'









'''
    if(string =~ m##is){

    }
'''

'''
    while(string =~ m##igs){

    }
'''