
class ParenthesesBal:
    
    def __init__(self, str):
        self.str = str
        self.opencount = self.str.count('(')
        self.closecount = self.str.count(')')
        
    def balance(self):
        if self.opencount < self.closecount:
            self.str = '('* (self.closecount-self.opencount) + self.str
        elif self.opencount > self.closecount:
            self.str += (self.opencount-self.closecount)*')'
        return self.str

in_str = '(а(в)ы(ыв)аф(аы)в()рл()аыв()ыа()о)л'

pb=ParenthesesBal(in_str)
print(pb.balance())
