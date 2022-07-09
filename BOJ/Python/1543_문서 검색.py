import sys
input = sys.stdin.readline

document = input().strip()
word = input().strip()
document_index = 0
word_len = len(word)

count = 0
while (document_index<len(document)):
    if(word in document[document_index:document_index+word_len]):
        count += 1
        document_index+=word_len
    else:
        document_index+=1

print(count)