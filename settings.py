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
        self.ship_limit = 3
        
        # 子弹的属性
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullters_allowed = 5

        # 外星人的属性
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1



