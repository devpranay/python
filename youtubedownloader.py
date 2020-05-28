from tkinter import *
from tkinter import filedialog
from pytube import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
#total size container
file_size = 0
#=================open file method======================#
def progress(chunk=None, file_handle=None, remaining=None):
    file_download = (file_size - remaining)
    per=(file_download / file_size) * 100
    dtbn.config(text="{:00.0f}% downloaded".format(per))
#=================starting after thread==================#   
def startDownload():
    global file_size
    try:
        url=entry.get()
        dtbn.config(text="Please wait....")
        dtbn.config(state=DISABLED)
        path=askdirectory()
        if path is None:
            return 
        ob=YouTube(url, on_progress_callback=progress)
        stream=ob.streams.first()
        file_size=stream.filesize
        print(file_size)
        stream.download(path)
        print("done")
        dtbn.config(text="Start Download")
        dtbn.config(state=NORMAL)
        showinfo("Downloaded Finished","Downloaded sucessfully ")
        entry.delete(0,END)
        
    except Exception as e:
        showinfo("DATA ERROR","NO LINK IS PASTED")

def startDownloadThread():
    #create thread
    thread=Thread(target=startDownload)
    thread.start()
        

#start gui 
root=Tk()
root.title("Youtube downloader")
#set geometry
root.geometry("600x300")
    
Label(root,text="YOUTUBE DOWNLOADER",font=("verdana",18),fg="red",justify=CENTER).pack(pady=10)
entry=Entry (root,font=("verdana",18),justify=CENTER)
entry.pack(side=TOP,fill=X,padx=10)


#download button
dtbn=Button(root,text="Download",font=("verdana-bold",18),relief='ridge',command=startDownloadThread)
dtbn.pack(side=TOP,pady=10)


root.mainloop()
