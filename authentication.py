import tkinter as tk
from tkinter import ttk 
import datetime

HEIGHT = 1500   
WIDTH = 1500

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH )
canvas.pack()


#label for the app heading
labelfont=('times' ,45, 'bold')
frame_label = tk.Label(root ,text="REGISTER YOUR PALM PRINT",font=labelfont,bg='#ffffff')
frame_label.place( rely=0.02 ,relwidth=1, relheight=0.05  )

frame_label2 = tk.Label(root ,text="Made by NAME",font=labelfont,bg='#ffffff')
frame_label2.place( rely=0.92 ,relwidth=1, relheight=0.09  )

# frame for information
frame= tk.Frame(root , bg='#ffffff', borderwidth=2 , relief="groove")
frame.place(relx=0.05,rely= 0.09,relwidth=0.39,relheight=0.82)

app_font = ('times', 20 , 'bold')
label = tk.Label(frame,text="Name of the Person",font=app_font ,bg='#d4fcdf')
label.place( rely=0.02 ,relwidth=1, relheight=0.05  )

name_entry_var = tk.StringVar()
name_entry = tk.Entry(frame,text=name_entry_var, textvariable= name_entry_var, justify = 'center')
name_entry.place(rely=0.075, relwidth=1 , relheight=0.05 , )
name_entry.focus()

mobile_label = tk.Label(frame,text="Enter Mobile no (Optional)",font=app_font ,bg='#d4fcdf')
mobile_label.place( rely=0.180    ,relwidth=1, relheight=0.05  )

mobile_var = tk.StringVar()
place_combobox = ttk.Entry(frame,text=mobile_var,textvariable=mobile_var,justify='center')
place_combobox.place(rely=0.235, relwidth= 1 , relheight=0.04)


side_label = tk.Label(frame,text="Which PALM ?",font=app_font ,bg='#d4fcdf')
side_label.place( rely=0.340 ,relwidth=1, relheight=0.05  )

palm_type_var = tk.StringVar()
palm_type = ttk.Radiobutton(frame, text='RIGHT PALM', value= 'Right Palm', variable=palm_type_var)
palm_type.place(relx=0,rely=0.40, relwidth= 0.49, relheight=0.05)

palm_type2 = ttk.Radiobutton(frame, text='LEFT PALM', value= 'Left palm', variable=palm_type_var)
palm_type2.place(relx=0.51,rely=0.40, relwidth= 0.49, relheight=0.05)


check_var = tk.IntVar()
state_check = ttk.Checkbutton(frame , text= "I agree to Provide My palm Details.", variable=check_var)
state_check.place(rely= 0.6, relwidth= 1, relheight= 0.05 )


dnt_label = tk.Label(frame,text="DATE AND TIME ",font=50 ,bg='#d4fcdf')
dnt_label.place( rely=0.7 ,relwidth=1, relheight=0.05  )

dnt_var= tk.StringVar()
now = datetime.datetime.now()
dnt_msg = tk.Entry(frame,text=dnt_var,justify='center', state= 'readonly' )
dnt_var.set(now.strftime("%A-%d-%B-%Y %X"))
dnt_msg.place(rely= 0.76,relwidth= 1,relheight= 0.1)

submit_button = tk.Button(frame, text='SUBMIT')
submit_button.place(relx= 0.2, rely= 0.9,relheight=0.05 , relwidth=0.2 )

snap = tk.Button(frame,text='CAMERA' )
snap.place(relx= 0.6, rely= 0.9,relheight=0.05 , relwidth=0.2 )

#frame for camera captured image 
frame2= tk.Frame(root , bg='#000000', borderwidth=2 , relief="groove")
frame2.place(relx=0.50,rely=0.09,relwidth=0.39,relheight=0.39)
#canvas for image
cam_canvas= tk.Label(frame2 ,width=50,height=50, borderwidth=5 , relief="groove")
cam_canvas.place(relx=0, rely=0.070, relwidth=1,relheight=0.81)

#LABEL for the camera
auto_take = tk.Label(frame2,text='AI CAMERA ')
auto_take.place(relx=0 ,rely= 0.015, relwidth= 1, relheight=0.05)

#button for TASKS frame2
image_show = tk.Button(frame2,text='SHOW THE PALM IMAGE' )
image_show.place(relx= 0.3, rely= 0.9,relheight=0.08 , relwidth=0.4 )

#frame for Processed image
frame3= tk.Frame(root , bg='#000000', borderwidth=2 , relief="groove")
frame3.place(relx=0.50,rely=0.50,relwidth=0.39,relheight=0.39)

#canvas for image
cur_canvas= tk.Label(frame3 ,width=50,height=50 ,borderwidth=5 , relief="groove")
cur_canvas.place(relx=0, rely=0.070, relwidth=1,relheight=0.81)

#button for image SHOW
cur_thres_button = tk.Button(frame3,text='PROCESS THIS IMAGE' )
cur_thres_button.place(relx= 0.55, rely= 0.9,relheight=0.08 , relwidth=0.4 )

image_show = tk.Button(frame3,text='Load the data ')
image_show.place(relx= 0.2, rely= 0.9,relheight=0.08 , relwidth=0.2 )

#label for the processed image 
cur_auto_take = tk.Label(frame3,text='VEHICLE IMAGE DATA')
cur_auto_take.place(relx=0 ,rely= 0.015, relwidth= 1, relheight=0.05)


root.mainloop()