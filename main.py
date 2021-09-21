import pygame
from pygame.locals import *
import sys
def main():
    pygame.init()                                 # Pygameの初期化c
    screen = pygame.display.set_mode((500, 500))  # 800*600の画面
    px=0
    py=500
    yuka=500
    key_in=(1,0)

    maps=[[0 for i in range(50)] for j in range(50)]
    hed=[25,25]

    while True:

        maps[hed[0]][hed[1]]=255
        hed[0]+=key_in[0]
        hed[1]+=key_in[1]
        if(hed[0]>=50):hed[0]=49
        if(hed[1]>=50):hed[1]=49
        if(hed[0]<0):hed[0]=0
        if(hed[1]<0):hed[1]=0
        print(hed)

        screen.fill((50,50,50))                                    # 背景を白
        pygame.draw.line(screen, (0,255,0), (0,550), (700,550), 2)    # 線
        for i,t in enumerate(maps):
            for i2,t2 in enumerate(t):
                pygame.draw.circle(screen,(t2,t2,t2),(5+i*10,5+i2*10),5)              # ●
            
        pygame.draw.rect(screen, (255,255,0), Rect(px,py,50,50), 1)    # syuzinkou
        pygame.display.update()


        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == KEYDOWN:  # キーを押したとき
            # ESCキーならスクリプトを終了
                print(event.key)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == 1073741903:#->
                    key_in=(1,0)
                if event.key == 1073741904:#<-
                    key_in=(-1,0)
                if event.key == 1073741905:#^
                    key_in=(0,1)
                if event.key == 1073741906:#^
                    key_in=(0,-1)
                        
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()                # 終了（ないとエラーで終了することになる）


if __name__ == "__main__":
    main()
