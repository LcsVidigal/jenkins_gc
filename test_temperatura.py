import unittest
from temperatura import fahrenheit_para_celsius, celsius_para_fahrenheit

class TestTemperatura(unittest.TestCase):
    
    def test_fahrenheit_para_celsius(self):
        # Testa o ponto de congelamento da água
        self.assertEqual(fahrenheit_para_celsius(32), 0)
        
    def test_celsius_para_fahrenheit(self):
        # Testa o ponto de ebulição da água
        self.assertEqual(celsius_para_fahrenheit(100), 212)

if __name__ == '__main__':
    unittest.main()