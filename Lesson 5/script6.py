def func(x):
	pass

lista1 = ['A','B','C']
lista2 = [chr(x) for x in range(65,72)]

if __name__ == '__main__':
	
	print 'I kena marr ',lista1
	print 'Nuk i kena marr ',lista2
	print 'Kena me i marr ',[
								x for x in lista2 
									if x not in lista1
							]


	print {2,2,1,1,2,3,1,1}