


def sol(s):
    return s.lower().count('p') == s.lower().count('y')

if __name__ == "__main__":
    s = "pPoooyY"	
    print(sol(s))