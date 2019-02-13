## This code is intended to make a tic tac toe game for both average mode and unbeatable mode
import random

board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

winning_pairs= ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])



def show_board():   ## This function is intended to show the board in the beginning of the referral to the loop.

    print (board[0],'|',board[1],'|',board[2])
    print('----------')
    print (board[3],'|',board[4],'|',board[5])
    print('----------')
    print (board[6],'|',board[7],'|',board[8])



def finding_the_winner():

        result=True


        for  i in range(len(winning_pairs)):

                first_checking_value=winning_pairs [i][0]
                second_checking_value=winning_pairs[i][1]
                third_checking_value=winning_pairs[i][2]



                if board[first_checking_value]=='x' and  board[second_checking_value]=='x' and board[third_checking_value]=='x':

                    print('Game Over,player x wins')

                    result=False

                    return result


                elif board[first_checking_value]=='o' and  board[second_checking_value]=='o' and board[third_checking_value]=='o':

                    print('Game Over, player o wins')

                    result=False

                    return result

  ## Making an advanced machanism using Minimax AI.


        def advanced_mode():  ##to be worked on
            pass

        


def main():

        counter=0


        show_board()
        while True:
            try:
                choice=int(input('Select a spot: '))

            except:
                print("Please enter a number from 0-8")
                continue


            if board[choice] !='x' and board[choice]!='o':
                 board[choice]='x'
                 counter+=1
            else:

                print('This spot is taken')
                continue

            while True:
                    if counter==9:
                        break;
                    random.seed()
                    computer_choice=random.randint(0,8)
                    if board[computer_choice]!='x' and board[computer_choice] !='o':
                        board[computer_choice]='o'
                        counter+=1
                        print(counter)
                        break;



            show_board()

            result=finding_the_winner()

            if result == False:

                break;

            elif result==True:
                print("Game Drawn")
                break;







if __name__ == '__main__':

    main()


