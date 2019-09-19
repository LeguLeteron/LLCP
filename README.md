# LLCP - The LeguLeteron Communication Protocol

Copyright (C) 2019 The LeguLeteron Project

Licensed under the GNU General Public License v3

## 사용 전 주의사항

LLCP는 점자 변환 시에 한글을 풀어써야 하므로, **hgtk** 모듈을 사전에 설치하여야 합니다.

> pip install -r requirements.txt

## braille.py

점자 모듈

- remove_acl_violation(target): target 문자열에 대하여 특수문자와 기타 지원불가 문자를 제거함.
- check(target): target 문자/문자열에 대하여 한글인지, 로마자인지, 숫자인지를 판별함.
- **create(target)**: target 문자열을 점자로 변환함.
- **beautify(target)**: target 점자 튜플을 패킷으로 전송하기 쉽게 서브튜플 사이의 관계를 단순화함.



사용범례: 문자열 LeguLeteron에 대하여 **beautify(create("LeguLeteron"))** 를 사용하면 다음과 같은 결과가 도출됩니다.

**-> ((1, 0, 1, 0, 1, 0), (1, 0, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0), (1, 0, 0, 0, 1, 1), (1, 0, 1, 0, 1, 0), (1, 0, 0, 1, 0, 0), (0, 1, 1, 1, 1, 0), (1, 0, 0, 1, 0, 0), (1, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0), (1, 1, 0, 1, 1, 0))**



## braille_support.py

점자 지원 모듈

딕셔너리 형태로 각 문자에 대한 점자 형태가 저장되어 있습니다.



## protocol.py

Uart 통신 프로토콜 모듈

### 클래스

- RX 클래스: **RX(커서그랩상태, 진동피드백상태, 진동피드백TEXT상태, 진동피드백IMAGE상태, 점자출력상태, 점자데이터)** 로 새 객체 생성 가능.
  - RX.raw(): RX 객체에 대하여 바로 전송이 가능한 바이트 패킷을 구성함.
- TX 클래스: **TX(커서그랩상태, 진동피드백TEXT상태, 진동피드백IMAGE상태, 점자출력상태, 디바이스주소)** 로 새 객체 생성 가능.
  - TX.raw() TX 객체에 대하여 바로 전송이 가능한 바이트 패킷을 구성함.

### 메소드

- report(): 현재 설정된 송수신 데이터 변수의 내용을 출력함.
- send(packet): packet이라는 패킷을 디바이스에 전송함.
- receive(): 디바이스로부터 패킷을 받아 TX 데이터 변수에 저장함.

### 송수신 흐름 제어

send() 메소드는 receive() 메소드가 성공적으로 패킷을 받아 True를 반환할 때까지 계속 디바이스에 동일 데이터를 전송합니다.

### 사용예시

아래 예시는 사용자로부터 문자열을 입력받아 현재 송신 데이터값과 함께 디바이스에 전송합니다.

> ```python
> text = beautify(create(input()))
> for i in text:
>     raw_go_hw = RX(rx_cursor, rx_vibrate, rx_vibrate_text, rx_vibrate_image, rx_output, i).raw()
>     send(raw_go_hw)
> ```