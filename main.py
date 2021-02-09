def xor_c(a, b):
	return '0' if(a == b) else '1'

def flip(c):
	return '1' if(c == '0') else '0'

def binarytoGray(binary):
	gray = ""
	gray += binary[0]
	for i in range(1, len(binary)):
		gray += xor_c(binary[i - 1],
					binary[i])
	return gray

def graytoBinary(gray):
	binary = ""
	binary += gray[0]
	for i in range(1, len(gray)):
		if (gray[i] == '0'):
			binary += binary[i - 1]
		else:                               
			binary += flip(binary[i - 1])
	return binary

def findSuccessor(suc):
  suc = int(suc, 2)
  suc += 1
  return bin(int(suc))[2:]

def findPredeccessor(pre):
  pre = int(pre, 2)
  pre -= 1
  return bin(int(pre))[2:]

print()
binary = input("Enter any Binary Code: ")

successor = ""
predecessor = ""
predecessor = findPredeccessor(binary).zfill(4)
successor = findSuccessor(binary).zfill(4)

print()
print("                | BINARY CODE | GRAY CODE |")
print(f"Predecessor     |        {predecessor} |      {binarytoGray(predecessor)} |")
print(f"Entered Value   |        {binary} |      {binarytoGray(binary)} |")
print(f"Successor   	|        {successor} |      {binarytoGray(successor)} |")

print()
gray = input("Enter any Gray Code: ")
binary = graytoBinary(gray)

predecessor = binarytoGray(findPredeccessor(binary)).zfill(4)
successor = binarytoGray(findSuccessor(binary)).zfill(4)

print()
print("                |   GRAY CODE | BINARY CODE |")
print(f"Predecessor     |        {predecessor} |        {graytoBinary(predecessor)} |")
print(f"Entered Value   |        {gray} |        {binary} |")
print(f"Successor   	|        {successor} |        {graytoBinary(successor)} |")
print()