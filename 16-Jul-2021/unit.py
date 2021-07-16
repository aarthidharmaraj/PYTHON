import unittest
  
class Teststring(unittest.TestCase):
    def setUp(self):
        pass
  
    # Returns True if the string is equal
    def test_str(self):
        ch="hai"
        self.assertEqual( ch, 'hai')
  
    # Returns True if the string is in upper case.
    def test_upper(self):        
        self.assertEqual('welcome'.upper(), 'WELCOME')
  
    # Returns TRUE if the string is in uppercase
    # else returns False.
    def test_isupper(self):        
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())
  
    # Returns true if the string is stripped and  matches the given output.
    def test_strip(self):        
        samp = 'unit test cases'
        self.assertEqual(samp.strip('unit'), 'test cases')
  
    # Returns true if the string splits and matches the given output.
    def test_split(self):        
        s = 'python programming'
        self.assertEqual(s.split(), ['python', 'programming'])
        with self.assertRaises(TypeError): 
            s.split(2)
    
    def test_ave(self):
        ls=[1,3,5,7,3,2,8]
        avg=sum(ls)/len(ls)
        self.assertEqual(avg,4.14)

    def test_even(self):
        for i in range(0,5):
            self.assertEqual(i%2,0,"It is not equal")

if __name__ == '__main__':
    unittest.main()