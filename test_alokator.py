import unittest
from kod_pocetna_verzija import Element, Alokator

class TestElement(unittest.TestCase):
    def test_getSize(self):
        e = Element((6,8,"ld"))
        self.assertEqual(e.getSize(), 3)

    def test_getList(self):
        e = Element((6,8,"ld"))
        self.assertEqual(e.getList(), (6, 8, "ld"))

class TestAlokator(unittest.TestCase):
    def test_getAllocatedList(self):
        a = Alokator(10, "BestFit")
        self.assertEqual(a.getAllocatedList(), [0,1,0,0,0,1,1,1,0,1])

    def test_getList(self):
        a = Alokator(10, "BestFit")
        self.assertEqual(a.getList(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_algoritam(self):
        e = Element((6,8,"ld"))
        a = Alokator(10, "BestFit")
        prvo, drugo = a.algoritam(e)
        self.assertEqual(prvo, 2) # Update the expected values accordingly
        self.assertEqual(drugo, [0, 0, 6, 8, "ld", 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()


