
import heapq

def sol(sco, k):

    ret = 0
    heapq.heapify(sco)

    while sco[0] < k:
        mix = heapq.heappop(sco) + (heapq.heappop(sco) *2)
        heapq.heappush(sco, mix)
        ret += 1

        if len(sco) < 2 and sco[0] < k:
            ret = -1
            break

    return ret


if __name__ == "__main__":
    a = [7, 4, 2, 5, 1, 8, 9]
    k = 7

    ret = sol(a, k)
    print(ret)