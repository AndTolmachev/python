def my_round(number, ndigits):
    # округлаяет х до a - го знака после запятой
   if x * 10 ** (a+1) % 10 >= 5:
       return int(x * 10 ** a + 1)/10 ** a
   else:
       return int(x * 10 ** a)/10 ** a


x = float(input('введите числов\n'))
a = int(input('введите, до какого знака после заптяой округлаять\n'))
print( rounding(x, a))
