import random

def 数字炸弹游戏():
    print("欢迎来到数字炸弹游戏！")
    print("我已经想好了一个1到100之间的数字。")
    print("你可以开始猜了，猜错了炸弹就会爆炸！")

    # 生成一个1到100之间的随机数
    正确数字 = random.randint(1, 100)
    猜测次数 = 0

    while True:
        try:
            # 获取玩家的猜测
            玩家猜测 = int(input("请输入你的猜测："))
            猜测次数 += 1

            # 检查玩家的猜测
            if 玩家猜测 < 正确数字:
                print("太小了，再试一次！")
            elif 玩家猜测 > 正确数字:
                print("太大了，再试一次！")
            else:
                print(f"恭喜你！你猜对了数字{正确数字}！")
                print(f"你总共猜了{猜测次数}次。")
                break
        except ValueError:
            print("请输入一个有效的数字！")

if __name__ == "__main__":
    数字炸弹游戏()
