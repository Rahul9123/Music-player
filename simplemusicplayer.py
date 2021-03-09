def unmutemusic():
    globals = currentvol
    root.UnmuteButton.grid_remove()
    root.MuteButton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    globals = currentvol
    root.MuteButton.grid_remove()
    root.UnmuteButton.grid()
    curentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def resusememusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabels.configure(text='playing.......')

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol + 0.05)
    ProgressbarVolumeLabel.configure(text = '{}%'.format(int(mixer.music.get_volume() * 100 )))
    ProgressbarVolume['value'] = mixer.music.get_volume() * 100

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.05)
    ProgressbarVolumeLabel.configure(text = '{}%'.format(int(mixer.music.get_volume() * 100)))
    ProgressbarVolume['value'] = mixer.music.get_volume() * 100

def stopmusic():
    mixer.music.stop()
    AudioStatusLabels.configure(text='stoped.......')

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabels.configure(text = 'paused.......')

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    ProgressbarLabel.grid()
    ProgressbarMusicLabel.grid()
    root.MuteButton.grid()
    mixer.music.set_volume( 0.4 )
    ProgressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    AudioStatusLabels.configure(text='playing.......')

    Song=MP3(ad)
    totalsonglength = int(Song.info.length)
    ProgressbarMusic['maximum'] = totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text = '{}'.format(str(datetime.timedelta(seconds = totalsonglength))))

    def progressbarmusictick():
        Currentsonglength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = Currentsonglength
        ProgressbarMusicStartTimeLabel.configure(text = '{}'.format(str(datetime.timedelta(seconds = Currentsonglength))))
        ProgressbarMusic.after(2,progressbarmusictick)

    progressbarmusictick()

def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir = 'D:/My Music',
                                        title = 'SelectAudio File',
                                        filetype = (('MP3', '*.mp3'),('WAV', '*.wav')))
    except:
        dd = filedialog.askopenfilename(title = 'SelectAudio File',
                                        filetype = (('MP3', '*.mp3'), ('WAV', '*.wav')))
    audiotrack.set(dd)

def createwidthes():
    global implay,impause,imbrowse,imvolumeup,imvolumedown,imstop,imresume,immute,imunmute
    global AudioStatusLabels,ProgressbarVolume,ProgressbarLabel,ProgressbarVolumeLabel,ProgressbarMusicLabel,\
           ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusicStartTimeLabel
    ########################## Images Register ######################################
    implay = PhotoImage(file = 'play.png')
    impause = PhotoImage(file = 'pause.png')
    imbrowse = PhotoImage(file = 'browsing.png')
    imvolumeup= PhotoImage(file = 'volume-up.png')
    imvolumedown = PhotoImage(file = 'volume-down.png')
    imstop = PhotoImage(file = 'stop.png')
    imresume = PhotoImage(file = 'resume.png')
    immute = PhotoImage(file = 'mute.png')
    imunmute = PhotoImage(file = 'unmute.png')

    ######################### change size of images ####################################

    implay = implay.subsample(19,19)
    impause = impause.subsample(19,19)
    imbrowse = imbrowse.subsample(19,19)
    imvolumeup = imvolumeup.subsample(19,19)
    imvolumedown= imvolumedown.subsample(19,19)
    imstop=imstop.subsample(19,19)
    imresume = imresume.subsample(19,19)
    immute = immute.subsample(19,19)
    imunmute = imunmute.subsample(19,19)

    ########################## Labels ####################################################

    TrackLabel = Label(root,text="Select Audio Track :",bg = 'lightskyblue',font = ('arial',15,'italic bold'))
    TrackLabel.grid(row = 0,column = 0,padx = 20,pady = 20)

    AudioStatusLabels = Label(text='',bg = 'lightskyblue',font = ('arial',15,'italic bold'),width=20)
    AudioStatusLabels.grid(row = 2,column = 1)
    ###############################  Entry Box ##############################################

    TrackLabelEntry = Entry(root,font=('arial',15,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=25,pady=25)
    ########################## Button ########################################################

    BrowseButton = Button(root,text='search',bg='deeppink',font=('arial',13,'italic bold'),width=200,bd=5,
                          activebackground='purple4',image=imbrowse,compound=RIGHT,command= musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root, text='Play', bg='green2', font=('arial', 13, 'italic bold'), width=200, bd=5,
                        activebackground='purple4',image=implay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)

    root.PauseButton = Button(root, text='Pause', bg='yellow', font=('arial', 13, 'italic bold'), width=200, bd=5,
                         activebackground='purple4',image=impause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1, column=1, padx=20, pady=20)

    root.ResumeButton = Button(root, text='Resume', bg='yellow', font=('arial', 13, 'italic bold'), width=200, bd=5,
                          activebackground='purple4', image=imresume, compound=RIGHT, command=resusememusic)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()

    VolumeupButton = Button(root, text='VolumeUp', bg='blue', font=('arial', 13, 'italic bold'), width=200, bd=5,
                            activebackground='purple4',image=imvolumeup,compound=RIGHT,command=volumeup)
    VolumeupButton.grid(row=1, column=2, padx=20, pady=20)

    StopButton = Button(root, text='Stop', bg='red', font=('arial', 13, 'italic bold'), width=200, bd=5,
                        activebackground='purple4',image=imstop,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    VolumedownButton = Button(root, text='VolumeDown', bg='blue', font=('arial', 13, 'italic bold'), width=200, bd=5,
                              activebackground='purple4',image=imvolumedown,compound=RIGHT,command=volumedown)
    VolumedownButton.grid(row=2, column=2, padx=20, pady=20)

    root.MuteButton = Button(root, text='Mute', bg='yellow', activebackground='purple4', width=100, bd=5,
                             image=immute, compound=RIGHT, command=mutemusic)
    root.MuteButton.grid(row=3, column=3)
    root.MuteButton.grid_remove()

    root.UnmuteButton = Button(root, text='Unmute', bg='yellow', activebackground='purple4', width=100, bd=5,
                             image=imunmute, compound=RIGHT,command=unmutemusic)
    root.UnmuteButton.grid(row=3, column=3, )
    root.UnmuteButton.grid_remove()

    ############################### Progress Volume ##############################################
    ProgressbarLabel = Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()

    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                                    value=0,length=190)

    ProgressbarVolume.grid(row=0,column=0,ipadx=5)
    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)

    ############################### ProgressBar Music ##############################################
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel, text='0:00:0', bg='red',width=6)
    ProgressbarMusicStartTimeLabel.grid(row=0, column=0)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel, text='0:00:0', bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0, column=2)

######################################################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

root = Tk()
root.geometry('1100x500+200+50')
root.title('Simple Music Player..')
root.iconbitmap('music.ico')
root.resizable(False,False)
root.configure(bg='lightskyblue')

############################## Global Variable ################################################

audiotrack = StringVar()
currentvol = 0
totalsonglength = 0
count = 0
text = ''

################################## Create slide ###############################################

SS='Developed By Rahul Kumar'
SlideLabel = Label(root,text = SS,bg='lightskyblue',font=('arial',20,'italic bold'))
SlideLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)

def IntroLabelTick():
    global count,text
    if(count >= len(SS)):
        count = -1
        text = ''
        SlideLabel.configure(text=text)
    else:
        text = text+SS[count]
        SlideLabel.configure(text=text)
    count += 1
    SlideLabel.after(200,IntroLabelTick)

IntroLabelTick()
mixer.init()
createwidthes()
root.mainloop()