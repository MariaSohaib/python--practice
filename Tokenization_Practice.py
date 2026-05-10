import re
with open('The_Verdict.txt','r',encoding='utf-8') as f:
    raw_text=f.read()
result=re.split(r'([,.()\'?:;/\"]|--|\s)', raw_text)
new_list=[]
for word in result:
    if word.strip():
        new_list.append(word)
result=new_list
print(f'Total number of characters: {len(raw_text)}')
# print(raw_text[45:99])
# print(result[:50])
print(len(result))