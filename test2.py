'''
仿射密码
(a,b)
m = 26，字符集为小写字母
加密函数是E(x)= (ax + b) (mod m)
解密函数为D(x) = (a^-1)(x - b) (mod m)，其中a^-1是a的乘法逆元
'''

#通过一个简单的遍历得到a的乘法逆元，也可以通过gmpy2库中的invert函数实现
def get_inverse(a):
    for i in range(1,27):
        if a*i%26==1:
            return i

#加密
def encipher(a, b, p):
    c=[]
    for i in p:
        if i == " ":
            c.append(" ")
        else:
            temp=((ord(i)-97)*a+b)%26+97
            c.append(chr(temp))
    print(''.join(c))

#解密
def decipher(a, b, c):
    a_inv = get_inverse(a)
    print(a_inv)
    p=[]
    for i in c:
        if i == " ":
            p.append(" ")
        else:
            temp=(((ord(i)-97)-b)*a_inv)%26+97
            p.append(chr(temp))
    print(''.join(p))

if __name__ == "__main__":
    a = 3
    b = 4
    # message = 'jzcgcgegcoxlqqveoxlqutettcrqkcxzqd'
    message = 'jzcg cg e gcoxlq qveoxlq ut ettcrq kcxzqd'
    # print((ord("a")-97))
    decipher(a,b,message)
    #decipher(a,b,message)