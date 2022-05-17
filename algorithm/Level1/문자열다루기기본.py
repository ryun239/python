

def sol(s):

    return s.isdigit() and len(s) in (4,6)

if __name__ == "__main__":
    #s = "1234"
    s = "a1234"
    print(sol(s))