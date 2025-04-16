![image](https://github.com/user-attachments/assets/09bf4fa6-fb7c-45be-9489-1dc8deaf6e7a)

# 💡 미션 1: 버튼이 눌린 동안만 LED 켜기

이 실습은 **라즈베리파이의 GPIO 입력 신호를 활용하여**,  
버튼이 **눌려 있는 동안에만 LED가 켜지고**,  
버튼에서 손을 떼면 LED가 자동으로 꺼지는 동작을 구현한 예제입니다.

---

## 🎯 실습 목적

- 입력 장치(Button)와 출력 장치(LED)의 동작 연계 이해
- `gpiozero` 라이브러리를 사용한 간결한 코드 구성 연습
- **디지털 입력의 상태에 따라 출력 제어**하는 기본 제어 로직 학습

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

[▶️ 시연 영상 보러가기](https://youtu.be/TNbJCfQXWqI?si=pzP8ZwS4gV-ggv8A)

👉 버튼을 누를 때만 4개의 LED가 동시에 점등됩니다.

---

## 🧩 회로 구성도

![image](https://github.com/user-attachments/assets/a62b4821-4004-4e4d-b096-870f52509ff1)


