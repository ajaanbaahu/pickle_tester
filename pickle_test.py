import unittest
from pickler import list_pickler, unpickler

class Pickle_tests(unittest.Testcase):
	def test_pickle(self):
		color=[1,2,3,4]
		list_pickler=list_pickler()
		result=list_pickler.pickler(color)
		self.assertEqual(result,[1,2,3,4])
		
#import pickle

#favorite_color=[1,2,3,4]

#pickle.dump(favorite_color, open("save.p","wb"))

#favorite_color_unpickled=pickle.load(open("save.p","rb")