def bubblesort( A ):
  for i in range( len( A ) ):
    for k in range( len( A ) - 1, i, -1 ):
      if ( A[k] < A[k - 1] ):
        swap( A, k, k - 1 )

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

if __name__=='__main__':
    A=list(map(int, input("input: ").split(',')))
bubblesort(A)
print(A)


