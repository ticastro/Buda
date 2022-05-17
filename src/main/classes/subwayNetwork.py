from collections import deque
from .station import Station
import os


def skipStation(station, color):
  if station.color == 'BLANCO': return False
  if color != 'BLANCO' and color != station.color:
    station.skipped = True
    return True
  return False

class SubwayNetwork:
  def __init__(self, input):
    self.allStations = {}
    dir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(dir, 'test', input)
    with open(filename, 'r') as file: 
      for i in file:
        lineSplit = i.split(',')
        lineSplit[-1] = lineSplit[-1][:1]
        newStation = Station(lineSplit[0], lineSplit[1], lineSplit[2:])
        self.allStations[f'{newStation.identifier}'] = newStation

  def BFS(self, initialStationId, endStationId, colorTrain):
    # REVISAR CASOS BORDE:
    # 1. Inicio en estación de un color que no puede el tren
    # 2. Final en una estacióon de un color que no puede el tren
    # 3. Estación de llegada es una isla
    # 4. No se llega (3 y 4 pueden ser iguales)
    initialStation = self.allStations[initialStationId] 
    initialStation.colorBFS = 'gray'
    queue = deque([])
    queue.append(initialStationId)
    while len(queue) != 0:
      reviewStationId = queue.popleft()
      reviewStation = self.allStations[reviewStationId]
      for nextStationId in reviewStation.neighbours:
        nextStation = self.allStations[nextStationId]
        if nextStation.colorBFS == 'white':
          nextStation.colorBFS = 'gray'
          if skipStation(nextStation, colorTrain):
            nextStation.setPreviousStations(reviewStation)
            queue.appendleft(nextStation.identifier)
            break
          nextStation.setPreviousStations(reviewStation)
          if nextStation.identifier == endStationId:
            queue = []
            break
          queue.append(nextStation.identifier)
      reviewStation.colorBFS = 'black'
    print(f'El camino para llegar a {endStationId} es {self.allStations[endStationId].previousStations}')