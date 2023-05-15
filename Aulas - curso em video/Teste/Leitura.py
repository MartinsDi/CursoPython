txt = 'palavras.txt'
arquivo = open(txt, 'r')
arr = []
nt = []
#tem = ['b', 'r', 'e', 't', 'o']
while True:
    a = str(input())
    if a == '0':
        break
    nt.append(a)
for i in arquivo:
    print(i)
    resp = False
    if i[2] == 'r' and i[4] == 'a' and 'i' in i and 'u' in i:
        for a in i:
            if a in nt:
                resp = False
                break
            else:
                resp = True

        if resp:
            arr.append(i)

print(arr)
print('furia\n' in arr)