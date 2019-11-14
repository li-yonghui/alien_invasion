class Settings():
    ''' 存储工程的所有设置 '''

    def __init__(self):
        ''' 初始化游戏的设置 '''

        # 屏幕的属性
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的属性
        self.ship_speed_factor = 1.5

