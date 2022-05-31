# 11조 할당 문제 팀 과제
# random 모듈 임포트
import random
def main():
    # 역할 1:
    # 사용자로부터 n값 입력받음
    # 사용자가 n의 값으로 정수를 입력하지 않았거나, 음수를 입력했을시의 예외 처리를 위해 raise문을 활용했다
    # whileTrue 반복문이 계속 돌아가면서 사용자에게 입력을 받는다.
    while True:
        try:
            #end를 탈출문으로 사용하기 위해서 우선 인풋값을 문자열로 받아옴
            s = input("n 값을 입력하세요(end 입력하면 코드 완료): ")
            #만약 input이 탈출문이면 코드 실행 종료
            if s == "end":
                print("코드를 완료합니다")
                return
            #n을 int로 받아옴
            n = int(s)
        except:
            #만약 n이 int가 아니면 오류 발생 후 다시 while문 실행
            print("정수를 입력해주세요")
            continue
        # 만약 n값이 10보다 크거나 0보다 같거나 작으면 오류 발생. 예외처리를 try-except문으로 구현
        try:
            if n>10 or n<=0:
                raise ValueError
        except:
            print("1 부터 9까지의 정수를 입력해주세요")
            continue

        # n*n 이중 리스트 생성
        data = [[rand_num() for i in range(n)] for j in range(n)]

        # 역할 2:
        # 0부터 n-1까지를 담은 리스트 생성
        index_list = [i for i in range(n)]

        # 0부터 n-1까지의 인덱스들의 모든 순열을 2D 리스트로 반환받아 for문에 사용
        # 다음과 같은 로직으로 최솟값을 계산:
        # 예를 들어, 2D 리스트과 다음과 같다면, [[0, 1], [1, 0]]
        # [0, 1]은 로봇 1이 작업 1을, 로봇 2가 작업 2를,
        # [1, 0]은 로봇 1이 작업 2를, 로봇 2가 작업 1을 하는 케이스이고,
        # 이러한 방법으로 모든 순열을 탐색하여 최소비용이 나오는 케이스를 최적 케이스로 반환하는 방식
        min_cost = -500
        min_case = []
        for i in permutation(index_list, n):
            # 각 순열의 비용을 나타내는 cost 생성
            cost = 0
            # for문을 이용하여 cost에 순열 정보대로 비용을 더함
            for j in range(n):
                cost += data[j][i[j]]
            # min_cost의 최초값은 임의로 -500이라는 음수로 설정
            # 따라서 min_cost가 음수이거나 (즉, 이번 순열이 첫번째 순열이거나)
            # 이번 순열의 cost가 기존 min_cost 값보다 크다면
            # min_cost 값을 이번 순열의 cost 값으로 update하고
            # min_case도 저장한다
            if cost < min_cost or min_cost < 0:
                min_cost = cost
                min_case = i

        # 아직 역할 4 구현 전이라 역할 2의 기능 점검을 위해 임시적으로 프린트문 생성, 이후 역할 4로 대체할 것
        print("최소 비용은 " + str(min_cost) + " 입니다.")
        print("이 때, 로봇들은 다음과 같이 작업을 수행합니다: ")
        for i in range(len(min_case)):
            print("로봇 " + str(i + 1) + "이(가) 작업 " + str(min_case[i]) + "을(를) 수행합니다.")


# 역할 1:
# 1부터 10까지의 랜덤 자연수 생성 함수
def rand_num():
    return random.randrange(1, 11)

# 역할 2:
# 리스트가 들어오면 r개 (r <= len(list1)) 크기의 모든 순열을 2D 리스트로 반환하는 함수
# 순열을 재귀적으로 구현하였으며, 다음 예시와 같은 로직을 통해 구현:
# (1, 2, 3, 4)의 모든 순열은 (1) + ((2, 3, 4)의 모든 순열)이고,
# (2, 3, 4)의 모든 순열은 (2) + ((3, 4)의 모든 순열)이고
# (3, 4)의 모든 순열은 (3) + ((4)의 모든 순열)
def permutation(list1, r):
    # 반환값이 될 리스트 생성
    return_list = []
    # 만일 r값이 1이라면, 그냥 각 원소를 2D 리스트 형태로 반환값 리스트에 저장
    if r == 1:
        for i in list1:
            return_list.append([i])
    # 만일 r값이 1보다 크다면, 다음과 같이 처리한다
    elif r > 1:
        # list1의 길이만큼 반복하는 for문
        for i in range(len(list1)):
            # copy_list1은 list1의 복사 리스트
            copy_list1 = [j for j in list1]
            # copy_list1의 i번째 값을 지움
            copy_list1.remove(list1[i])
            # 짧아진 리스트를 permutation에 넣고 재귀적 실행
            # 그 후, 첫 값과 permutation 함수로부터 받아온 2D 리스트들의 원소들(1D 리스트들)을 합쳐서 반환
            # 리스트에 append한다
            for p in permutation(copy_list1, r - 1):
                return_list.append([list1[i]] + p)
    # 반환 리스트를 반환한다.
    return return_list


# 메인 함수의 실행
if __name__ == "__main__":
    main()