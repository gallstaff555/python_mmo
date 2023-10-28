#!/bin/bash

for filename in *.png; do
	convert $filename -flop flip_$filename
done
