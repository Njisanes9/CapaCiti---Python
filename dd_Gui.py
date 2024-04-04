import tkinter as tk
from tkinter import ttk
from time import time



class DailyDigestGui(tk.Tk):


    def __init__(self):
        
        super().__init__()
        
        


    def _build__gui_recipient(self, master, add_recipient_var, recipient_list_var):

        pass

    def _build_gui_schedule(self,master,hour_var,minute_var):
        pass

    def _build_giu_contents(self,master,quote_var,weather_var, twitter_var,wikipedia_var):
       self.master = master
       self.master = tk.Tk()
       self.master.title('Daily Digest')
       self.Heading = tk.Label(self, text="Your daily digest")
                 

    def _build_gui_sender(self,master,sender_email_var,sender_password_var):
       self.master = master

       self.master = tk.Tk()
       self.master.geometry("800x800")

       self.lblhead = tk.Label(self, text='Daily Digest', font=("Comic Sans MS", 20, "bold"))
       self.lblhead.pack()
                 

    def _build_gui_controls(self,master):
        pass

    def add_recipient(self):
        pass

    def _remove_selected_recipients(self,selection):
        pass

    def _update_settingS(self):
        pass



if __name__ == '__main__':

    
    getGui = DailyDigestGui()
    
    master = None
    hrVar = None
    minute = None
    tweet = None
    wiki = None
    getGui._build_gui_sender(master,hrVar,minute)
    getGui.mainloop()