![image](https://github.com/user-attachments/assets/ce6d92e8-fa03-4988-9362-149b0996e3ea)


# 💡 미션 3: 버튼을 누르면 도미노 LED 순차 점등

이 실습은 라즈베리파이의 버튼 입력을 활용하여  
버튼을 **한 번 누르면 4개의 LED가 순차적으로 켜졌다 꺼지는 도미노 동작**을 구현한 예제입니다.

버튼을 누를 때마다 도미노 동작이 **한 번만 실행**되고,  
끝나면 다시 대기 상태로 돌아갑니다.

---

## 🎯 실습 목적

- 입력 트리거 발생 시 순차 출력 동작 구현  
- `gpiozero`의 `when_pressed` 이벤트 사용법 학습  
- 리스트, 반복문, 시간 지연을 조합한 도미노 패턴 구성

---

## 🔌 사용한 GPIO 핀

| 기능   | 연결된 GPIO 핀 |
|--------|----------------|
| LED 1  | GPIO 8         |
| LED 2  | GPIO 7         |
| LED 3  | GPIO 16        |
| LED 4  | GPIO 20        |
| 버튼   | GPIO 25        |

버튼에는 내부 Pull-up 기능이 적용되며,  
버튼이 눌릴 때 GPIO 25번 핀이 GND에 연결되어 `lo` 상태가 됩니다.

---

## 🎥 시연 영상

[▶️ 시연 영상 보러가기](https://youtu.be/LwHpUlh4mug?si=VZUWRmCfWLcRxH6w)

👉 버튼을 한 번 누르면 LED가 **도미노처럼 차례로 켜졌다 꺼집니다.**

---

## 🧩 회로 구성도

![image](https://github.com/user-attachments/assets/0a01d0dd-4245-4b95-99b6-bd95f4966ad4)


---
