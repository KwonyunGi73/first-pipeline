# test_calculator.py
from calculator import add  # 1단계에서 만든 파일의 add 함수를 가져옴

# add 함수를 테스트하는 함수
def test_add_function():
    # 2 더하기 3이 5가 맞는지 확인
    assert add(2, 3) == 5
    # -1 더하기 1이 0이 맞는지 확인
    assert add(-1, 1) == 0
    
    print("성공: 모든 계산기 테스트를 통과했습니다!")