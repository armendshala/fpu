import sys
import math

if __name__ == '__main__':
		
	# i = 1
	# j = 2

	# j = j - 1

	# print id(i)
	# print id(j)

	# longnum = 530298402983423948129380192L
	# longnum += 1
	# complex = 3.14j

	# print complex
	# print longnum

	# print sys.maxint
	# print sys.float_info


	# # --------------------------------------------------------

	# # Number type conversion
	# print int(2.5)
	# print long(2.5)
	# print float(2)
	# print complex(2)
	# print complex(2,0)

	# # --------------------------------------------------------

	# # Math functions

	# print abs(-3) # 3
	# print math.ceil(4.1) # 5
	# print math.ceil(-2.8) # -2
	# print cmp(3,2) # -1 if x < y, 1 if x > y, 0 if x == y
	# print math.exp(1) # 2.71 - e^1
	# print math.fabs(-1) #  1.0 - float abs
	# print math.floor(1.2) # 1
	# print math.log(2) # 0.69
	# print math.log10(2) # 0.30
	# print max(1,2) # 2
	# print min(1,2) # 1
	# print math.modf(2.5) # (0.5,2.0)
	# print pow(2,2) # 4
	# print round(0.5) # 1
	# print round(-0.5) # -1
	# print math.sqrt(9) # 3.0


	# # --------------------------------------------------------

	# Strings operations
	# print "Armend" + "Shala" # ArmendShala
	# print "Armend " + "Shala" # Armend Shala
	# print "Armend","Shala" # Armend Shala
	# print "Armend "*2 # Armend Armend

	# # String slicing
	# print "Armend"[0] # A
	# print "Armend"[0:2] # Ar
	# print "Armend"[:2] # Ar
	# print "Armend"[2:] # mend
	# print "Armend"[::] # Armend
	# print "Armend"[:] # Armend
	# print "Armend"[::-1] # dnemrA

	# # String membership
	# print "A" in "Armend" # True
	# print "A" not in "Armend" # False

	# # Identity 
	# print 'A' is 'A'
	# print 'Z' is not 'A'

	# # String Raw
	# print r"Armend\n" # Raw string
	# print "Armend\n" # No Raw string - newline at the end.

	# # String format
	# print '%s'  % "Armend" # Armend
	# print '%s is %d yrs old.'  % ("Armend",20) # Armend is 20 yrs old
	# print '{0} is {1} yrs old.'.format("Armend",20) # Armend is 20 yrs old

	# # String unicode
	# print u'Armend' # Armend , 16 bit unicode
	# print 'Armend' # Armend , 8 bit ascii

	# # String conversation functions
	# print 'armend'.capitalize() # Armend
	# print 'ARMEND'.lower() # armend
	# print 'armend'.upper() # ARMEND
	# print 'ArmEnD'.swapcase() # aRMeNd
	# print 'armend shala'.title() # Armend Shala
	# print 'Armeend'.count('e') # 2

	# # String comparison
	# print 'armend'.islower() # True
	# print 'armend'.isupper() # False
	# print 'armend'.isdigit() # False
	# print u'armend'.isdecimal() # False
	# print u'armend'.isnumeric() # False
	# print 'armend'.isalpha() # True
	# print 'a-'.isalnum() # False

	# # String padding
	# print 'Armend'.rjust(12,'*') # ARMEND******
	# print 'Armend'.ljust(12,'*') # ******ARMEND
	# print 'Armend'.center(12,'*') # ****ARMEND****
	# print 'Armend'.zfill(10) # 00000ARMEND

	# # String find functions
	# print 'Armend'.find('r') # 1
	# print 'Armend'.find('Z') # -1
	# print 'Armend'.index('r') # 1
	# # print 'Armend'.index('Z') #  valueError
	# print 'Armend'.rfind('d') # 5

	# # String replace
	# print 'Armend'.replace('A','B')
	# print 'Armend Shala'.split(' ')
	# print 'Armend Shala'.split('a') # ['Armend Sh','l','']
	# print 'A\nrm\nen\nd'.splitlines() # ['A']
	# print 'A\nrm\nen\nd'.splitlines(1)
	# print ''.join(['A','R','M','E','N','D'])

	# # String misc
	# print '		Armend'.lstrip()
	# print '*****Armend'.lstrip('*')
	# print 'Armend*****'.rstrip('*')
	# print '*****Armend*****'.strip('*')
	# print len('Armend')


	# #----------------------------------------------------------------
	# LIST
	
	list1 = []
	list2 = list()
	
	# print type(list1)
	# print type(list2)

	list = [1,2.0,2L,'A',['Another list'],('Tuple'),{'SET'},{'Dictionary':{'Another key':'value'}},None,object,]
	# print len(list)

	# Append
	list1.append(1)
	print list1

	# # Update element
	# print list1
	# list1[0] = 2
	# print list1

	# # Delete element
	# del list[0]
	# list1.remove(1)
	# print list1
	# del list1
	# print list1

	# # Count
	print list1.count(1)

	# # Extend list
	list1.extend([1,2,3,3])
	print list1

	# # Find index of an element
	print list1.index(1)

	# Insert element at position
	list1.insert(1,10)
	print list1

	# # Get last item
	print list1.pop()

	# # Reverse list
	# print list1.reverse() # return None, replace in-Place
	# print reversed(list1)
	# or
	# print list1[::-1]

	# # # Sort
	# list1.sort()
	# print list1

	# # Membership
	# print 3 in [1,2,3]
	# print 'Z' in [1,2,3,4]

	# # # Iterate loop
	# for i in [1,2,3]: print i

	# # Identity 
	# print 3 is [1,2,3]
	# list1 = [1]
	# list2 = [1]

	# print id(list1)
	# print id(list2)

	# #----------------------------------------------------------------
	# # TUPLES
	
	# tuple1 = ()
	# tuple2 = tuple()

	# print type(tuple1)
	# print type(tuple2)

	# tuple = (1,2.0,2L,'A',['Another tuple'],('Tuple'),{'SET'},{'Dictionary':{'Another key':'value'}},None,object,)
	# print len(tuple)
	# print tuple[0]
	# print tuple[1:3]
	# print tuple[2:]
	# print tuple * 2
	# print tuple + ('Another tuple') #

	# # Update element
	# print tuple[0]
	# tuple[0] = 2
	# print tuple[0]

	# # Delete element
	# del tuple[0]
	# print tuple
	# del tuple
	# print tuple

	# # Membership
	# print 3 in [1,2,3]
	# print 'Z' in [1,2,3,4]

	# # Iterate loop
	# for i in (1,2,3): print i

	# # Identity 
	# print 3 is (1,2,3)
	# list1 = (1)
	# list2 = (1)

	# print id(list1)
	# print id(list2)

	# # ------------------------------------------------------------------------------------------------
	# # Dictionary

	# Init
	dict1 = {}
	dict2 = dict()

	list1 = []
	list2 = list()

	tuple1 = ()
	tuple2 = tuple()

	set1 = {}
	set2 = set()

	
	# frozenset2 = frozenset()


	# # Type
	# print type(dict1)
	# print type(dict2)

	# # Identity
	# print id(dict1)
	# print id(dict2)

	# # Compare
	# print cmp({2:6},{2:7})

	# # Assigment 
	# dict1['1'] = 1
	# dict1['2'] = 1
	# print dict1['1']

	# # Update
	# dict1['1'] = 2
	# print dict1['1']

	# # Delete
	# # del dict1['1']
	# # print dict1['1']

	# # Len
	# print len(dict1)

	# # Convert dict to string
	# print str(dict1)

	# # Clear all keys and values
	# print dict1.clear()

	# # Copy dictionary
	# dict3 = dict1.copy()
	# print dict3

	# # Create a dict from tuple
	# print dict1.fromkeys((1,2))

	# # Get dict value from key
	# print dict1.get('1')
	# print dict1.get('1',"not found")

	# # Check exists key
	# print dict1.has_key('1')

	# # Convert dictionary to list of tuples
	# print dict1.items()

	# # Get only dict keys to list
	# print dict.keys()

	# # Get only values from dict
	# print dict.values()


	# # Set a default value to key if not exists
	# print dict.setdefault('1','100')
	# print dict.setdefault('2','100')

	# # Update dictionary (extend)
	# print dict.update(dict3)

	# # SETS
	#  SETS are just like dict. but only contains keys

	# # FROZENSET
	# FROZENSET are immutable sets

	# # --------------------------------------------------------------------------------

	# LOOPS

	# while True:
	# 	print 'Running inf.'

	# i = 0
	# while i < 10:
	# 	print i
	# 	i += 1

	# for i in range(10): print i

	# for i in range(11):
	# 	for j in range(11):
	# 		print i*j

	# for l in [1,2,3]: print l

	# for t in (1,2): print t 

	# for k,v in {'A':'B'}.items():
	# 	print 'key: %s, value: %s' % (k,v)

	# for k in {'A':'B'}.keys(): print k

	# for v in {'A':'B'}.values(): print v

	# for i in range(10):
	# 	print i
	# else:
	# 	print 'done'

	# for i in range(10):
	# 	print i
	# 	if i > 5:
	# 		break
	# else:
	# 	print 'done'

	# k = 10
	# while k < 10:
	# 	print k
	# 	k += 1
	# else:
	# 	print k

	# Conditions
	# k = 0
	# if k == 0:
	# 	print 'k is:',k

	# k = -1
	# if k >= 0:
	# 	print 'k > 0'
	# else:
	# 	print 'k < 0' 

	# k = 5
	# if k < 0:
	# 	print 'k < 0'
	# elif k > 0 and k < 10:
	# 	print 'k > 0 and k < 10'
	# else:
	# 	print 'k > 10'

	# if 3 in [1,2,3]:
	# 	print '3 is in list'
	# else:
	# 	print '3 is not in list'

	# for i in range(10):
	# 	if i == 5:
	# 		print 'continue'
	# 		continue
	# 	print i
	# else:
	# 	print 'done'

	# for i in range(10):
	# 	if i == 5:
	# 		print 'break'
	# 		break
	# 	print i
	# else:
	# 	print 'done'

	# for i in range(10):
	# 	if i == 5:
	# 		pass
	# 	print i

	# list = ['Armend','Shala']
	# for k,v in enumerate(list):
	# 	print list[k]


	# list comprehesions

	# regex