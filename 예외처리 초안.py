def main():
    while True:
        n = input("1에서 9 사이의 정수를 입력하시오 (end 입력 시 코드 완료): ")
        if n == "end":
            print("코드가 완료되었습니다.")
            return
        try:
            if len(n) != 1:
                print("올바른 형식의 숫자를 입력하시오.")
                raise ValueError()
            if n not in "123456789":
                print("올바른 형식의 숫자를 입력하시오.")
                raise ValueError()
            break
        except ValueError:
            continue

main()