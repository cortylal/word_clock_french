#word_clock_french
#created december 20, 2015
#inspired from https://github.com/mattohagan/word-clock
from datetime import datetime
from Tkinter import *

s1 = 'IL EST DEUX'
s2 = 'QUATRETROIS'
s3 = 'NEUFUNESEPT'
s4 = 'HUITSIXCINQ'
s5 = 'MIDIXMINUIT'
s6 = 'ONZE HEURES'
s7 = 'MOINS LEDIX'
s8 = 'ET QUART   '
s9 = 'VINGT-CINQ '
s10 = 'ET DEMIE   '

words = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
# print (str(hour) + ':' + str(minute))

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
        #self.timer()
        #self.root.mainloop()

    def initUI(self):

        self.parent.title("Horloge de mots")
        self.pack(fill=BOTH, expand=1)

        defualt_fill='#393939'
        defualt_font='Courier 70 bold'
        height=75
        width=47

        #height = 100
        #width = (height*47)/75
        
        self.canvas = Canvas(self, cursor='', bg='#292929')
        #first row
        self.il_est = self.canvas.create_text(width, height, anchor=W, font=defualt_font,
                           text=words[0][:6], fill=defualt_fill)
        self.deux = self.canvas.create_text(width*9.4, height, anchor=W, font=defualt_font,
                           text=words[0][7:], fill=defualt_fill)
        #second row
        self.quatre = self.canvas.create_text(width, height*2, anchor=W, font=defualt_font,
                           text=words[1][:6], fill=defualt_fill)
        self.trois = self.canvas.create_text(width*8.2, height*2, anchor=W, font=defualt_font,
                           text=words[1][6:], fill=defualt_fill)
        #third row
        self.neuf = self.canvas.create_text(width, height*3, anchor=W, font=defualt_font,
                           text=words[2][:4], fill=defualt_fill)
        self.une = self.canvas.create_text(width*5.8, height*3, anchor=W, font=defualt_font,
                           text=words[2][4:7], fill=defualt_fill)
        self.sept = self.canvas.create_text(width*9.4, height*3, anchor=W, font=defualt_font,
                           text=words[2][7:], fill=defualt_fill)
        #fourth row
        self.huit = self.canvas.create_text(width, height*4, anchor=W, font=defualt_font,
                           text=words[3][:4], fill=defualt_fill)
        self.six = self.canvas.create_text(width*5.79, height*4, anchor=W, font=defualt_font,
                           text=words[3][4:7], fill=defualt_fill)
        self.cinq1 = self.canvas.create_text(width*9.4, height*4, anchor=W, font=defualt_font,
                           text=words[3][7:], fill=defualt_fill)
        #fifth row
        self.mi = self.canvas.create_text(width, height*5, anchor=W, font=defualt_font,
                           text=words[4][:2], fill=defualt_fill)
        self.di = self.canvas.create_text(width*3.4, height*5, anchor=W, font=defualt_font,
                           text=words[4][2:4], fill=defualt_fill)
        self.x = self.canvas.create_text(width*5.79, height*5, anchor=W, font=defualt_font,
                            text=words[4][4:5], fill=defualt_fill)
        self.minuit = self.canvas.create_text(width*7, height*5, anchor=W, font=defualt_font,
                           text=words[4][5:], fill=defualt_fill)
        #sixth row
        self.onze = self.canvas.create_text(width, height*6, anchor=W, font=defualt_font,
                           text=words[5][:4], fill=defualt_fill)
        self.heure = self.canvas.create_text(width*7, height*6, anchor=W, font=defualt_font,
                           text=words[5][5:10], fill=defualt_fill)
        self.s = self.canvas.create_text(width*13, height*6, anchor=W, font=defualt_font,
                           text=words[5][10:], fill=defualt_fill)
        #seventh row
        self.moins = self.canvas.create_text(width, height*7, anchor=W, font=defualt_font,
                           text=words[6][:5], fill=defualt_fill)
        self.le = self.canvas.create_text(width*8.2, height*7, anchor=W, font=defualt_font,
                           text=words[6][6:8], fill=defualt_fill)
        self.dix2 = self.canvas.create_text(width*10.6, height*7, anchor=W, font=defualt_font,
                           text=words[6][8:], fill=defualt_fill)
        #eigth row
        self.et1 = self.canvas.create_text(width, height*8, anchor=W, font=defualt_font,
                           text=words[7][:2], fill=defualt_fill)
        self.quart = self.canvas.create_text(width*4.6, height*8, anchor=W, font=defualt_font,
                           text=words[7][3:8],fill=defualt_fill)
        #ninth row
        self.vingt = self.canvas.create_text(width, height*9, anchor=W, font=defualt_font,
                           text=words[8][:5], fill=defualt_fill)
        self.cinq2 = self.canvas.create_text(width*8.2, height*9, anchor=W, font=defualt_font,
                           text=words[8][6:10], fill=defualt_fill)
        self.tiret = self.canvas.create_text(width*7, height*9, anchor=W, font=defualt_font,
                           text=words[8][5:6], fill=defualt_fill)
        #tenth row
        self.et2 = self.canvas.create_text(width, height*10, anchor=W, font=defualt_font,
                           text=words[9][:2], fill=defualt_fill)
        self.demie = self.canvas.create_text(width*4.6, height*10, anchor=W, font=defualt_font,
                           text=words[9][3:8], fill=defualt_fill)

        #extra letters
        self.canvas.create_text(width*3.3, height, anchor=W, font=defualt_font,
                           text='V   X', fill=defualt_fill)
        self.canvas.create_text(width*5.7, height*6, anchor=W, font=defualt_font,
                           text='R', fill=defualt_fill)
        self.canvas.create_text(width*7, height*7, anchor=W, font=defualt_font,
                           text='Z', fill=defualt_fill)
        self.canvas.create_text(width*3.4, height*8, anchor=W, font=defualt_font,
                           text='R     PMS', fill=defualt_fill)
        self.canvas.create_text(width*13, height*9, anchor=W, font=defualt_font,
                           text='U', fill=defualt_fill)
        self.canvas.create_text(width*3.35, height*10, anchor=W, font=defualt_font,
                           text='S     PAM', fill=defualt_fill)
        
        
        self.canvas.pack(fill=BOTH, expand=1)
        

