#!/bin/bash

# GPIO 핀 번호 (MSB → LSB 순서): 14, 15, 16
pins=(14 15 16)

# 핀들을 출력 모드로 설정
for pin in "${pins[@]}"; do
    pinctrl set $pin op
done

# 1부터 7까지 이진수로 표현하면서 LED 점등
while true; do
    for num in {1..7}; do
        for i in {0..2}; do
            bit_index=$((2 - i))  # MSB부터
            value=$(( (num >> bit_index) & 1 ))

            if [ "$value" -eq 1 ]; then
                pinctrl set "${pins[$i]}" dh
            else
                pinctrl set "${pins[$i]}" dl
            fi
        done
        sleep 1
    done
done