![image](https://github.com/user-attachments/assets/32514ad8-c5ae-4778-b881-fda813a6f2e4)


# 💡 미션 4: 버튼을 누를 때마다 4비트 카운터 증가

이 실습은 라즈베리파이의 버튼 입력을 활용하여,  
버튼을 **누를 때마다 숫자가 1씩 증가하고**,  
그 값을 4개의 LED로 **이진수 형태로 시각적으로 표현**하는 예제입니다.

숫자는 0부터 15까지 증가하며,  
15 이후에는 다시 0으로 초기화되어 반복됩니다.

---

## 🎯 실습 목적

- 이진수 표현 방식과 비트 연산을 활용한 출력 제어 이해  
- `gpiozero`를 사용하여 간단하게 수동 카운터 구현  
- 리스트 인덱싱과 `>>` 연산을 결합한 LED 제어 방식 학습

---

## 🔌 사용한 GPIO 핀

| 기능   | 연결된 GPIO 핀 |
|--------|----------------|
| LED 1 (MSB) | GPIO 8     |
| LED 2       | GPIO 7     |
| LED 3       | GPIO 16    |
| LED 4 (LSB) | GPIO 20    |
| 버튼        | GPIO 25    |

- LED는 **MSB → LSB 순서**로 배치되어 있으며,  
- 버튼은 내부 Pull-up 설정이 적용된 GPIO 25번 핀에 연결됩니다.  
- 버튼이 눌리면 `"lo"` 상태로 인식되어 입력으로 처리됩니다.

---

## 🎥 시연 영상

[▶️ 시연 영상 보러가기](https://youtu.be/PuJJDU0mwUs?si=P5HtQ7EsHSu7KpSF)

👉 버튼을 누를 때마다 **이진수로 표시되는 숫자가 1씩 증가**합니다.

---

## 🧩 회로 구성도

![image](https://github.com/user-attachments/assets/211f3ee8-e5d4-4f23-bdc1-5167dfbc2ad8)


---

