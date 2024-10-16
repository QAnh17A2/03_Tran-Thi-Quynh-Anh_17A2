class PS:
    def __init__(self, tu = 0, mau = 0):
        self.tu = tu
        self.mau = mau
        
    
    def creat(self):
        self.tu = int(input('nhập tử số:'))
        self.mau = int(input('nhập mẩu số:'))
   
    def check(self):
        if self.mau == 0:
            print('phân số không hợp lệ!!!')
        else:
            print('phân số hợp lệ!!!')
    
    def print(self):
        if self.mau != 0:
            print(f'{self.tu}/{self.mau}')     
        else:
            print('phân số không hợp lệ')

ps1 = PS()
ps1.creat()
ps1.check()
ps1.print()
