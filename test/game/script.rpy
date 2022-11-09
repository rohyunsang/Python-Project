# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image winter idle = "images/winter.jpg"
image winter idle2 = "images/winter2.jpg"

# 게임에서 사용할 캐릭터를 정의합니다.
define lee = Character('이영민', color="#32a732")
define win = Character('winter',color = "#3db7b1")
$ i = 10

# 여기에서부터 게임이 시작합니다.
label start:

    lee "윈터야 안뇽" 

    win "민!! 나 근데 요즘 고민이 있어 ㅜㅜ"

    lee "뭔데?"

    win "사진 이게 이뻐 저게이뻐?"
    
    show winter idle at right
    win "이게 1번!"

    show winter idle2 at left 
    win "이게 2번이야"

    hide winter
    win "히히 부끄러 그만봐"

    menu:
        '1번':
            jump root_1
        '2번':
            jump root_2

    return

label root_1:
    show winter idle
    win "1번이 더 이쁘지? 히히[i]"
    jump script2
    

label root_2:
    show winter idle2 
    win "2번이 더 이쁘지? 히히"
    jump script2

label script2:

    lee "하하"

    
