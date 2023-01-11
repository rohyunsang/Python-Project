# 이 파일에 게임 스크립트를 입력합니다.

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
                
                text "jung 호감도{space=15}[persistent.junglove]" size 24
                bar:
                    value persistent.junglove
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
                
                text "han 호감도{space=15}[persistent.hanlove]" size 24
                bar:
                    value persistent.hanlove
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
define persistent.junglove = 10
define persistent.hanlove = 40

#love[0] = jung
#love[1] =jeon
#love[2] = lee
#love[3] = han 

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
#image winter idle = "images/winter.jpg"
#image winter idle2 = "images/winter2.jpg"
image bg bus = "bg_bus.jpeg"
image bg bar = "bg_bar.png"####
image bg room = "bg_room.jpeg"
image bg pcidle = "pc_idle.jpeg"
image bg pckitchen = "pc_idle.jpeg"
image bg lw = "bg_lotteworld.png"
image bg lr = "bg_lectureroom.png"
image bg lotteworldnight = "bg_lotteworldnight.jpeg"
image msg1:
    "msg1.png"
    zoom 0.5
image msg2:
    "msg2.png"
    zoom 0.5

image msg3:
    "msg3.png"
    zoom 0.5

image msg4:
    "msg4.png"
    zoom 0.5

image msg5:
    "msg5.png"
    zoom 0.5
image m1:
    "m1.png"
    zoom 0.5
image m2:
    "m2.png"
    zoom 0.5
image m3:
    "m3.png"
    zoom 0.5
image m4:
    "m4.png"
    zoom 0.5
image m5:
    "m5.png"
    zoom 0.5
image m6:
    "m6.png"
    zoom 0.5
image m7:
    "m7.png"
    zoom 0.5
image m8:
    "m8.png"
    zoom 0.5
image m9:
    "m9.png"
    zoom 0.5
image m10:
    "m10.png"
    zoom 0.5
image m11:
    "m11.png"
    zoom 0.5
image m12:
    "m12.png"
    zoom 0.5


image han smile1 = "han_smile1.png"
image han hi2 = "han_hi2.png"
image han smile2 = "han_smile2.png"
image jeon hi = "jeon_hi.png"
image jeon normal = "jeon_idle.png"
image jung normal = "jung_idle.png"
image jung cute = "jung_cute.png"
image jung pretty = "jung_pretty.png"
image jung smile = "jung_smile.png"
image jung smile2 = "jung_smile2.png"
image jung pretty2 = "jung_pretty2.png"
image jung jung_pretty3 = "jung_pretty3.png"



# 게임에서 사용할 캐릭터를 정의합니다.
define kim = Character('김건우', color="#32a732")
define ym = Character('이영민', color="#c425aa")####
define jung = Character('정다희',color = "#3db7b1")
define han = Character('한서희',color = "#138211")

