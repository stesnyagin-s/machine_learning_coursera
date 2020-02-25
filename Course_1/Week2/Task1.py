import numpy as np
import heapq
from scipy.spatial import distance
import re
file = open('C:/Users/stesn/Downloads/_3a8d746cf4d86fba2f31586f239d11fd_sentences.txt', 'r')
text = file.readlines()
file.close()
text = [line.lower() for line in text]
text = [re.split('[^a-z]', line) for line in text]
text = [list(filter(None, line)) for line in text]
words = set()
for line in text: 
    for word in line:
        words.add(word)
word_dic = {}
i = 0
for word in words:
    word_dic[word] = i
    i+=1
n = len(text)
m = len(words)
A = np.zeros(shape = (n, m), dtype = np.float64)
i = 0
for line in text:
    for word in line:
        A[i, word_dic.get(word)] += 1
    i+=1
dist = []
for i in range(1,n):
    heapq.heappush(dist, (distance.cosine(A[0,:], A[i,:]), i))
file = open('ans1.txt', 'w')
file.write(str(heapq.heappop(dist)[1]) + ' ')
file.write(str(heapq.heappop(dist)[1]))
file.close()