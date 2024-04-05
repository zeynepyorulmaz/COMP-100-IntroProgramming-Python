"""
Do not modify this file unless instructed.
"""

try:
	from part1_a import is_there_a_solution
except:
	pass

try:
	from part1_b import get_the_solution
except:
	pass

try:
	from part2_a import is_there_a_solution_C1
except:
	pass

try:
	from part2_b import get_the_solution_C1
except:
	pass

try:
	from part2_c import is_there_a_solution_C2
except:
	pass

def test_part1_a_0():
  assert is_there_a_solution(3, 'O|X|X|O') == 'NO'

def test_part1_a_1():
  assert is_there_a_solution(7, 'OO|OX|OO|XX|XO|OO') == 'YES' 
  
def test_part1_a_2():  
  assert is_there_a_solution(8, 'OOOO|OXXO|XOXO|OOXX') == 'YES' 

def test_part1_b_0():
  assert get_the_solution(3, 'O|X|X|O') == 'X'  

def test_part1_b_1():
  assert get_the_solution(7, 'OO|OX|OO|XX|XO|OO') == 'SS|SX|SS|XX|XS|SO'

def test_part1_b_2():
  assert get_the_solution(8, 'OOOO|OXXO|XOXO|OOXX') == 'SSSS|SXXS|XSXS|OOXX'


def test_part2_a_0():
  assert  is_there_a_solution_C1(6, 3, 2, 'OO|OX|OO|XX|XO|OO') == 'YES' 

def test_part2_a_1():
  assert is_there_a_solution_C1(8, 4, 4, 'OOOO|OXXO|XOXO') == 'YES'

def test_part2_a_2():
  assert is_there_a_solution_C1(10, 2, 6, 'OOOOOO|OOOXXO|XXOOXO') == 'NO' 

def test_part2_b_0():
  assert get_the_solution_C1(6, 3, 2, 'OO|OX|OO|XX|XO|OO') == 'SS|OX|SS|XX|XO|SS'

def test_part2_b_1():
  assert get_the_solution_C1(8, 4, 4, 'OOOO|OXXO|XOXO') == 'SSSS|SXXS|XSXS'

def test_part2_b_2():
  assert get_the_solution_C1(10, 2, 6, 'OOOOOO|OOOXXO|XXOOXO') == 'X' 


def test_part2_c_0():
  assert is_there_a_solution_C2(6, 3, 2, 'OO|OX|OO|XX|XO|OO') == 'YES'

def test_part2_c_1():
  assert is_there_a_solution_C2(8, 4, 4,'OXXO|OXXO|OOOO') == 'NO'

def test_part2_c_2():
  assert is_there_a_solution_C2(12, 3, 6, 'OOOOOO|OOXXXO|XOOOOX') == 'NO' 


if __name__ == '__main__':

  tests = [test_part1_a_0, test_part1_a_1, test_part1_a_2, test_part1_b_0, test_part1_b_1, test_part1_b_2, test_part2_a_0, test_part2_a_1, test_part2_a_2, test_part2_b_0, test_part2_b_1, test_part2_b_2, test_part2_c_0, test_part2_c_1, test_part2_c_2]

  print('Points:')
  for t in tests:
    try:
      t()
      print(str(t).split()[1], 1)
    except AssertionError:
      print(str(t).split()[1], 0)
