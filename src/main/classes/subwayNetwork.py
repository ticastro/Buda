import os
from collections import deque
from .station import Station
from utils import FILE, DIR, WHITE, GREEN, RED, NOT_VISITED_STATE, VISITED_STATE, VISITING_STATE

def skipStation(station, color):
  if station.color == WHITE: return False
  if color != WHITE and color != station.color:
    station.skipped = True
    return True
  return False

def validateStations(network, initialStation, endStation, trainColor):
  initialColor = network.allStations[initialStation].color
  finalColor = network.allStations[endStation].color
  if trainColor != WHITE:
    if initialColor != trainColor and initialColor != WHITE:
      return False
    elif finalColor != trainColor and finalColor != WHITE:
      return False
  return True

class SubwayNetwork:
  def __init__(self, input):
    self.allStations = {}
    dir = os.path.dirname(os.path.realpath(FILE))
    filename = os.path.join(dir, DIR, input)
    with open(filename, 'r') as file: 
      for i in file:
        lineSplit = i.split(',')
        lineSplit[-1] = lineSplit[-1][:1]
        newStation = Station(lineSplit[0], lineSplit[1], lineSplit[2:])
        self.allStations[f'{newStation.identifier}'] = newStation

  def bfs(self, initialStationId, endStationId, colorTrain):
    stationValidator = validateStations(self, initialStationId, endStationId, colorTrain)
    if not stationValidator:
      return self.allStations[endStationId].previousStations
    initialStation = self.allStations[initialStationId] 
    initialStation.bfsState = VISITING_STATE
    queue = deque([])
    queue.append(initialStationId)
    while len(queue) != 0:
      reviewStationId = queue.popleft()
      reviewStation = self.allStations[reviewStationId]
      for nextStationId in reviewStation.neighbours:
        nextStation = self.allStations[nextStationId]
        if nextStation.bfsState == NOT_VISITED_STATE:
          nextStation.bfsState = VISITING_STATE
          if skipStation(nextStation, colorTrain):
            nextStation.setPreviousStations(reviewStation)
            queue.appendleft(nextStation.identifier)
            break
          nextStation.setPreviousStations(reviewStation)
          queue.append(nextStation.identifier)
      reviewStation.bfsState = VISITED_STATE
    return self.allStations[endStationId].previousStations