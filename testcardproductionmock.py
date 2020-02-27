class TestCardProduction(object):
    def __init__(self, nCardsToProduce, testCardSettings):
        self.nCardsToProduce = nCardsToProduce
        self.testCardSettings = testCardSettings
        

    def preview(self):
        print('* test')
        self.testCardSettings.print()


    def run(self):
        for i in range(self.nCardsToProduce):
            print('%d' % (i + 1))
