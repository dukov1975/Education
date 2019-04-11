def summ_squares(data_array):
  summ = 0
  for item in data_array:
    try:
        value = int(item)
        summ += value ** 2
    except ValueError:
        pass
  return summ

data = [1, '5', 'abc', 20, '2']
print('Сумма квадратов = ', summ_squares(data))