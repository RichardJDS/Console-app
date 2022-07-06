from water.menu import Menu
class WaterMain:
    def __init__(self):
        pass
    def run(self):
        menu = Menu()
        should_exit = False
        while(not should_exit):
            should_exit = menu.process_run()
