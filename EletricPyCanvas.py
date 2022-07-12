import tkinter as tk
class ProjectCanvas:
    def __init__(self,master,user_w,user_h,project_w,project_h):
        canvas_frame = tk.Frame(master=master)
        vscrollbar = tk.Scrollbar(canvas_frame)
        hscrollbar = tk.Scrollbar(canvas_frame,orient='horizontal')


        canvas = tk.Canvas(canvas_frame,yscrollcommand=vscrollbar.set, xscrollcommand= hscrollbar.set,
                    width = user_w ,height = user_h)
        

        vscrollbar.config(command=canvas.yview)
        vscrollbar.pack(side=tk.LEFT,fill=tk.Y) 
        hscrollbar.config(command=canvas.xview)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        project_canvas = tk.Canvas(canvas,width = project_w , height = project_h , bg = 'white') 

        canvas.pack()
        canvas.create_window(0,0,window = project_canvas, anchor='nw')


        master.update()
        canvas_frame.pack(expand=True)
        canvas.config(scrollregion=canvas.bbox("all"))

        self.frame = canvas_frame
        self.draw_canvas = project_canvas
        self.insert_ui = None
        self.insert_ui_id = None

        self.bind_all()
        pass
    
    def click_left(self,event):
        element = self.draw_canvas.gettags("current")
        if self.insert_ui:
            self.draw_canvas.coords(self.insert_ui_id,-100,0)
            self.insert_ui.delete()
            self.insert_ui = None
        pass
    
    def bind_all(self):
        self.draw_canvas.bind("<Button-1>",self.click_left)
        pass
    
    def pack(self):
        self.frame.pack()
