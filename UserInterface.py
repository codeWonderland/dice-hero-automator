import tkinter as Tkinter


class DragDropListbox(Tkinter.Listbox):
    """ A Tkinter listbox with drag'n'drop reordering of entries. """
    def __init__(self, master, **kw):
        kw['selectmode'] = Tkinter.SINGLE
        Tkinter.Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None

    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)

    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
        elif i > self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i

    
if __name__ == '__main__':     
    tk = Tkinter.Tk()     
    length = 10     
    dd = DragDropListbox(tk, height=length)     
    dd.pack( )     
    
    for i in range(length):         
        dd.insert(Tkinter.END, str(i))     
        
    def show(*args):         
        ''' show the current ordering every 2 seconds '''         
        for x in dd.get(0, Tkinter.END):             
            print(x)   

        tk.destroy()           
            
    tk.protocol("WM_DELETE_WINDOW", show)   
    tk.bind("<Escape>", show)  
    tk.mainloop( )