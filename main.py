# 11조 할당 문제 과제
import random
import numpy as np
import itertools as it


def main():
    # 역할 1:
    # 사용자로부터 n값 입력받음
    n=int(input("n : "))

    # n*n 이중 리스트 생성
    data=[[rand_num() for i in range(n)] for j in range(n)]

    data=np.array(data)

    print(data)

    # 솔루션 탐색 초안:
    list=list(range(n))

    permute=it.permutations(list, n)

    final_permute=0
    sum_of_permute=10*n

    for i in permute:
        sum=0
        k=0
        for j in i:
            sum+=data[k][j]
            k+=1
        if sum_of_permute>sum:
            sum_of_permute=sum
            final_permute=i

    print(sum_of_permute, final_permute)

# 1부터 10까지의 랜덤 자연수 생성 함수
def rand_num():
    return random.randrange(1, 11)

# 메인 함수의 실행
if __name__ == "__main__":
    main()

