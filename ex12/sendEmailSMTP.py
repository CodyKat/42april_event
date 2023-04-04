import smtplib
import imghdr #이미지 첨부를 위한 라이브러리
from email.message import EmailMessage

# STMP 서버의 url과 port 번호
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

# 1. SMTP 서버 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

EMAIL_ADDR = 'jjm480251@gmail.com'
EMAIL_PASSWORD = 'fqlwtazomsaaanmd'

# 2. SMTP 서버에 로그인
smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)

# 3. MIME 형태의 이메일 메세지 작성
message = EmailMessage()
message.set_content('my name is jaemjeon')
message["Subject"] = "SMTP TEST"
message["From"] = EMAIL_ADDR  #보내는 사람의 이메일 계정
message["To"] = 'piepie1346@gmail.com'

# 3-1. 이메일에 사진 첨부하기
with open('/Users/jaemjeon/Downloads/IMG_4022.jpg', 'rb') as image:
  image_file = image.read() # 이미지 파일 읽어오기

image_type = imghdr.what('e-mail', image_file)
message.add_attachment(image_file, maintype = 'image', subtype = image_type)

# 4. 서버로 메일 보내기
smtp.send_message(message)

# 5. 메일을 보내면 서버와의 연결 끊기
smtp.quit()