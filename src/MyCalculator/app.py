"""
my first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial


class Calculator(toga.App):

    def startup(self):
        #here i will add 6 box
        #box1=inputtext
        #box2=button 7 8 9 +
        #box3=button 4 5 6 -
        #box4= button 1 2 3 *
        #box5=. 0 C /
        #box= calculate button
        
        box1=toga.Box()
        box2=toga.Box()
        box3=toga.Box()
        box4=toga.Box()
        box5=toga.Box()
        box6=toga.Box()
       
        main_box = toga.Box()
        
        #text input
        self.input_text=toga.TextInput()
        self.input_text.style.width=300
        
        button7=toga.Button('7',on_press=partial(self.enterdata,number='7'))
        button7.style.padding_top=20
        
        button8=toga.Button('8',on_press=partial(self.enterdata,number='8'))
        button8.style.padding_top=20
        
        button9=toga.Button('9',on_press=partial(self.enterdata,number='9'))
        button9.style.padding_top=20
        
        buttonplus=toga.Button('+',on_press=partial(self.enterdata,number='+'))
        buttonplus.style.padding_top=20
        
        #button 4 5 6 -
        
        button4=toga.Button('4',on_press=partial(self.enterdata,number='4'))
        
        button5=toga.Button('5',on_press=partial(self.enterdata,number='5'))
        
        button6=toga.Button('6',on_press=partial(self.enterdata,number='6'))
        
        buttonminus=toga.Button('-',on_press=partial(self.enterdata,number='-'))
        
        #button 1 2 3 *
        
        button1=toga.Button('1',on_press=partial(self.enterdata,number='1'))
        
        button2=toga.Button('2',on_press=partial(self.enterdata,number='2'))
        
        button3=toga.Button('3',on_press=partial(self.enterdata,number='3'))
        
        buttonmultiply=toga.Button('*',on_press=partial(self.enterdata,number='*'))
        
        #dot 0 c /
        
        buttondot=toga.Button('.',on_press=partial(self.enterdata,number='.'))
        
        button0=toga.Button('0',on_press=partial(self.enterdata,number='0'))
        
        buttonclear=toga.Button('C',on_press=partial(self.enterdata,number='C'))
        
        buttondivide=toga.Button('/',on_press=partial(self.enterdata,number='/'))
        
        #calculate button
        
        calculate=toga.Button('Calculate',on_press=self.calculate)
        calculate.style.width=300
        calculate.style.padding_top=30
        
        #adding buttons to boxes
        
        box1.add(self.input_text)
        
        box2.add(button7)
        box2.add(button8)
        box2.add(button9)
        box2.add(buttonplus)
        
        box3.add(button4)
        box3.add(button5)
        box3.add(button6)
        box3.add(buttonminus)
        
        box4.add(button1)
        box4.add(button2)
        box4.add(button3)
        box4.add(buttonmultiply)
        
        box5.add(buttondot)
        box5.add(button0)
        box5.add(buttonclear)
        box5.add(buttondivide)
        
        box6.add(calculate)
        
        #adding box1 to 6in main window
        
        main_box.add(box1)
        main_box.add(box2)
        main_box.add(box3)
        main_box.add(box4)
        main_box.add(box5)
        main_box.add(box6)
        
        main_box.style.update(direction=COLUMN)
        
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
    def enterdata(self,widget,number):
        if(number=="C"):
            self.input_text.value=""
        else:
            self.input_text.value=self.input_text.value+number
            
    def calculate(self,widget):
        output=eval(self.input_text.value)
        self.main_window.info_dialog('Result',str(output))
        #dialog box


def main():
    return Calculator()
