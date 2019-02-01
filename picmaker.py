#! /usr/bin/env python3
import sys

def generate_picture():
	fout = open("picture.ppm","w+")
	fout.write("P3\n500 500\n255\n")

	line = []
	for i in range(500):
		for j in range(500):
			line.append(str(i//2)+" 255 "+str(j//2))
		line.append("\n")
		temp = " ".join(line)
		fout.write(temp)
		line = []
	fout.close()
	
generate_picture()


