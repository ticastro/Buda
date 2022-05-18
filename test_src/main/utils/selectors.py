import os

from .const import (FILE, DIR, FILE_SELECTION_OPEN, WRONG_INPUT, ENTER_FILE_SELECTION,
 FINAL_STATION_INPUT, INITIAL_STATION_INPUT, SAME_STATION_INPUT, TRAIN_COLOR_INPUT, WHITE,
 RED, GREEN)

def inputValidator(input, max): 
  if not 0 < int(input) < max:
    return False
  return True

def inputSelector():
  dir = os.path.dirname(os.path.realpath(FILE))
  filename = os.path.join(dir, DIR)
  dirFiles = os.listdir(filename)
  print(FILE_SELECTION_OPEN)
  for i in range(len(dirFiles)):
    print(f'{i + 1}.  {dirFiles[i]}')
  try:
    fileSelection = int(input(ENTER_FILE_SELECTION))
    validInput = inputValidator(fileSelection, len(dirFiles) + 1) 
  except:
    validInput = False
  while not validInput:
    try:
      fileSelection = int(input(WRONG_INPUT))
      validInput = inputValidator(fileSelection, len(dirFiles) + 1)
    except:
      validInput = False
      continue 
  return dirFiles[fileSelection - 1]

def stationSelector(case, network):
  stations = list(network.allStations.keys())
  print(type(stations))
  print(stations)
  for i in range(len(stations)):
    print(f'{i+1}.  {stations[i]}')
  try:
    if case == 1:
      station = int(input(INITIAL_STATION_INPUT))
    elif case == 2:
      station = int(input(FINAL_STATION_INPUT))
    elif case == 3:
      station = int(input(SAME_STATION_INPUT))
    validInput = inputValidator(station, len(stations) + 1) 
  except:
    validInput = False
  while not validInput:
    try:
      station = int(input(WRONG_INPUT))
      validInput = inputValidator(station, len(stations) + 1)
    except:
      validInput = False
      continue 
  return stations[station - 1] 

def colorSelector():
  colors = [WHITE, GREEN, RED]
  for i in range(len(colors)):
    print(f'{i+1}.  {colors[i]}')
  try:
    color = int(input(TRAIN_COLOR_INPUT))
    validInput = inputValidator(color, len(colors) + 1) 
  except:
    validInput = False
  while not validInput:
    try:
      color = int(input(WRONG_INPUT))
      validInput = inputValidator(color, len(colors) + 1) 
    except:
      validInput = False
  return colors[color - 1]