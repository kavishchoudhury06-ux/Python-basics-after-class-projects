from collections import Counter

dic = {
    'Apple' : 2,
    'Banana' : 4,
    'Orange' : 2,
    'Guava' : 2,
    'Pineapple' : 3
  
}

counts = Counter(dic.values())

print('Frequence of 2 is', counts[2], 'times')