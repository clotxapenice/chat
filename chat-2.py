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
    Allen_word_count = 0
    Allen_sticker_count = 0
    Allen_picture_count = 0
    Viki_word_count = 0
    Viki_sticker_count = 0
    Viki_picture_count = 0
    for line in lines:
        s = line.split(' ')     
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker_count += 1
            elif s[2] == '圖片':
                Allen_picture_count += 1
            for m in s[2:]:
                Allen_word_count += len(m)       
        elif name == 'Viki':
            if s[2] == '貼圖':
                Viki_sticker_count += 1
            elif s[2] =='圖片':
                Viki_picture_count += 1
            for m in s[2:]:
                Viki_word_count += len(m)
    print('Allen說了', Allen_word_count, '個字')
    print('Allen傳送了', Allen_sticker_count, '個貼圖')
    print('Allen傳送了', Allen_picture_count, '個圖片')
    print('Viki說了', Viki_word_count, '個字')
    print('Viki傳送了', Viki_sticker_count, '個貼圖')
    print('Viki傳送了', Viki_picture_count, '個圖片')
#寫入檔案
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig')as f:
        for  line in lines:
            f.write(line)

#執行檔案main
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)
main()