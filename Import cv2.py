import cv2
import tkinter as tk
from PIL import Image, ImageTk


VIDEO_SRC = 'assets/TWICE -720.mp4'


INTERVAL = 50

class CvApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pause_flag = False

        self.label = tk.Label(self)
        self.label.pack()

        #控制按鈕
        self.ui_pause=tk.Button(self,text='暫停',command=self.pause)
        self.ui_pause.pack()
        self.ui_rewind=tk.Button(self,text='重播',command=self.rewind)
        self.ui_rewind.pack()


        self.cap = cv2.VideoCapture(VIDEO_SRC)

        self.update_frame()
        

    def pause(self):
        if self.pause_flag:

            self.pause_flag = False
        else:
            self.pause_flag = True
        print ('暫停被按下')

    def rewind(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        print ('重播被按下')   
    

    def update_frame(self):
        ret,frame = self.cap.read()
        print(ret)
        if self.pause_flag == False:
        
            if ret :
                frame_id= self.cap.get(cv2.CAP_PROP_POS_FRAMES)
                print(frame_id)
                
                frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                photo = ImageTk.PhotoImage(image=img)

                self.label.config(image=photo)
                self.label.image = photo

        self.after(INTERVAL,self.update_frame)

    def destroy(self):
        self.cap.release()
        super().destroy()

app = CvApp()
app.mainloop()                