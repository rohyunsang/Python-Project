# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image winter idle = "images/winter.jpg"
image winter laugh = "images/winter2.jpg"

# 게임에서 사용할 캐릭터를 정의합니다.
define lee = Character('이영민', color="#32a732")
define oh = Character('오주원',color = "#db2dbb")
define winter = Character('winter',color = "#3db7b1")

# 여기에서부터 게임이 시작합니다.
label start:

    lee "나 이영민 여자친구를 만들고 싶다."

    lee "오주원 너 나랑 사귀자!!!!!"

    oh "헤이 boy~~~~~~~"

    oh "Hi how was your today?"

    lee "섹스"

    show winter idle
    winter "영민쿤 나는 안되는거야?"

    lee "꺼져 이 못생긴년아 나는 주원이 밖에 없어"
    
    show winter laugh
    winter "힝구힝구"
    hide winter

    lee "하핫"

    return
