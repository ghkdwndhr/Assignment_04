# 💡 도미노 LED 제어

이 폴더에는 라즈베리파이의 GPIO 핀을 이용하여  
LED를 도미노처럼 순차적으로 점등하는 스크립트가 들어 있습니다.

본 프로젝트는 간단한 쉘 스크립트를 통해  
GPIO 출력을 제어하는 방법을 익히고,  
하드웨어와 소프트웨어의 연동을 실습하는 데 목적이 있습니다.

---

## 🎥 시연 동영상

[![도미노 LED 시연 영상](https://img.youtube.com/vi/JqaspqSPogI/0.jpg)](https://youtu.be/JqaspqSPogI?si=rbQri3j8Vn_CoLt7)

👉 클릭하면 유튜브 영상으로 이동합니다.

---

## 🧩 회로 사진

> 아래는 실제 도미노 LED 회로 구성 사진입니다.  
> 회로는 브레드보드와 점퍼선을 활용하여 라즈베리파이의 GPIO 핀과 연결되어 있습니다.

![회로 사진](https://github.com/user-attachments/assets/cfeb92fd-beb6-4fba-a7de-f2902c0774e5)

---

## 🔌 사용한 GPIO 핀

| LED 번호 | 연결된 GPIO 핀 |
|----------|----------------|
| LED 1    | GPIO 14        |
| LED 2    | GPIO 15        |
| LED 3    | GPIO 16        |
| LED 4    | GPIO 18        |

LED는 총 4개이며, 한 번에 하나의 LED만 켜지도록 설계되어 있습니다.  
**14 → 15 → 16 → 18번 핀 순서로**, **1초 간격**으로 점등됩니다.  
이 순환은 무한 반복되며 도미노처럼 부드럽게 연결된 흐름을 시각적으로 보여줍니다.

---

## 📁 포함된 파일

- `domino4.sh` : 도미노 LED 제어를 위한 메인 쉘 스크립트  
  이 스크립트는 Bash로 작성되었으며, `pinctrl` 명령어를 사용하여 GPIO 핀의 상태를 제어합니다.

---

## ▶️ 실행 방법

터미널에서 다음 명령어를 입력하여 실행 권한을 부여하고 실행할 수 있습니다:

```bash
chmod +x domino4.sh
./domino4.sh