# 여기에서부터 게임이 시작합니다.
label start:                                          #scene 1
    ############################################################################
    #scene1
    scene bg bar
    
    kim "얘는 왜 이렇게 늦는거야.. "
    ym "건우 오래기다렸어? 쏴리 쏴리~"
    kim "됐고 얼른 술이나 먹자. 이모 여기 술국하나랑 후레시 한 병 주세요"
    "(얼마 후....)"
    ym "아오 써,, 몇 병째야 우리 오늘 너무 달리는 거 아니야?"
    kim "넌 이게 쓰냐!! 난 술이 달다,,, 인생이 쓰다..."
    ym "ㅋㅋㅋㅋㅋㅋ"
    kim "복학하면 연애하고싶었는데 전공공부하고 알바하다보니 이번학기 끝나버렸다."
    kim "그나마 남는 시간이라고는 너랑 술먹고 피파하는게 전부인게 너무 현타온다"
    ym "건우,,, 저기 셀카찍는 사람봐바 존예다 존예"
    kim "내말 듣고있기나.."

    show han_smile2
    "(와.. 진짜 예쁘다...)"
    ym "건우야 아까 너 연애하고 싶다면서 가서 번호물어봐"
    "(고민하는 건우.. 하지만 저렇게 예쁜사람에겐 보나마나 멋진 남자친구가 있을 것 같았다.)"
    kim "됐어 내가 뭔 연애냐, 이제 방학인데 알바나 열심히해서 여행이나 가려고"
    ############################################################################
    #scene2
    scene bg room
    kim "아 아까 번호 물어볼걸그랬다... 진짜 내스타일이었는데 다음에 보면 꼭 번호 물어봐야겠다."
    kim "종강도 했으니 알바나 찾아볼까"
    kim "어 여기 바로 집 앞 피씨방이잖아 시간대도 괜찮고, 사람도 별로 안오는거같은데 여기 지원해봐야겠다."
    
    show msg1
    " "
    show msg2
    " "
    show msg3
    " "
    show msg4
    " "
    show msg5
    " "
    
    kim "피씨방 알바는 해봤으니 잘 할 수 있겠지..."
    ############################################################################
    #scene3
    scene bg pcidle

    "어..!"
    show han smile2
    "건우:(어제봤던 예쁜 사람이다..!!)"
    kim "안녕하세요 저 오늘 여기 면접보러왔는데요.."
    han "아 사장님이 말씀하신 분이구나..!"
    han "사장님이 갑자기 일이 생기셔서... 이력서 저한테 주세요!"
    kim "아 넵넵"
    "건우:(와 어제보다 더 예쁘네)"
    han "피자가게 뷔페, 다른 피시방 야간알바 8개월 정도 하셨고.. 흠.. 그럼 기본적인것들은 다 하실줄 아시겠네요?" 

    kim "네 다할줄압니다. !" 

    han "나이가 24살.. 지금 대학생? 어 단국대 다니시네요?? 저돈데...ㅎㅎ"
    "한서희:(건우? 훈훈하게 생겼네)"
    show screen han_favority
    $persistent.hanlove = 0

    menu:
        "건우가 물어본다.."

        "혹시 어제 볶신에 있지 않으셨어요?" :
            han "어! 어케아셨어요 하긴, 제 미모가 좀 눈에 띄긴 하죠"
            $ persistent.hanlove +=15
            "호감도가 15 증가했습니다."
            "건우:(처음부터 예쁘다하면 너무 들이대는 거 같으니깐 어물쩍 넘겨야겠다.)"
            kim "하하 그런가? 어제 친구랑 거기서 한잔했어요 ㅋㅋ"
            han "뭔가 뵌 거같기도 해요..!"

        "전공이 뭐에요??" :
            han "저 경영학과요!! 건우씨는요?"
            kim "저는 컴퓨터공학과요"
            han "혹시 노윤상 아세요?"
            
            menu:
                "윤상이 모르면 간첩이죠, 컴공과 천재 게임개발자잖아요. 지금 피씨방 점유율 1등게임 개발자를 모를수가 있나요 하하":
                    han "(헐 대박!!! 나중에 소개해달라고해야겠다.)"
                    $ persistent.hanlove +=15
                    "호감도가 15 올랐습니다."
                    
                "아니요":
                    han "와 말투 진짜 싸가지없네;; 그리고 어떻게 컴공이 노윤상을 몰라;;"
                    $ persistent.hanlove -=40
                    "호감도가 40 내려갔습니다."
    han "건우씨 몇살이에요?"
    kim "저 24살이요"
    han "저 23살인데 말 편하게 하세요 오빠"
    "건우:(오빠..라니...이건 반칙이잖아,,,,)"
    kim "으..응 그래"
    han "그럼 내일부터 나오는걸로 사장님께 말씀 드려놓는다? 주말2시부터 10시까지야!! 기본적인 일은 내일 알바생이 알려줄거야"
    show han_hi2
    han "그럼 잘가!!"
    hide screen han_favority  
    ############################################################################
    scene bg bus

    kim "(드디어 오늘 피방 첫출근이구나 저번에 본 서희는 평일 오후에만 나오나 서희랑 같이하면 좋았을텐데..?)"

    "건우는 설레는 마음을 이끈채로 피방에 출근하려고 버스에 탔다."

    scene bg pcidle

    kim "아.. 안녕하세요! 오늘부터 알바하게된 김건우라고 합니다."

    
    show jung normal at left

    jung "ㅎㅇㅎㅇ 어? 주말오후 신입맞죠!!!!"

    kim "안녕하세요 김건우입니다."

    jung "저는 정다희에요 24살"

    kim "어 동갑이네요! (와 이분도 진짜 아름다우시다..)"
    
    $persistent.junglove = 10

    hide jeon normal at right

    menu:
        "다희씨는 여기서 얼마나 일했어요?":
            jung "여기서 일한지 별로안됐어요."
            kim "(왠지 말이 잘 통할것같은 기분이 든다.)"

        "다희씨는 전공이 뭐에요?":
            jung "저 컴공 졸업하고 회사다니다가 지금 취직 준비중이라 알바하구있어요" 
            kim "저도 컴공이에요!!"
            jung "와 신기하다~"
            $persistent.junglove +=5
            "호감도가 5 증가했습니다."

    "142번 자리에서 음식주문이 들어왔습니다."

    kim "매콤떡갈비마요? 이건 어떻게 만들어요?"

    jung "알려줄게요 따라오세요."

    scene bg pckitchen

    show jung smile

    "....(알바끝)"

    kim "수고했어 다희야 친절하게 알려줘서 고마웠어"

    jung "뭘 ..ㅎㅎ 수고했어 너두 너 이제 알바끝났는데 뭐하게? 술먹을래?"

    "(아니 진짜 뭐지? 이렇게 이쁜 여자가 나한테 술을먹자한다고?)"
    hide jeon_favority
    show screen jung_favority
    menu:
        "나 대기소과제해야해서...":
            jung "응 알겠어 다음주에 보자!"
            kim "(아니다,, 오늘 아니면 언제 또 이런사람이랑 술먹어보겠냐 걍 술마시러가야겠다.)"
            kim "다희야 가자 술먹으러 나 어차피 집에가도 게임할거같아 ㅋㅋ"

        
        "어어? 으응? 좋지!":
            $persistent.junglove += 10
            "호감도가 10 증가하였습니다."
    
    ############################################################################

    scene bg bar
    "어쩌다 보니 술집에 오게 되었다.. 어색해 죽겠네 그래도 믿기지가 않는구먼.."

    show jung cute

    jung "안주는 뭐로할래?"

    menu:
        "호두 닭강정":
            $persistent.junglove +=10
            jung "그거 좋다!"
            "호감도가 10 증가하였습니다."
        "민트초코화채":
            $persistent.junglove +=15
            jung "그거 좋다!"
            "호감도가 15 증가하였습니다."                    
        "오뎅탕":
            $persistent.junglove +=20
            jung "그거 좋다!"
            "호감도가 20 증가하였습니다."
        
    jung "그나저나 오늘 술마시고 싶었는데 ㅋㅋ 좋네"
    $persistent.junglove +=10
    "호감도가 10 증가하였습니다."

    menu:
        "오늘 왜 술먹고 싶었는데?":
            jung "요즘 취준때매 힘들어서 그랬어 "
            kim "그렇구나,, 취준하기 힘들겠다.. 힘내!"
            jung "고마워 ㅋㅋ"
            $persistent.junglove +=5
            "호감도가 5증가 하였습니다."
        
        "...ㅎㅎ그랬구나":
            jung "(뭐야 싱겁게,,)"
            $persistent.junglove -=5
            "호감도가 5감소하였습니다."

    jung "내 MBTI맞춰볼래??"

    menu:
        "E/I중에 고르세요"
        "E":
            jung "그리고?"
            $persistent.junglove +=5
            "호감도가 5증가 하였습니다."
        
        "I":
            jung "땡 E로시작해"
    menu:
        "S/N중에 고르세요"
        "S":
            jung "그리고?"
            $persistent.junglove +=5
            "호감도가 5증가 하였습니다."
        
        "N":
            jung "땡 S야"
    menu:
        "F/T중에 고르세요"
        "F":
            jung "그리고?"
            $persistent.junglove +=5
            "호감도가 5증가 하였습니다."
        
        "T":
            jung "땡 T야"
    menu:
        "P/J중에 고르세요"
        "P":
            jung "ESFP가 내 MBTI야"
            $persistent.junglove +=5
            "호감도가 5증가 하였습니다."
        
        "J":
            jung "땡 P야, ESFP"

    menu:
        "나는 MBTI과몰입하는 거 싫더라":
            jung "(뭐지 나 들으라고하는 이야기인가;;)"
            $persistent.junglove -=10
            "호감도가 10감소 하였습니다."
        
        "ESFP들은 연예인같다던데 너 진짜 연예인같다 윈터 닮았다는 소리 안들었어?":
            jung "아진짜 뭐래~ "
            jung "(얘 뭐야뭐야~ 나한테 관심있나봐 미쳤나봐)"
            $persistent.junglove +=15
            "호감도가 15 올랐습니다."

    " (2시간 후 : 현재 시간 12시 30분 ) "

    "(서로 기분좋게 취했다)"

    menu:
        "맞다, 나 너 전화번호좀 ㅎㅎ":
            jung "아 그래그래 내 번호는  010-4908-7325야"
            kim "내 번호는 010-5241-7713이야"
            $persistent.junglove +=10

        "2차갈래?":
            jung "나 통금있어서 가봐야해"
            jung "맞다, 폰 줘바 내 번호 알려줄게 010-4908-7325야"
            
    "어느 덧 막차가 끊길 시간이다. 다희는 서둘러 역쪽으로 떠났다."
    
    kim "조심히 들어가~ 카톡할게"
    hide jung cute
    show jung smile2
    jung "어 너도 조심히 들어가"

