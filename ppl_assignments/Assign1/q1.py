#puzzle
bank1 = {"grass", "goat", "tiger"}
bank2 = set()
invalid1 = {"grass", "goat"}
invalid2 = {"tiger", "goat"}
bank = 1
while len(bank1) != 0:
	if bank == 1:
		if len(bank1) == 3:
			a = bank1.pop()
			if bank1 != invalid1 and bank1 != invalid2:
				print(f"farmer takes {a} from bank1 to bank2")
				bank2.add(a)
				bank = 2
			else:
				bank1.add(a)
		else:
			a = bank1.pop()
			print(f"farmer takes {a} from bank1 to bank2")
			bank2.add(a)
			bank = 2
	else:
		if bank2 == invalid1 or bank2 == invalid2:
			a = bank2.pop()
			print(f"farmer takes {a} from bank2 to bank1")
			bank1.add(a)
		else:
			print("farmer reaches bank2 from bank1")
		bank = 1
