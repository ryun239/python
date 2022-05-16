
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

def solution(new_id):
    answer = ''
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    print("step 1", new_id)

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    print("step 2", answer)

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.

    while ".." in answer:
        answer = answer.replace("..", ".")
    print("step 3", answer)

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if answer[0] == '.':
        answer.lstrip(".")
    if answer[-1] == '.':
        answer = answer[:-1]
    print("step 4", answer)


    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not answer:
        answer = "a"
    print("step 5", answer)

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if 16 <= len(answer) + 1:
        answer = answer[0 : 15]
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        if answer[-1] == '.':
            answer = answer[: -1]
    print("step 6", answer)
        
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(answer) < 3:
        answer += answer[-1]

    print("step 7", answer)

    

if __name__ == "__main__":
    #a = "...!@BaT#*..y.abcdefghijklm."
    #a = "z-+.^."
    a = "=.="
    #a = "123_.def"
    #a = "abcdefghijklmn.p"
    # bat.y.abcdefghi
    solution(a)