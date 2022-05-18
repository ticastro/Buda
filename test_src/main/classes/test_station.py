import unittest
from station import Station

class TestPreviousStations(unittest.TestCase):
  def test_instance(self): 
    station1 = Station('A', 'ROJO', ['B'])
    station2 = Station('B', 'VERDE', ['A','C'])
    station3 = Station('C', 'BLANCO', ['B'])
    message = "Este no es instancia"
    self.assertIsInstance(station1, Station, message)
    self.assertIsInstance(station2, Station, message)
    self.assertIsInstance(station3, Station, message)

  def testPreviousStations(self): #agregar mas test
    message = 'Las estaciones previas son erroneas'
    station1 = Station('A', 'ROJO', ['B'])
    station2 = Station('B', 'VERDE', ['A','C'])
    station3 = Station('C', 'BLANCO', ['B'])
    station4 = Station('D', 'VERDE', ['F'])
    station5 = Station('E', 'VERDE', ['F'])
    station4.setPreviousStations(station5)
    self.assertEqual(station4.previousStations, ['E'], message)
    station2.setPreviousStations(station1)
    self.assertEqual(station2.previousStations, ['A'], message)
    station3.setPreviousStations(station2)
    self.assertEqual(station3.previousStations, ['A', 'B'], message)
    self.assertEqual(station5.previousStations, [], message)

if __name__ == '__main__':
  unittest.main()