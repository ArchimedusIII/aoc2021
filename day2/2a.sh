#!/bin/bash
forward=$(grep forward input | awk '{print $2}' | paste -sd+ | bc)
down=$(grep down input | awk '{print $2}' | paste -sd+ | bc)
up=$(grep up input | awk '{print $2}' | paste -sd+ | bc)

antwoord=$(($forward*($down-$up)))

echo "$antwoord"
