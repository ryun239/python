


def solution(sizes):
    answer = 0

    sizes = [sorted(i) for i in sizes]
    w = [i[0] for i in sizes]
    h = [i[1] for i in sizes]

    print(max(w) * max(h))

    return answer

if __name__ == '__main__':
    #a = [[60, 50], [30, 70], [60, 30], [80, 40]]
    a = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    solution(a)