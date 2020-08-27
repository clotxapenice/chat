lines =[]
newline = []
with open('3.txt', 'r', encoding='utf-8-sig')as f:
    for line in f:
        lines.append(line.strip())
for line in lines:
    s = line.split(' ')
    time = str(s[0][:5])
    name = str(s[0][5:])
    content = str(s[1: ])
    newline.append(time + ' ' + name + ' ' + content)
     

print(newline)
with open('3output', 'w', encoding='utf-8-sig')as f:
    for new in newline:
        f.write(new + '\n')

    