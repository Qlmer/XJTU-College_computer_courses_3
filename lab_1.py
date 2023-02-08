from random import randint


def judge_RPS(f, s):
    '''rock is 1,scissors is 2,paper is 3
    >>> RPS(1,2)
    True
    >>> RPS(3,2)
    False
    '''
    if f - s == -1 or f - s == 2:
        return True
    else:
        return False


def computer_play():
    '''computer player'''
    return randint(1, 3)


def inactive_player():
    a = int(input('the rock is 1,scissors is 2,paper is 3,please input your choice '))
    if a == 1 or a == 2 or a == 3:
        return a
    else:
        print("the rock is 1,scissors is 2,paper is 3,please check your input")
        inactive_player()


def play_with(num_play):
    '''choice the number of human players'''

    if num_play == 0:
        play(computer_play, computer_play)
    if num_play == 1:
        play(inactive_player, computer_play)
    else:
        print('num_players must be 0 or 1.')


def play(p1, p2):
    print('this is the first player turn')
    c1 = p1()
    print('this is the second player turn')
    c2 = p2()
    if judge_RPS(c1, c2) is True:
        print('the first player wins')
        scoreboard(1)
    else:
        print('the second player wins')
        scoreboard(2)


def scoreboard(n):
    global the_first, the_second
    if n == 1:
        the_first += 1
    else:
        the_second += 1
    print('the first player score is %d,the second score is %d' %
          (the_first, the_second))


def continue_play():
    print("if you want to continue play,input 1")
    a = input()
    if input == '1':
        new_play()
    else:
        return


the_first = 0
the_second = 0


def new_play():
    num__play = int(input("choice the number of human players "))
    play_with(num__play)
    continue_play()


new_play()
