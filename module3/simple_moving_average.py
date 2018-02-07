data = [
(9/18/17, 53.78)
(9/15/17, 53.64)
(9/14/17, 53.63)
(9/13/17, 52.92)
(9/12/17, 52.08)
(9/11/17, 51.82)
(9/8/17, 52.53)
(9/7/17, 52.48)
(9/6/17, 52.04)
]

transformed_data = [] # The SMA data

for index, datum in enumerate(data):
  if index < SMA_WINDOW_SIZE:
      transformed_data.append((datum[0],0))
  else:
      sma = 0
      for i in range(SMA_WINDOW_SIZE):
          sma += float(data[index - i][1])
      sma = sma/SMA_WINDOW_SIZE
      transformed_data.append((datum[0],sma))
