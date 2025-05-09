# 🔢 3비트 LED 카운터 과제

이 폴더에는 라즈베리파이의 GPIO 핀을 이용하여  
LED 3개로 숫자 1부터 7까지를 **이진수로 표현하는 LED 카운터 스크립트**가 포함되어 있습니다.

본 과제는 Bash 스크립트를 통해 2진수 개념을 시각적으로 이해하고,  
GPIO 제어를 통해 하드웨어와의 연동을 실습하는 것을 목표로 합니다.

---

## 🎥 시연 동영상

[![3비트 카운터 시연 영상](https://img.youtube.com/vi/sFfZCYv-jSo/0.jpg)](https://youtu.be/sFfZCYv-jSo?si=sqDUGz0Gey9cy3Z3)

👉 클릭하면 유튜브 영상으로 이동합니다.

---

## 🧩 회로 사진

> 아래는 실제 3비트 카운터 회로 구성 사진입니다.  
> 각 LED는 라즈베리파이의 GPIO 14, 15, 16번 핀에 연결되어 있습니다.
> 회로에는 라즈베리파이, 브레드보드, 점퍼선, LED, 저항이 연결되어 있습니다.

![image](https://github.com/user-attachments/assets/5cd2e13e-2067-4095-a716-9c252d1d8145)


---

## 🔌 사용한 GPIO 핀

| 비트 위치 | 연결된 GPIO 핀 | 설명     |
|-----------|----------------|----------|
| MSB (2)   | GPIO 14        | 가장 왼쪽 LED |
| Bit 1     | GPIO 15        | 가운데 LED   |
| LSB (0)   | GPIO 16        | 가장 오른쪽 LED |

LED는 숫자의 이진수 표현에 따라 점등되며,  
1초 간격으로 숫자가 1부터 7까지 증가합니다.

---

## 📁 포함된 파일

- `count8.sh` : 3비트 LED 카운터 스크립트

---

## ▶️ 실행 방법

```bash
chmod +x count8.sh
./count8.sh
