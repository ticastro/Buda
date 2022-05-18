import os
from utils.selectors import inputSelector, stationSelector, colorSelector
from classes import SubwayNetwork


def main():
  file = inputSelector()
  network = SubwayNetwork(file)
  initialStation = stationSelector(1, network)
  endStation = stationSelector(2, network)
  while initialStation == endStation:
    endStation = stationSelector(3, network)
  color = colorSelector()
  network.bfs(initialStation, endStation, color)

if __name__ == '__main__':
  main()