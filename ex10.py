print("string1 : ", end='')
string1 = "Veh jxyi unuhsysu oek mybb xqlu je mhyju jxu fqiimeht yd q iocrebkc.jnj vybu."

# for i in range(0,10):
for j in range(0, len(string1)):
	# string1[j]가 영문자인것만 적용
	if (string1[j] != ' ' and string1[j] != '.'):
		char = ord(string1[j]) + 10
		if (char > 122):
			char = char - 26
		elif (char > 90 and char < 97):
			char = char - 26
		char = chr(char)
		print(char, end="")
	else:
		print(string1[j], end='')
print("")

print("string3 : ", end='')
countLetter = ord('Z') - ord('a') + 1
string6 = "Xlmtizgfozgrlmh lm wvxlwrmt gsrh ormv, gsv gsriw ovggvi rh: s"
for i in range(0, len(string6)):
	if (string6[i] != ' ' and string6[i] != ',' and string6[i] != ':'):
		char = ord('Z') - (ord(string6[i]) - ord('a'))
		char = chr(char)
		print(char, end="")
	else:
		print(string6[i], end='')
print("")

print("string2 : ", end='')
string2 = "Q29uZ3JhdHVsYXRpb25zIG9uIGRlY29kaW5nIHRoaXMgbGluZSwgdGhlIGZpcnN0IGxldHRlciBpczogaw=="
# bash에서 base64 -d 명령어로 디코딩한 결과를 출력하는 코드
import base64
print(base64.b64decode(string2))


print("string4 : ", end='')
string3 = "67 79 78 71 82 65 84 85 76 65 84 73 79 78 83 79 78 68 69 67 79 68 73 78 71 84 72 73 83 76 73 78 69 84 72 69 78 69 88 84 67 72 65 82 65 67 84 69 82 73 83 50"
string3 = string3.split(' ')
for i in string3:
	print(chr(int(i)), end='')
print("")


print("string5 : ", end='')
string4 = "Charlie Oscar November Golf Romeo Alpha Tango Uniform Lima Alpha Tango India Oscar November Sierra ... Oscar November ... Delta Echo Charlie Oscar Delta India November Golf ... Tango Hotel India Sierra ... Lima India November Echo ... Tango Hotel Echo ... November Echo X-Ray Tango ... Lima Echo Tango Tango Echo Romeo ... India Sierra ... Juliett"
string4 = string4.split(' ')
for i in string4:
	if (i == '...'):
		print(' ', end='')
	else:
		print(i[0], end='')
print("")


print("string6 : ", end='')
string5 = "CONGRATULATIONS ON DECODING THIS LINE THE NEXT LETTER IS K"
print(string5)


print("string7 : ", end='')
countLetter = ord('Z') - ord('A') + 1
string6 = "RSOEBLNZAYNDQOT QT IKITREUM OEBO YEUM, NKG AYTN PGSZNMB RT: K"
# url : https://www.boxentriq.com/code-breaking/playfair-cipher
result6 = "CONGRATUYFTISQN SN DECODNPG THIS LNPE, TMH YFNO LETXTEC BS: M"