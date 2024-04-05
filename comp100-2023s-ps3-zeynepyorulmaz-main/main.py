def quantify_quary(terrain_data):
  def findthegarbage(terrain_data):
    def helper(terrain_data, i):
      if i == len(terrain_data):
        return []
      elif terrain_data[:i] == [] or terrain_data[i + 1:] == [] or min(max(terrain_data[:i]),
                                                                       max(terrain_data[i + 1:])) < \
              terrain_data[i]:
        return [0] + helper(terrain_data, i + 1)
      else:
        min1 = min(max(terrain_data[0:i]), max(terrain_data[i + 1:len(terrain_data)]))
        return [min1 - terrain_data[i]] + helper(terrain_data, i + 1)

    return helper(terrain_data, 0)
  def sum(list):
    if len(list)< 1:
      return 0
    else:
      return list[0] + sum(list[1:])
  return sum(findthegarbage(terrain_data))









if __name__ == '__main__':
  terrain_data = [3,7,3,4,6,1,9,4,2,6]
  total_garbage_amount = quantify_quary(terrain_data)
  print(total_garbage_amount) # should print 20

  # There are more test cases in `test_main.py`