class Station:
  def __init__(self, identifier, color, neighbours):
    self.identifier = identifier
    self.color = color
    self.neighbours = neighbours
    self.bfsState = 'not_visited'
    self.previousStations = []
    self.skipped = False

  def setPreviousStations(self, previousStation):
    previousStationsArray = []
    for i in previousStation.previousStations:
      previousStationsArray.append(i)
    if not previousStation.skipped:
      previousStationsArray.append(previousStation.identifier)
    self.previousStations = previousStationsArray
    return self.previousStations