#######################################################################
    scene bg room
    kim "(어젠 정말 즐거운 시간이었다.. 연락해봐야지)"
    
    show m1
    " "
    show m2
    " "
    show m3
    " "
    show m4
    " "
    show m5
    " "
    show m6
    " "
    show m7
    " "
    show m8
    " "
    show m9
    $persistent.junglove +=10
    "호감도가 10 증가하였습니다."
    show m10
    " "
    show m11
    " "
    show m12
    " "
    kim "김건우 미쳤다라는 말밖에 안나온다."

    #################################################################
    scene bg_lectureroom
    kim "(다희와의 데이트 3시간전이지만 대학기초SW수업만큼은 집중해서 들어야지)"
    
    #################################################################
    scene bg_lotteworld
    kim "후우,,, 떨린다잉"

    show jung_smile2
    jung "건우!! 안뇽 아침수업있다더니 늦지않게 잘 왔네"
    kim "(다희와의 데이트인데 어떻게 늦을 수가 있단 말인가..)"
    kim "(그나저나 오늘 다희는 말도안되게 예쁘군)"
    kim "가..갈까 ? "

    jung "빨리 가서 재밌는거 많이 타자."
    kim "(설렘반 떨림반 두근거리는 마음을 부여잡고 롯데월드에 입장했다.)"
    hide jung_smile2
    show jung_pretty
    "그 후 우리는 말도안되게 재미난 시간을 보냈다. 어트렉션 줄을 기다리며 다희와 나는 쉬지않고 대화했다." 
    hide jung_pretty
    "평상시에 여자랑 대화할 때면, 꿔다놓은 보릿자루마냥 말이 없던 나였지만 오늘 다희와의 대화는 물흐르듯이 잘 흘러갔다. "
    $persistent.junglove +=10
    "호감도 10이 증가했습니다"
    show jung_pretty2
    "다희와 아틀란티스도 타고 자이로드롭 등등 여러가지 어트렉션을 즐기고 초코 슈가 안에 가득채워져있는 츄러스와 엄청길고 맛있는 아이스크림도 먹었다. "
    $persistent.junglove +=10
    "호감도 10이 증가했습니다"
    hide jung_pretty2
    show jung_pretty3
    "토끼머리띠도 끼고 사진을 같이 찍던중, 우리 커플 컨셉으로 사진찍자라는 말에 나는 당황해 아무말도 하지 못했는데 다희가 내 어깨에 살짝 기대어 사진을 찍었다. "
    $persistent.junglove +=10
    "호감도 10이 증가했습니다"
    "나는 살짝어색한표정으로 웃고있었다. 슬슬 어두워지고 안으로 들어와 퍼레이드를 보던중 좀비가 나오는 호러 어트렉션에서 커플 맞으시죠? 라는 직원의 멘트에 살짝 쑥스러워하며 웃는 다희의 얼굴이 생각이나 살며시 웃었다. "
    $persistent.junglove +=10
    "호감도 10이 증가했습니다"
    "고백은 그날의 분위기다.. 나 김건우 오늘 고백을 해야겠다는 생각이들었다."


    scene bg_lotteworldnight
    show jung_pretty3
    kim "다희야..."
    jung "너무 즐겁다 건우야~~~ 엉 왜??"
    kim "우리...... 사......"

    if persistent.junglove<100:
        kim "(뭐지...... 갑자기 말이 안나온다...)"
        kim "우리...... 사......ㄱ  ㅜ   ㅣ"
        jung "응? 무슨말하는거야?? 건우야 괜찮아?!!"
        
        play music "alarm.mp3" loop

        
        stop music

        scene bg_room
        play music "alarm.mp3" loop
        "엄마: 건우야 건우야~~~~ 일어나야지 금요일 9시에 대학기초SW수업 있잖니~"
        kim "...................."
        stop music
        ""
        play music "last.mp3" 
        "어느 깊은 가을밤,잠에서 깨어난 제자가 울고있었다."
        "그 모습을 본 스승이 기이하게 여겨 제자에게 물었다."
        "무서운 꿈을 꾸었느냐?"
        "아닙니다"
        "슬픈 꿈을 꾸었느냐?"
        "아닙니다. 달콤한 꿈을 꾸었습니다."
        "그런데 왜 그리 슬피 우느냐?"
        "제자는 흐르는 눈물을 닦아내며 나지막히 말했다."
        "그 꿈은 이루어질수 없기 때문입니다."
    else:
        kim "다희야... 우리 사귀자!!!"
        jung "건우야,,,, "
        hide jung_pretty3
        show jung_smile
        jung "그래.... ><"
        

    return 

    
