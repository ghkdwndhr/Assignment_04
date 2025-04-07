#!/bin/bash

# 사용할 GPIO 핀 번호
pins=(14 15 16 18)

# 각 핀을 출력 모드로 설정
for pin in "${pins[@]}"; do
    pinctrl set $pin op
done

# LED 도미노 루프
while true; do
    for pin in "${pins[@]}"; do
        # 모든 LED 끄기
        for offpin in "${pins[@]}"; do
            pinctrl set $offpin dl
        done

        # 현재 핀 켜기
        pinctrl set $pin dh

        # 1초 대기
        sleep 1
    done
done
