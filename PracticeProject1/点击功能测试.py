import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
demo_image = pygame.image.load("./images/again.png")
demo_image_rect = demo_image.get_rect()
demo_image_rect.x = 150
demo_image_rect.y = 200
screen.blit(demo_image, (demo_image_rect.x, demo_image_rect.y))
# print(demo_image_rect.topright[0])
while True:

    for event in pygame.event.get():

        pygame.click = 60

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        # print(mouse)
        if click[0] == 1:
            print("点击左键")
        if click[1] == 1:
            print("点击中键")
        if click[2] == 1:
            print("点击右键")
        if click[0] == 1 and demo_image_rect.topright[0] > mouse[0] > demo_image_rect.x \
                and demo_image_rect.bottom > mouse[1] > demo_image_rect.y:
            print("重新开始")

        pygame.display.update()

        if event.type == pygame.QUIT:
            print("退出")

            #   quit卸载所以模块
            pygame.quit()

            #   退出系统
            exit()
