исходная_строка = 'yqwdyqyw dyqwdyqwydyqd'
новая_строка = ''

for x in исходная_строка:
    if x == 'y':
        новая_строка += 'x'
    else:
        новая_строка += x
        
print(новая_строка)