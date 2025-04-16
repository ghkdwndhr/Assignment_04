![image](https://github.com/user-attachments/assets/832ce610-5f8d-46aa-930b-0945b1fc4f40)


# 💡 미션 2: 버튼이 눌릴 때마다 LED 토글

이 실습은 라즈베리파이의 GPIO 버튼 입력을 활용하여,  
버튼을 **누를 때마다 LED의 상태가 반전**되는 구조를 구현한 예제입니다.  
LED는 버튼을 누를 때마다 켜졌다 꺼지는 **토글 방식**으로 제어됩니다.

---

## 🎯 실습 목적

- 버튼 입력에 반응하여 상태를 기억하고 제어하는 구조 이해  
- `gpiozero`의 `when_pressed` 이벤트 기반 제어 학습  
- 간결한 토글 로직 구현 및 비트 연산 활용 실습

---

## 🔌 사용한 GPIO 핀

| 핀 번호 | 용도     | 설명                        |
|---------|----------|-----------------------------|
| GPIO 8  | LED 1    | 가장 왼쪽 LED               |
| GPIO 7  | LED 2    | 왼쪽에서 두 번째 LED        |
| GPIO 16 | LED 3    | 오른쪽에서 두 번째 LED      |
| GPIO 20 | LED 4    | 가장 오른쪽 LED             |
| GPIO 25 | 버튼     | 토글 트리거용 (내부 Pull-up 사용)

- LED는 **MSB → LSB 순서**로 연결되어 있고,  
- 버튼은 GPIO 25번 핀에 연결되어 **눌릴 때 `"lo"` 상태가 되어 입력이 감지됩니다.

---

## 🎥 시연 영상

[▶️ 시연 영상 보러가기](https://youtu.be/v8Ha2BVN80c?si=wDWBzJsfgD6uFIBO)


---


## 🧩 회로 구성도

![image](https://github.com/user-attachments/assets/fb23bb8c-5a57-4c55-845d-c9bda2ef26f4)


---

