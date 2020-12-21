import tkinter as tk 
import os 

HEIGHT = 750 
WIDTH = 750 

root = tk.Tk()
canvas = tk.Canvas(root, height= HEIGHT , width= WIDTH )
canvas.pack()

def register():
    os.system("python register.py")  

def authentication():
    os.system("python authentication.py")

#label for the app heading
labelfont=('times' ,39, 'bold')
frame_label = tk.Label(root ,text="PALM PRINT AUTHENTICATION APP",font=labelfont,bg='#ffffff')
frame_label.place( rely=0.05 ,relwidth=1, relheight=0.15  )


frame_label2 = tk.Label(root ,text="Made by NAME",font=labelfont,bg='#ffffff')
frame_label2.place( rely=0.92 ,relwidth=1, relheight=0.09  )

Button_font = ('times' ,25, 'bold')
#Button for Register Palm print 
Register_button = tk.Button(root,text='REGISTER YOUR PALM PRINT',font=Button_font, command=register )
Register_button.place(relx= 0.15, rely= 0.35,relheight=0.15 , relwidth=0.7 )

#Button for Authentication
Authentication_button = tk.Button(root,text='AUTHENTICATE YOUR PALM PRINT',font=Button_font, command=authentication ) 
Authentication_button.place(relx= 0.15, rely= 0.55,relheight=0.15 , relwidth=0.7 )

  

root.mainloop()