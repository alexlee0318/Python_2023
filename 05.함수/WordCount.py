# 파일의 단어 개수 세기
import re, string, sys
# sys.argv[0] - WordCount, sys.argv[1] - filename 이 들어감
if len(sys.argv) != 2:
     print('사용법: WordCount filename')
     sys.exit(-1)
with open (sys.argv[1]) as file:
    contents = file.read()
clean_contents = re.sub('['+string.punctuation+']',' ',contents)
clean_contents = clean_contents.replace('\n','').lower()

words = clean_contents.split()

print(f'총 단어는 {len(words):,d}개 이고, 고유 단어는 {len(set(words)):,d}입니다.')

dic = {}
for word in words:
    if word in dic.keys():
        dic[word] += 1
    else:
        dic[word] = 1

result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print('사용 빈도가 높은 단어 Top 10')
for word, count in result[:10]:
        print(f'{word}\t{count:,d}')