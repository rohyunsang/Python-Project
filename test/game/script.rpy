﻿# 이 파일에 게임 스크립트를 입력합니다.

init:
    screen jung_favority:
        # 호감도 창
        frame:
            # 호감도 창 테두리와 컨텐츠와의 간격
            padding (15, 15)
            # 호감도 배경 (반투명 - 뒤 2자리 코드가 투명도)
            background "#4f5a6680"
            # x, y축 정렬
            align (1.0, 0.0)
            # 호감도 창 크기
            xmaximum 250
            ymaximum 200
 
            # 텍스트와 호감도 바가 수직으로 배치됨
            vbox:
                
                text "jung 호감도{space=15}[persistent.junglove]" size 16
                bar:
                    value persistent.junglove
                    # 호감도 바 범위
                    range 100
                    
                    # 아래 지정한 fixed_bar 스타일을 따름
                    style "fixed_bar"
                    
    screen jeon_favority:
        # 호감도 창
        frame:
            # 호감도 창 테두리와 컨텐츠와의 간격
            padding (15, 15)
            # 호감도 배경 (반투명 - 뒤 2자리 코드가 투명도)
            background "#4f5a6680"
            # x, y축 정렬
            align (1.0, 0.0)
            # 호감도 창 크기
            xmaximum 250
            ymaximum 200
 
            # 텍스트와 호감도 바가 수직으로 배치됨
            vbox:
                
                text "jeon 호감도{space=15}[persistent.jeonlove]" size 16
                bar:
                    value persistent.jeonlove
                    # 호감도 바 범위
                    range 100
                    
                    # 아래 지정한 fixed_bar 스타일을 따름
                    style "fixed_bar"
    screen lee_favority:
        # 호감도 창
        frame:
            # 호감도 창 테두리와 컨텐츠와의 간격
            padding (15, 15)
            # 호감도 배경 (반투명 - 뒤 2자리 코드가 투명도)
            background "#4f5a6680"
            # x, y축 정렬
            align (1.0, 0.0)
            # 호감도 창 크기
            xmaximum 250
            ymaximum 200
 
            # 텍스트와 호감도 바가 수직으로 배치됨
            vbox:
                
                text "lee 호감도{space=15}[persistent.leelove]" size 16
                bar:
                    value persistent.leelove
                    # 호감도 바 범위
                    range 100
                    
                    # 아래 지정한 fixed_bar 스타일을 따름
                    style "fixed_bar"
    screen han_favority:
        # 호감도 창
        frame:
            # 호감도 창 테두리와 컨텐츠와의 간격
            padding (15, 15)
            # 호감도 배경 (반투명 - 뒤 2자리 코드가 투명도)
            background "#4f5a6680"
            # x, y축 정렬
            align (1.0, 0.0)
            # 호감도 창 크기
            xmaximum 250
            ymaximum 200
 
            # 텍스트와 호감도 바가 수직으로 배치됨
            vbox:
                
                text "han 호감도{space=15}[persistent.hanlove[0]]" size 16
                bar:
                    value persistent.hanlove[0]
                    # 호감도 바 범위
                    range 100
                    
                    # 아래 지정한 fixed_bar 스타일을 따름
                    style "fixed_bar"
                  
                
 
 
init -5 python:
    # 호감도 바 스타일
    style.fixed_bar = Style(style.default)
    
    # bar width
    style.fixed_bar.xmaximum = 200
    
    # bar height
    style.fixed_bar.ymaximum = 15
    
    # bar의 gutter 부분 간격; 5로 지정할 시 5만큼 색이 칠해져있음
    style.fixed_bar.left_gutter = 0 
    style.fixed_bar.right_gutter = 0
    
    style.fixed_bar.left_bar = Frame("images/bar_full.png", 0, 0)
    style.fixed_bar.right_bar = Frame("images/bar_empty.png", 0, 0)
 
# 호감도 수치
define persistent.junglove = 0
define persistent.jeonlove = 0
define persistent.leelove = 0
define persistent.hanlove = [0,]

#love[0] = jung
#love[1] = jeon
#love[2] = lee
#love[3] = han 

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image winter idle = "images/winter.jpg"
image winter idle2 = "images/winter2.jpg"

# 게임에서 사용할 캐릭터를 정의합니다.
define kim = Character('김건우', color="#32a732")

define jung = Character('정다희',color = "#3db7b1")
define jeon = Character('전민정',color = "#111111")
define lee = Character('이은채',color = "#1f24b4")
define han = Character('한서희',color = "#138211")
define win = Character('김윈터',color = "#142421")


# 여기에서부터 게임이 시작합니다.
label start:                                          #scene 1

    scene bg building
    
    show screen jung_favority # status window open

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

label root_1:                                        #scene 2-1
    show winter idle
    win "1번이 더 이쁘지? 히히"
    $ persistent.junglove += 30
    if persistent.junglove > 100:
        $ persistent.junglove = 100
    jump script2
    

label root_2:                                        #scene 2-2
    show winter idle2 
    win "2번은 안이뻐 사실"
    $ persistent.junglove -= 30
    if persistent.junglove < 0: # 0 미만일 경우 0으로 처리
        $ persistent.junglove = 0 
    jump script2

label script2:                                       #scene 3

    lee "하하"

    lee "호감도 창을 지워볼까? "
    
    hide screen jung_favority

    lee "다른 사람 호감도 창을 뛰워 볼까?"

    show screen han_favority

    lee "이렇게 하는게 맞노? han favoirty" 

    hide screen han_favority

    show screen jeon_favority

    lee "이렇게 하는게 맞노? jeon_favority" 

    hide screen jeon_favority

    show screen lee_favority

    lee "이렇게 하는게 맞노? lee_favority" 

    return 
