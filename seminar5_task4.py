
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



from base64 import decode
from itertools import count


with open('first_for_sem5.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст, необходимый для сжатия: '))

with open('first_for_sem5.txt', 'r', encoding='UTF-8') as file:
    my_text = file.readline()
    text_compression = my_text.split()

    print(my_text)

def rle_encode(text): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not text: 
        return '' 

    for char in text: 
            # Если предыдущие и текущие символы не совпадают 
        if char != prev_char: 
                # затем добавьте количество и символ в нашу кодировку 
               
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
                # Или увеличьте наш счетчик, если символы действительно совпадают
              
            count += 1 
    else: 
         # Завершите кодировку
        encoding += str(count) + prev_char 
        return encoding

text_compression = rle_encode(my_text)

with open('second_for_sem5.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)

# Декодирование и запись в третий файл
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

text_decode = rle_decode(text_compression)
with open('decode_for_sem5.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_decode}')

print(text_decode)
