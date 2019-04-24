from random import *

def main():


        while True:

            try:
              n = int(input('Please enter the size of the matrix '))
            except:

               print('Please provide a positive integer')
               continue

            a =[]
            top = 0
            bottom = n - 1
            left = 0
            right = n - 1
            direction = 0

            temp=1
            for i in range(n):
                a.append([])
                for j in range(n):
                    a[i].append(0)

            while (top <= bottom and left <= right):

                if direction == 0:
                    for i in range(left, right + 1):
                        a[top][i]+=temp
                        temp+=1
                    top += 1
                    direction = 1

                elif direction == 1:
                    for i in range(top, bottom + 1):
                        a[i][right]+=temp
                        temp+=1
                    right -= 1
                    direction = 2

                elif direction == 2:
                    for i in range(right, left - 1, -1):
                        a[bottom][i]+=temp
                        temp+=1
                    bottom -= 1
                    direction = 3

                elif direction == 3:
                    for i in range(bottom, top - 1, -1):
                        a[i][left]+=temp
                        temp+=1
                    left += 1
                    direction = 0




            print('The matrix in the wanted form is : ')
            for x in a:
                print(*x, sep=" ")





if __name__ == '__main__':
    main()
