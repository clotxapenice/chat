import os
#讀寫檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig')as f:
        for line in f:
            lines.append(line.strip())
    return lines
#轉換檔案
def convert(lines):
    new = []
    name = None
    for line in lines:
        if line == 'Allen':
            name = 'Allen'
            continue
        elif line == 'Tom':
            name = 'Tom'
            continue
        if name:
            new.append(name + ': ' + line + '\n')
            
    return new
#寫入檔案
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig')as f:
        for  line in lines:
            f.write(line)

#執行檔案main
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
main()