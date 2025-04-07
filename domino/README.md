# 💡 도미노 LED 제어

이 폴더에는 라즈베리파이 GPIO 핀을 이용하여  
LED를 도미노처럼 순차적으로 켜는 스크립트가 들어 있습니다.

---

## 🎥 시연 동영상

[![도미노 LED 시연 영상](https://img.youtube.com/vi/JqaspqSPogI/0.jpg)](https://youtu.be/JqaspqSPogI?si=rbQri3j8Vn_CoLt7)

👉 클릭하면 유튜브 영상으로 이동합니다.

---

## 🧩 회로 사진

![회로 사진](https://github.com/user-attachments/assets/fbe4a4bb-3d4d-4cfb-af4f-a59dd6257ab2)

---

## 🔌 사용한 GPIO 핀

| LED 번호 | 연결된 GPIO 핀 |
|----------|----------------|
| LED 1    | GPIO 14        |
| LED 2    | GPIO 15        |
| LED 3    | GPIO 16        |
| LED 4    | GPIO 18        |

한 번에 하나의 LED만 켜지며,  
**14 → 15 → 16 → 18번 핀 순서로**,  
**1초 간격**으로 점등됩니다.

---

## 📁 포함된 파일

- `domino4.sh` : 도미노 LED 제어를 위한 메인 스크립트

---

## ▶️ 실행 방법

```bash
chmod +x domino4.sh
./domino4.sh
