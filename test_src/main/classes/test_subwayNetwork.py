import unittest
from subwayNetwork import SubwayNetwork

class TestPreviousStations(unittest.TestCase):
  def test_instance(self): 
    network1 = SubwayNetwork('test_1.csv')
    network2 = SubwayNetwork('test_2.csv')
    network3 = SubwayNetwork('test_3.csv')
    message = "Este no es instancia"
    self.assertIsInstance(network1, SubwayNetwork, message)
    self.assertIsInstance(network2, SubwayNetwork, message)
    self.assertIsInstance(network3, SubwayNetwork, message)

  def test_attributes(self):
    network1 = SubwayNetwork('test_1.csv')
    network2 = SubwayNetwork('test_2.csv')
    network3 = SubwayNetwork('test_3.csv')
    messageDict = "allstations no es un diccionario"
    self.assertIsInstance(network1.allStations, dict, messageDict)
    self.assertIsInstance(network2.allStations, dict, messageDict)
    self.assertIsInstance(network3.allStations, dict, messageDict)
    messageDictKeys = "las keys estan erroneas"
    self.assertEqual(list(network1.allStations.keys()), ['A','B','C','D','E','F','G','H','I'], messageDictKeys)
    self.assertEqual(list(network2.allStations.keys()), ['A','B','C','D','E','F','G','H','I'], messageDictKeys)
    self.assertEqual(list(network3.allStations.keys()), ['A','B','C','D','E','F','G','H','I'], messageDictKeys)

  def test_bfs(self):
    test1_network1 = SubwayNetwork('test_1.csv')
    test2_network1 = SubwayNetwork('test_1.csv')
    test3_network1 = SubwayNetwork('test_1.csv')
    test4_network1 = SubwayNetwork('test_1.csv')
    test5_network1 = SubwayNetwork('test_1.csv')
    test6_network1 = SubwayNetwork('test_1.csv')
    test7_network1 = SubwayNetwork('test_1.csv')
    test8_network1 = SubwayNetwork('test_1.csv')
    test9_network1 = SubwayNetwork('test_1.csv')
    message = 'Error de salida'

    self.assertEqual(test1_network1.bfs('A','F', 'BLANCO'), ['A', 'B', 'C', 'D', 'E'], message)
    self.assertEqual(test2_network1.bfs('A','F', 'ROJO'), ['A', 'B', 'C', 'H'], message)
    self.assertIn(test3_network1.bfs('A','F', 'VERDE'), [['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'G', 'I']], message)

    self.assertEqual(test4_network1.bfs('A', 'G', 'BLANCO'), ['A', 'B', 'C'])    
    self.assertEqual(test5_network1.bfs('A', 'G', 'VERDE'), ['A', 'B', 'C'])    
    self.assertEqual(test6_network1.bfs('A', 'G', 'ROJO'), [])    

    self.assertEqual(test7_network1.bfs('F','A', 'BLANCO'), ['F','E', 'D', 'C', 'B'], message)
    self.assertEqual(test8_network1.bfs('F','A', 'ROJO'), ['F','H', 'C', 'B'], message)
    self.assertIn(test9_network1.bfs('F','A', 'VERDE'), [['F','E', 'D', 'C', 'B'], ['F', 'I', 'G', 'C', 'B',]], message)


    

  # def testPreviousStations(self): #agregar mas test
  #   message = 'Las estaciones previas son erroneas'
  #   station1 = Station('A', 'ROJO', ['B'])
  #   station2 = Station('B', 'VERDE', ['A','C'])
  #   station3 = Station('C', 'BLANCO', ['B'])
  #   station4 = Station('D', 'VERDE', ['F'])
  #   self.assertEqual(station4.previousStations, ['E'], message)
  #   station5 = Station('E', 'VERDE', ['F'])
  #   station2.setPreviousStations(station1)
  #   self.assertEqual(station2.previousStations, ['A'], message)
  #   station3.setPreviousStations(station2)
  #   self.assertEqual(station3.previousStations, ['A', 'B'], message)
  #   station4.setPreviousStations(station5)
  #   self.assertEqual(station5.previousStations, [], message)

if __name__ == '__main__':
  unittest.main()