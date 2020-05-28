#example 1
print("example1:\n")
try:
	f1 = open("testfile1.txt","r")
	f1.write("File for exception handling\n")
except IOError:
	print("Error:can't find file or read data\n")
	f1 = open("testfile1.txt","w+")
	print("Error handled by creating a file")
else:
	print("Contents written succesfully\n")
finally:
	print("Done!Error raised because the file didn't exist.")

#example 2
print("example2:\n")
try:
	f3 = open("testfile3.txt","r")
	f4 = open("testfile4.txt","r+")
except IOError:
	print("Error:can't find file or write data\n")
else:
	print("Contents in testfile3:\n")
	line1 = f3.readline()
	print(line1)
	for data in f3:
		f4.write(data)
	print("Contents written in testfile4 from testfile3\n")
	line2 = f4.readline()
	print(line2)
	f3.close()
	f4.close()
finally:
	print("Done!")

#example 3
print("example3:\n")
try:
	f2 = open("testfile3.txt","w+")
except IOError as e:
	print("Error occured, as Permission Error:\n",e)
else:
	print("Contents read succesfully\n")
finally:
	print("Done!No error hence except block won't execute.")

#example 4
#raise exception example
print("example4:\n")
def f():
	try:
		fh = open("testfile6.txt", "r")
	except:
		print("Cannot open this file and hence raise the error")
		raise
	else:
		text = fh.readlines()
		fh.close()

text = []

try:
	f()
except IOError as e:
	print(e)

if text:
	print(text[100])

