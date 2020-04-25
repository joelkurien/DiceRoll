#Type of dice needed
def dicetype():
	print("1.Cubical Die")
	print("2.Octahedron Die")
	print("3.Pentagonal Trapezohedron Die")
	print("4.Dodecahedron Die")
	print("5.Icosahedron Die")
	n = int(input("Enter the dice of choice"))
	if n==1:
		return 6
	elif n==2:
		return 8
	elif n==3:
		return 10
	elif n==4:
		return 12
	elif n==5:
		return 20

#Roll of the dice
import random
def generateroll():
	z = dicetype()
	x = int(input("Enter the number of dice"))
	a = []
	for i in range(0,x):
		a.append(random.randint(1,z))
	return a

#Check the validity of roll
def check():
	chk = generateroll()
	print(chk)
	if len(chk) == 1:
		if chk[0] == 1 or chk[0] == 6:
			print("roll again")
			check()
	else:
		chkset = set(chk)
		n = len(chkset)
		if n == 1:
			print("roll again")
			check()

if __name__ == "__main__":
	choice = 'Y'
	while True:
		check()
		n = input("Want to roll again[Y/N] ")
		choice = n
		if choice == 'N':
			break
