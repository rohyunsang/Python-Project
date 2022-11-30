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
                
                text "jeon 호감도{space=15}[persistent.jeonlove]" size 24
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
                
                text "lee 호감도{space=15}[persistent.leelove]" size 24
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
                
                text "han 호감도{space=15}[persistent.hanlove[0]]" size 24
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
define persistent.junglove = 10
define persistent.jeonlove = 20
define persistent.leelove = 0
define persistent.hanlove = [40,]

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
define jeon = Character('전민정',color = "#111111")
define lee = Character('이은채',color = "#1f24b4")
define han = Character('한서희',color = "#138211")
define win = Character('김윈터',color = "#142421")


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
    $ persistent.hanlove[0] = 0

    menu:
        "건우가 물어본다.."

        "혹시 어제 볶신에 있지 않으셨어요?" :
            han "어! 어케아셨어요 하긴, 제 미모가 좀 눈에 띄긴 하죠"
            $ persistent.hanlove[0] +=15
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
                    $ persistent.hanlove[0] +=15
                    "호감도가 15 올랐습니다."
                    
                "아니요":
                    han "와 말투 진짜 싸가지없네;; 그리고 어떻게 컴공이 노윤상을 몰라;; 이사람 html으로 프로그래밍 한다고 할거같은데;; "
                    $ persistent.hanlove[0] -=40
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

    show jeon hi
    hide jeon hi
    show jeon normal

    jeon "안녕하세요~ 전민정이라고해요~"

    "머리에 샤넬 머리띠를 한 키가 한 155정도 돼보이는 여자가 날 한번 째려보더니 안녕하세요 라고 인사한다." 

    "그리곤 키 뭉텅이를 하나 들더니 따라 오라고 한다. "

    "따라 갔더니 면접봤던 그장소에 알바복이 여러개 걸려있었다. "

    "내 사이즈에 맞는 옷을 꺼내 입고 , 다시 피시방으로 향했다."

    jeon "피방알바 해봤다 했죠? 그럼 웬만한건 다 아시겠네요?"

    kim "네네" 

    "system : 41번 자리에서 음식주문이 들어왔습니다." 

    jeon "치즈돈까스라볶이 들어왔다 치즈돈까스 라볶이 만드는법 알려드릴게요"

    "냉장고에서 재료를 꺼내오는 전민정"

    jeon  "다른피시방어디에서 해봤어요?"

    kim "정자에서 했었는데 거기는 코로나 때문에 망해서 멀리까지 왔어요"

    jeon  "어디살아요?"

    kim "저 정자동 살아요 오는데 한 30분 ? 걸려요"

    jeon  "음.. 조금 머네요" 

    jeon  "이름이 어떻게 되세요?"

    kim "김건우에요 나이는 24살!"

    

    jeon  "저는 22살, 전민정이에요"

    "(ㅎㅎ 내가 오빠네 오빠라고 해주면 좋겠다.)"

    jeon  "라볶이 는 이렇게 이렇게 돈까스는 튀김기 알람 2분 울리면 한번 뒤집어 줘요."

    kim "아 아~"

    jeon  "그리고 라볶이 위에 돈까스 잘라서 나가주면 돼요 "

    kim "쉽네요 ㅎㅎ. 제가 가져다 주고 올게요!" 

    jeon  "네"

    "2시 51분, 정다희가 출근했다."
    hide jeon normal

    show jeon normal at right
    show jung normal at left

    jung "ㅎㅇㅎㅇ 어? 주말오후 신입맞죠!!!!"

    kim "안녕하세요 김건우입니다."

    jung "저는 정다희에요 24살"

    kim "어 동갑이네요! (와 진짜 개이쁘다 여긴 뭐 얼굴보고 뽑나? 아니 진짜 뭐지? )"

    jeon "저 가볼게요 다희언니 고생하고 건우오빠 담주에 뵈여"
    
    hide jeon normal at right

    jung "혹시 담배펴요 건우씨 ?" 

    kim "아 군대 갔다와서 진짜 끊어 보려했는데 잘 안되더라구요 담배 하나 피러 가시죠"

    kim "(입에 담배를 물며) 저희 말 편하게 할래요? (와 진짜 내 스타일이다..)"

    jung "ㅇㅇ 좋치 나 라이터좀 빌려주라"

    kim "다희 너 여기서 얼마나 일했어 ?"

    jung "나도 여기서 일한지 별로안됐어 "

    kim "다희 너는 전공이 뭐야 ?"

    jung " 나 컴공과 ! 인데 졸업하고 회사다니다가 지금 이직 준비중이라 알바하구있어" 

    kim "어 ? 나도 컴공과인데 오오"

    jung "어 진짜 ?"

    kim "웅 너 멋지다 회사도 다녔구"

    "142번 자리에서 음식주문이 들어왔습니다."

    kim "매콤떡갈비마요? 이건 어떻게 만들어?"

    jung "알려줄게 따라와봐."

    "…....(알바끝)"

    kim "수고했어 다희야 친절하게 알려줘서 고마웠어"

    jung "뭘 ..ㅎㅎ 수고했어 너두 너 이제 알바끝났는데 뭐하게? 술먹을래?"

    "(아니 진짜 뭐지? 이렇게이쁜여자가 나한테 술을먹자한다고? 이거 장기 때이는거아니야? 아니 나 드디어 여자친구 생기는건가? 아니 신혼여행은 ? 어디로가지? 손주이름은 뭐로하는게 좋치 ?진짜 뭐지 나 드디어 “성공”해버린 건가 ? )"
    hide jeon_favority
    show screen jung_favority
    $persistent.junglove = 10
    menu:
        "나 대기소과제해야해서...":
            jung "응 알겠어 다음주에 보자!"
            kim "(아니다,, 집에가봤자 어차피 과제는 안하고 게임할거같아 그럴바엔 걍 술이라도 먹어야겠다)"
            kim "다희야 가자 술먹으러 나 어차피 집에가도 게임할거같아 ㅋㅋ"

        
        "어어? 으응? 좋지!":
            $persistent.junglove += 10
            "호감도가 10 증가하였습니다."
    
    ############################################################################

    scene bg bar
    "어쩌다 보니 술집에 오게 되었다.. 어색해 죽겠네 그래도 믿기지가 않는구먼.."
    jung "안주는 뭐로할래?"

    menu:
        "호두 닭강정":
            $persistent.junglove +=10
            jung "그거 좋다!"
            "호감도가 10 증가하였습니다."
        "민트초코화채":
            $persistent.junglove +=20
            jung "그거 좋다!"
            "호감도가 20 증가하였습니다."                    
        "오뎅탕":
            $persistent.junglove +=30
            jung "그거 좋다!"
            "호감도가 30 증가하였습니다."
        
    jung "그나저나 오늘 술마시고 싶었는데 ㅋㅋ 좋네"
    $persistent.junglove +=10
    "호감도가 10 증가하였습니다."

    kim "너는 어쩌다 이직하게 된거야?"

    jung "나 .. 음 거기 회사는 내가 계속 다녀도 실력도 늘거 같지도 않고 발전이 없을거 같아서 그랬어"

    kim "그랬구나 나도 취업하구 싶다. 아직 대학생이라 ㅜㅜ"

    jung "그건 환상이야 너두 다녀봐 ㅎㅎ(멋쩍은 웃음)" 

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
    show jung_smile2
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
    jung "츄러스먹자!!"
    kim "낫배드"
    jung "토끼머리띠도하자!!"
    kim "진짜 낫배드"
    jung "교복도 빌리자"
    kim "진짜 진짜 낫배드"

    jung "빨리 가서 재밌는거 많이 타자."
    kim "(설렘반 떨림반 두근거리는 마음을 부여잡고 롯데월드에 입장했다.)"
    hide jung_smile2
    show jung_pretty
    "그 후 우리는 말도안되게 재미난 시간을 보냈다. 어트렉션 줄을 기다리며 다희와 나는 쉬지않고 대화했다." 
    hide jung_pretty
    "평상시에 여자랑 대화할 때면, 꿔다놓은 보릿자루마냥 말이 없던 나였지만 오늘 다희와의 대화는 전성기 유재석을 능가하는 입담 퍼포먼스였다. "
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
    "역시 여자들은 셀카를 많이 찍어서인지 잘나왔지만 나는 살짝어색한표정으로 웃고있었다. 슬슬 어두워지고 안으로 들어와 퍼레이드를 보던중 좀비가 나오는 호러 어트렉션에서 커플 맞으시죠? 라는 직원의 멘트에 살짝 쑥스러워하며 웃는 다희의 얼굴이 생각이나 살며시 웃었다. "
    $persistent.junglove +=10
    "호감도 10이 증가했습니다"
    "고백은 그날의 분위기다.. 나 김건우 오늘 고백을 해야겠다는 생각이들었다."

    scene bg_lotteworldnight
    kim "다희야..."
    jung "너무 즐겁다 건우야~~~ 엉 왜??"
    kim "우리...... 사......"
    kim "(뭐지...... 갑자기 말이 안나온다...)"
    kim "우리...... 사......ㄱ  ㅜ   ㅣ"
    jung "응? 무슨말하는거야?? 건우야 괜찮아?!!"
    
    play music "alarm.mp3" loop

    "건우야 건우야~~~~~~"
    stop music

    scene bg_room
    play music "alarm.mp3" loop

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


















            
    return 

    
