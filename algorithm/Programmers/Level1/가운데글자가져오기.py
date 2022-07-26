

from unicodedata import name

def sol(s):
    answer = ""
    s_len = len(s)
    print(s_len)

    if s_len % 2:
        answer = s[int(s_len/2)]
    else:
        answer = s[int(s_len/2) -1 : int(s_len/2)+1]

    return answer

if __name__ == "__main__":
    #s = 'abcde'
    #s = '123456789
    s = 'qwer'
    print(sol(s))