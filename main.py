import pickle
import os

# 全局变量
maxx = 10  # 最大列数
maxy = 10  # 最大行数

Checkboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              ]

class Save_load:
    def __init__(self, maxx, maxy):
        self.maxx, self.maxy = maxx, maxy
        self.who = 0  # 0: 黑方, 1: 白方, 2: 红方

    def save(self, Checkboard, who):
        fpath = input("请输入保存路径：")
        with open(fpath, "wb") as file:
            self.who = who
            pickle.dump((Checkboard, self.who), file)

    def load(self):
        fpath = input("请输入棋盘路径：")
        if os.path.exists(fpath):
            with open(fpath, "rb") as file:
                status = pickle.load(file)
                return status
        else:
            print("文件不存在")
            return None

# 显示棋盘
def PrintCheckboard(Checkboard):
    print("         五子棋游戏           ")
    print("    0  一  二  三  四  五  六  七  八  九")
    for i in range(maxx):
        print(i, end=" ")
        for j in range(maxy):
            if Checkboard[i][j] == 0:
                print(" 空 ", end="")
            elif Checkboard[i][j] == 1:
                print(" 黑 ", end="")
            elif Checkboard[i][j] == 2:
                print(" 白 ", end="")
            elif Checkboard[i][j] == 3:
                print(" 红 ", end="")
        print()  # 换行


def inRange(Checkboard, xPoint, yPoint):
    return 0 <= xPoint < maxx and 0 <= yPoint < maxy

# 是否五子连线
def checkFiveRow(Checkboard, xPoint, yPoint, xDir, yDir):
    count = 0
    t = Checkboard[xPoint][yPoint]
    x = xPoint
    y = yPoint
    while inRange(Checkboard, x, y) and t == Checkboard[x][y]:
        count += 1
        x += xDir
        y += yDir
    x, y = xPoint, yPoint
    while inRange(Checkboard, x, y) and t == Checkboard[x][y]:
        count += 1
        x -= xDir
        y -= yDir
    if count > 5:
        return True
    else:
        return False

# 判断棋局胜负
def isWin(Checkboard, xPiont, yPoint):
    Result1 = checkFiveRow(Checkboard, xPiont, yPoint, 1, 0)
    Result2 = checkFiveRow(Checkboard, xPiont, yPoint, 0, 1)
    Result3 = checkFiveRow(Checkboard, xPiont, yPoint, 1, 1)
    Result4 = checkFiveRow(Checkboard, xPiont, yPoint, +1, -1)

    if Result1 or Result2 or Result3 or Result4:
        return True
    else:
        return False


# 记录棋盘状态
def Record(Checkboard):
    End_chess = False
    who = 0  # 0: 黑方, 1: 白方, 2: 红方
    while not End_chess:
        player = "黑方" if who == 0 else "白方" if who == 1 else "红方"
        t = input(f"请下子（x,y),现在由{player}下子：")
        if len(t) == 3:
            x = int(t[0])
            y = int(t[2])
            if Checkboard[x][y] == 0:
                Checkboard[x][y] = who + 1  # 1: 黑方, 2: 白方, 3: 红方
                # 判断棋局
                Result = isWin(Checkboard, x, y)
                if Result:
                    print(f"{player}赢")
                    End_chess = True
                else:
                    who = (who + 1) % 3  # 切换到下一个玩家
                    End_chess = False
                    PrintCheckboard(Checkboard)
            else:
                print("该位置已经下子！")
        elif len(t) == 1:
            if t[0] == "S":
                Begin_End.save(Checkboard, who)
            if t[0] == 'L':
                Status = Begin_End.load()
                Checkboard = Status[0]
                who = Status[1]
                PrintCheckboard(Checkboard)
        else:
            print("输入位置有误，请重新输入：")

# 主程序入口
Begin_End = Save_load(maxx, maxy)
Record(Checkboard)