# Напишите программу, удаляющую из текста все слова, содержащие "абв"

text = 'Свет мой абв, зеркальце! Скажи, мнеабв да всю полнуабвю правду доложи. абв'
lst = ' '.join(list(filter(lambda s: 'абв' not in s, text.split())))
print(lst)