try:
  from main import quantify_quary
except ImportError:
  print("Cannot import quantify_quary from main.py. Check for syntax or indentation errors")
  exit(-1)

def is_approx(pred, gt, allowance= 0.1):
  if gt == 0:
    return abs(pred) <= 0.1
  else:
    return abs((pred-gt)/gt) <= allowance

def test_1():
  terrain_data = [3,7,3,4,6,1,9,4,2,6]
  gt = 20
  pred = quantify_quary(terrain_data)
  
  assert is_approx(pred, gt)

def test_2():
  terrain_data = [8, 8, 10, 5, 8, 2, 0, 0, 8]
  gt = 25
  pred = quantify_quary(terrain_data)
  
  assert is_approx(pred, gt)


def test_3():
  terrain_data = [3, 2, 7, 5, 2] 
  gt = 1
  pred = quantify_quary(terrain_data)

  assert is_approx(pred, gt)

def test_4():
  terrain_data = [4, 4, 2, 3, 8, 7] 
  gt = 3
  pred = quantify_quary(terrain_data)

  assert is_approx(pred, gt)

def test_5():
  terrain_data = [1.688866652527019,
                  7.127714738753489,
                  1.664148285350291,
                  1.1857284627607723,
                  7.386050667061763,
                  6.325197539612684,
                  2.084934233264606] 
  gt = 11.405552729395914
  pred = quantify_quary(terrain_data)

  assert is_approx(pred, gt)

def test_6():
  terrain_data = [1.4253589545271195,
                  0.2062841866165699,
                  4.972810527225632,
                  0.7930056924214379,
                  5.9889182172799345,
                  9.266361488209565,
                  7.954979086533492,
                  9.594010482478732,
                  5.76806983528341,
                  8.450886281174109] 
  gt = 9.393078450281514
  pred = quantify_quary(terrain_data)

  assert is_approx(pred, gt)

def test_7():
  terrain_data = [6, 1, 6, 10, 8, 2, 0]
  gt = 5
  pred = quantify_quary(terrain_data)

  assert is_approx(pred, gt)

def test_8():
  terrain_data = [0, 10, 6, 5] 
  gt = 0
  pred = quantify_quary(terrain_data)

  assert is_approx(pred, gt)

def test_9():
  terrain_data = [7.670535679440946,
                  5.6300099461322315,
                  0.06608653898793837,
                  6.494259942102896,
                  4.623119309949422,
                  8.51554707642832] 
  gt = 13.868666980591296
  pred = quantify_quary(terrain_data)

  assert is_approx(pred, gt)

def test_10():
  terrain_data = [4.749970127517784,
                  1.0378757106308933,
                  7.950535325051675,
                  1.9283904815129616,
                  1.3034004926933263,
                  9.622688829064519,
                  2.420069996959062,
                  5.529349379105618,
                  4.576026764387761,
                  4.164288943070423] 
  gt = 19.490653474930507
  pred = quantify_quary(terrain_data)

  assert is_approx(pred, gt)



if __name__ == '__main__':

  tests = [test_1, test_2, test_3, test_4]

  for t in tests:
    try:
      t()
      print('Passed', t.__name__)
    except AssertionError:
      print('Failed', t.__name__)