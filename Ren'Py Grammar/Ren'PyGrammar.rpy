# filename extension is .rpy

label start:
# its similiar main in c or cpp


# How to charcter say : press 'Tab' key and write

define lee = Charcter('이영민', color = "#111111")

#define charcter name = Charcter('charcter name',color = '# hex code')

$ percent = 100.0 * points / max_points # make variable
g "I like you [percent:.2] percent!"

# Not supported global variable

# VSC 주석 처리

# Ctrl K + C => 선택한 영역 주석
# Ctrl K + U => 선택한 영역 주석 해제

# 2. Persistent - 데이터 보관

# 1) define 변수명
# 2) define persistent.변수명

# 변수를 두 가지 방법으로 선언했을 때,

# 1)은 게임을 재실행하면 초기화된다.
# 2)는 초기화 persistent._clear() 하기 전까지는 값이 계속 보관된다.

# 재설치 후에 persistent 데이터가 계속 남아있는지는 확인이 필요하다.

if persistent.love[0] < 0: # if에는 $ 써주면 안된다.
        $ persistent.love[0] = 0 # 모든 변수에는 $을 써줘야한다.