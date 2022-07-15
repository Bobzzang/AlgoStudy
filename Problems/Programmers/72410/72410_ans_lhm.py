#https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    temp = ''
    for s in new_id:
        if s in [str(i) for i in range(10)]: #숫자 0~9
            temp +=s
        if 97<= ord(s) <= 122 or s in ['-','_','.']: #알파벳 a~z, -_.
            temp +=s
    new_id = temp

    while True:
        if '..' in new_id:
            new_id = new_id.replace("..",".")
        else:
            break
    if new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) >=2 and new_id[-1] == ".":
        new_id = new_id[:-1]
    if len(new_id) ==1 and new_id[-1] == ".":
        new_id = ''
    if new_id == '':
        new_id = 'a'
    while 16 <= len(new_id):
        new_id = new_id[:-1]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    while len(new_id)<=2:
        new_id = new_id + new_id[-1]
    return new_id 