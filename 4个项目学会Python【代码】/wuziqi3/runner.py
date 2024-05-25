from gamelogic.gamelogic import GameLogic

game = GameLogic()
while True:
    game.showBoard()
    game.playerRound()  #玩家的回合 下黑子
    if game.isPlayerWin():
        print('恭喜！你赢了！')
        break
    game.cpuRound()  #电脑的回合 下白子
    if game.isCPUWin():
        print('哎！你输了！')
        break