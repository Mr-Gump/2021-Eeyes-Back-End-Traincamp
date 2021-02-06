import sys


class Player(object):

    def __init__(self , name , mark):
        self.name = name
        self.mark = mark

    def gen_point(self):
        loc = input(f'player {self.name} , please enter a point like 1,2 :')
        return Point.pre_gen(loc , self.mark)


class Point(object):
    chess_type = {0: '-' , 1: 'X' , 2: "O"}

    def __init__(self , x , y , mark):
        self.x = x
        self.y = y
        self.mark = mark

    @classmethod
    def pre_gen(cls , pre_str , mark):
        x = int(pre_str.split(',')[0]) - 1
        y = int(pre_str.split(',')[1]) - 1
        return cls(x , y , mark)


class Chess(object):
    

    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append([0 , 0 , 0])

    def print_chess(self):
        for line in self.board:
            for i in line:
                print(Point.chess_type[i] , end=' ')
            print()

    def insert_to_chess(self , point):

        # 判断是否超出棋盘
        if point.x > 2 or point.y > 2:
            print('落子位置超出棋盘,落子无效!')
            sys.exit()

        # 判断是否该位置还有其他落子
        if self.board[point.x][point.y] != 0:
            print('落子位置有其他落子,落子无效')
            sys.exit()

        self.board[point.x][point.y] = point.mark
        self.print_chess()
        if self.judge() == 1:
            print('player1获胜')
            sys.exit()
        elif self.judge() == 2:
            print('player2 获胜')
            sys.exit()

    def judge(self):
        # type1 同一行都是某位玩家的棋子
        flag = 0
        for line in self.board:
            if line[0] == line[1] and line[2] == line[1]:
                if line[0] == 1:
                    flag = 1
                elif line[0] == 1:
                    flag = 2

        # type2 同一列都是某位玩家的棋子
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[2][i] == self.board[1][i]:
                if self.board[0][i] == 1:
                    flag = 1
                elif self.board[0][i] == 2:
                    flag = 2

        # type3 对角线是某位玩家棋子
        if self.board[0][0] == self.board[1][1] and self.board[2][2] == self.board[1][1]:
            if self.board[0][0] == 1:
                flag = 1
            elif self.board[0][0] == 2:
                flag = 2
        elif self.board[0][2] == self.board[1][1] and self.board[2][0] == self.board[1][1]:
            if self.board[1][1] == 1:
                flag = 1
            elif self.board[1][1] == 2:
                flag = 2

        return flag


if __name__ == '__main__':
    player1 = Player('ty' , 1)
    player2 = Player('gwh' , 2)
    chess = Chess()
    print('-----比赛开始-------')
    while True:
        current_point = player1.gen_point()
        chess.insert_to_chess(current_point)
        current_point = player2.gen_point()
        chess.insert_to_chess(current_point)