def timer(ex):
    clear_all(ex)
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    
    default_fill='#EAEAEA'
    ex.canvas.itemconfigure(ex.il_est, fill=default_fill)
    

    #minutes
    if minute >= 55:
        changeColor(ex, ex.moins)
        changeColor(ex, ex.cinq2)
        hour += 1
    elif minute >= 50:
        changeColor(ex, ex.moins)
        changeColor(ex, ex.di)
        changeColor(ex, ex.x)
        hour += 1
    elif minute >= 45:
        changeColor(ex, ex.moins)
        changeColor(ex, ex.le)
        changeColor(ex, ex.quart)
        hour += 1
    elif minute >= 40:
        changeColor(ex, ex.moins)
        changeColor(ex, ex.vingt)
        hour += 1
    elif minute >=35:
        changeColor(ex, ex.moins)
        changeColor(ex, ex.vingt)
        changeColor(ex, ex.tiret)
        changeColor(ex, ex.cinq2)
        hour += 1
    elif minute >= 30:
        changeColor(ex, ex.et2)
        changeColor(ex, ex.demie)
    elif minute >= 25:
        changeColor(ex, ex.vingt)
        changeColor(ex, ex.tiret)
        changeColor(ex, ex.cinq2)
    elif minute >= 20:
        changeColor(ex, ex.vingt)
    elif minute >= 15:
        changeColor(ex, ex.et1)
        changeColor(ex, ex.quart)
    elif minute >= 10:
        changeColor(ex, ex.di)
        changeColor(ex, ex.x)
    elif minute >= 5:
        changeColor(ex, ex.cinq2)

    
    #hours
    if hour == 1 or hour == 13:
        ex.canvas.itemconfigure(ex.une, fill=default_fill)
    elif hour == 2 or hour == 14:
        ex.canvas.itemconfigure(ex.deux, fill=default_fill)
    elif hour == 3 or hour == 15:
        ex.canvas.itemconfigure(ex.trois, fill=default_fill)
    elif hour == 4 or hour == 16:
        ex.canvas.itemconfigure(ex.quatre, fill=default_fill)
    elif hour == 5 or hour == 17:
        ex.canvas.itemconfigure(ex.cinq1, fill=default_fill)
    elif hour == 6 or hour == 18:
        ex.canvas.itemconfigure(ex.six, fill=default_fill)
    elif hour == 7 or hour == 19:
        ex.canvas.itemconfigure(ex.sept, fill=default_fill)
    elif hour == 8 or hour == 20:
        ex.canvas.itemconfigure(ex.huit, fill=default_fill)
    elif hour == 9 or hour == 21:
        ex.canvas.itemconfigure(ex.neuf, fill=default_fill)
    elif hour == 10 or hour == 22:
        ex.canvas.itemconfigure(ex.dix1, fill=default_fill)
    elif hour == 11 or hour == 23:
        ex.canvas.itemconfigure(ex.onze, fill=default_fill)
    elif hour == 12 :
        ex.canvas.itemconfigure(ex.mi, fill=default_fill)
        ex.canvas.itemconfigure(ex.di, fill=default_fill)
    elif hour == 24 or hour == 0:
        ex.canvas.itemconfigure(ex.minuit, fill=default_fill)

    #am/pm/oclock
    if hour != 1 and hour != 13 and hour != 12 and hour != 24 and hour != 0:
        ex.canvas.itemconfigure(ex.heure, fill=default_fill)
        ex.canvas.itemconfigure(ex.s, fill=default_fill)
    elif hour == 1 or hour == 13:
        ex.canvas.itemconfigure(ex.heure, fill=default_fill)
        
    ex.canvas.after(10000,timer, ex)

    

def clear_all(ex):
    defualt_fill='#393939'
    ex.canvas.itemconfigure(ex.il_est, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.et1, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.dix2, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.et2, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.demie, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.quart, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.vingt, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.cinq1, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.tiret, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.moins, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.le, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.une, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.deux, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.trois, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.quatre, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.cinq2, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.six, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.sept, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.huit, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.neuf, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.di, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.x, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.onze, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.mi, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.minuit, fill=defualt_fill)

def changeColor(ex, itemID):
    default_fill='#EAEAEA'
    ex.canvas.itemconfigure(itemID, fill=default_fill)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("720x820+300+300")
    root.after(1000,timer, ex)
    root.mainloop()

    
    


if __name__ == '__main__':
    main()
    