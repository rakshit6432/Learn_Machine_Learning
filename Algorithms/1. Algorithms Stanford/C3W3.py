#greedy algorithm from the lectures on Huffman coding

import sys
from heapq import *

sys.setrecursionlimit(1500)

V = {}

class BinaryTree:
  """A special BT for Huffman's algorithm"""

  def __init__(self, left = None, right = None, value = None):
    self.value = value
    self.left = BinaryTree(None, None, left) if left else None
    self.right = BinaryTree(None, None, right) if right else None
    V[self.value] = self

  def getLength(self, fn):
    if not (self.left and self.right):
      return 0

    leftLength = self.left.getLength(fn) if self.left else 0
    rightLength = self.right.getLength(fn) if self.right else 0

    return 1 + fn(leftLength, rightLength)


def huffman(alphabet):

  if len(alphabet) == 2:
    return BinaryTree(alphabet[0][1], alphabet[1][1])

  (pa, a) = heappop(alphabet)
  (pb, b) = heappop(alphabet)

  ab = str(a) + '_' + str(b)

  heappush(alphabet, (pa + pb, ab))

  T = huffman(alphabet)

  V[ab].__dict__.update(BinaryTree(a, b).__dict__)

  return T


if __name__ == '__main__':
  input_file_name = 'huffman.txt'

  # Build alphabet heap from file
  alphabet = []

  with open(input_file_name) as f:
    f.readline() # 1000 chars

    char_name = 0
    for line in f:
      char_name += 1
      heappush(alphabet, (int(line.rstrip()), char_name))

  tree = huffman(alphabet)

  print(tree.getLength(min)) # 9 bits
  print(tree.getLength(max)) # 19 bits



#the dynamic programming algorithm for computing a maximum-weight independent set of a path graph
"""
import time
start_time = time.time()

def mwis(weights):
  n = len(weights) - 1
  A = [0, weights[1]]

  for i in range(2, n + 1):
    A.append(max(A[i - 1], A[i - 2] + weights[i]))

  i = n
  S = set()

  while i >= 1:
    if A[i - 1] >= A[i - 2] + weights[i]:
      i -= 1
    else:
      S.add(i)
      i -= 2

  return S



if __name__ == '__main__':
  input_file_name = 'mwis.txt'

  weights = [None]

  with open(input_file_name) as f:
    f.readline() # 1000 weights

    for line in f:
      weights.append(int(line.rstrip()))

  S = mwis(weights)

  v = [1, 2, 3, 4, 17, 117, 517, 997]

  print("".join(["1" if i in S else "0" for i in v]))

print("--- %s seconds ---" % (time.time() - start_time))

"""