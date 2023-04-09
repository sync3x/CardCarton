#!/usr/bin/env python3
#
q1={
  'z1':[
    [ 'M', 1,1, ],
    [ 'L', 2,2, ],
  ],'z2':[
    [ 'M', 3,3, ],
  ( [ 'L', 4,4, ],
    [ 'M', 5,5, ] ) if 1==0 else
  ( [ 'L', 6,6, ],
    [ 'M', 7,7, ] ),
    [ 'L', 8,8, ],
  ],
}

for k, v in q1.items():
  print('[['+k+']]')
  for a in v:
    print('['+str(len(a))+']')
    for b in a:
      print(b)
