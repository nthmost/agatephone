import unittest
from death_horoscope import get_california_zodiac_sign

class TestCaliforniaZodiacSignDistribution(unittest.TestCase):
    
    def test_california_condor(self):
        # Test boundaries for "California Condor" in January
        self.assertEqual(get_california_zodiac_sign(1, 1), "California Condor")
        self.assertEqual(get_california_zodiac_sign(1, 19), "California Condor")
        
        # Test boundaries for "California Condor" in December
        self.assertEqual(get_california_zodiac_sign(12, 22), "California Condor")
        self.assertEqual(get_california_zodiac_sign(12, 31), "California Condor")

    def test_common_raven(self):
        # Test boundaries for "Common Raven"
        self.assertEqual(get_california_zodiac_sign(1, 20), "Common Raven")
        self.assertEqual(get_california_zodiac_sign(2, 18), "Common Raven")

    def test_starfish(self):
        # Test boundaries for "Starfish"
        self.assertEqual(get_california_zodiac_sign(2, 19), "Starfish")
        self.assertEqual(get_california_zodiac_sign(3, 20), "Starfish")

    def test_turkey_vulture(self):
        # Test boundaries for "Turkey Vulture"
        self.assertEqual(get_california_zodiac_sign(3, 21), "Turkey Vulture")
        self.assertEqual(get_california_zodiac_sign(4, 19), "Turkey Vulture")

    def test_western_gull(self):
        # Test boundaries for "Western Gull"
        self.assertEqual(get_california_zodiac_sign(4, 20), "Western Gull")
        self.assertEqual(get_california_zodiac_sign(5, 20), "Western Gull")

    def test_isopod(self):
        # Test boundaries for "Isopod"
        self.assertEqual(get_california_zodiac_sign(5, 21), "Isopod")
        self.assertEqual(get_california_zodiac_sign(6, 20), "Isopod")

    def test_dungeness_crab(self):
        # Test boundaries for "Dungeness Crab"
        self.assertEqual(get_california_zodiac_sign(6, 21), "Dungeness Crab")
        self.assertEqual(get_california_zodiac_sign(7, 22), "Dungeness Crab")

    def test_pacific_octopus(self):
        # Test boundaries for "Pacific Octopus"
        self.assertEqual(get_california_zodiac_sign(7, 23), "Pacific Octopus")
        self.assertEqual(get_california_zodiac_sign(8, 22), "Pacific Octopus")

    def test_grey_wolf(self):
        # Test boundaries for "Grey Wolf"
        self.assertEqual(get_california_zodiac_sign(8, 23), "Grey Wolf")
        self.assertEqual(get_california_zodiac_sign(9, 22), "Grey Wolf")

    def test_hagfish(self):
        # Test boundaries for "Hagfish"
        self.assertEqual(get_california_zodiac_sign(9, 23), "Hagfish")
        self.assertEqual(get_california_zodiac_sign(10, 22), "Hagfish")

    def test_sea_cucumber(self):
        # Test boundaries for "Sea Cucumber"
        self.assertEqual(get_california_zodiac_sign(10, 23), "Sea Cucumber")
        self.assertEqual(get_california_zodiac_sign(11, 21), "Sea Cucumber")

    def test_carrion_beetle(self):
        # Test boundaries for "Carrion Beetle"
        self.assertEqual(get_california_zodiac_sign(11, 22), "Carrion Beetle")
        self.assertEqual(get_california_zodiac_sign(12, 21), "Carrion Beetle")

    def test_no_overlapping_signs(self):
        # Test middle dates in each sign's range to ensure proper sign boundaries
        self.assertEqual(get_california_zodiac_sign(1, 10), "California Condor")
        self.assertEqual(get_california_zodiac_sign(2, 5), "Common Raven")
        self.assertEqual(get_california_zodiac_sign(3, 15), "Starfish")
        self.assertEqual(get_california_zodiac_sign(4, 10), "Turkey Vulture")
        self.assertEqual(get_california_zodiac_sign(5, 10), "Western Gull")
        self.assertEqual(get_california_zodiac_sign(6, 10), "Isopod")
        self.assertEqual(get_california_zodiac_sign(7, 10), "Dungeness Crab")
        self.assertEqual(get_california_zodiac_sign(8, 10), "Pacific Octopus")
        self.assertEqual(get_california_zodiac_sign(9, 10), "Grey Wolf")
        self.assertEqual(get_california_zodiac_sign(10, 10), "Hagfish")
        self.assertEqual(get_california_zodiac_sign(11, 10), "Sea Cucumber")
        self.assertEqual(get_california_zodiac_sign(12, 10), "Carrion Beetle")

if __name__ == "__main__":
    unittest.main()

