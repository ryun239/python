


def solution(a, b):
    answer = 0
    days = ['fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu']
    months = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

    for i in range(a -1):
        answer += sum(months[i])

    answer += b -1

    print(days[answer % 7])
    return days[answer % 7]

    


if __name__ == "__main__":
    solution(1, 2)

