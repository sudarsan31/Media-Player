import vlc,easygui
media="video1.mp4"
player=vlc.MediaPlayer(media)
picture="pic.gif"
i=0
List=["video1.mp4","Song1.mp3","video2.wmv","Song2.mp3"]
#List=["alagar.mp3","karupanaswami.mp3","18ampadi karuppa.mp3"]
while True:
    choice=easygui.buttonbox(title="Media player",msg="Welcome to Media Player press play to start",image=picture,choices=["<<Prev","Play","Pause","Next>>","Fullscreen","New","Quit"])     
    print(choice)
    if(choice=="Play"):
        player.play()
    elif(choice=="Pause"):
        player.pause()
        choice=easygui.buttonbox(title="Media player",msg=" press Resume to Start ",image=picture,choices=["Resume","Quit"])
        if(choice=="Resume"):
            player.play() 
        else:
            player.stop()
            easygui.msgbox("Thank you!")
            break 
    elif(choice=="Fullscreen"):
        player.set_fullscreen(True)
    elif(choice=="Next>>"):
        player.stop()
        if(i==3):
            i=-1
        i+=1
        player=vlc.MediaPlayer(List[i])
        player.play()
    elif(choice=="<<Prev"):
        player.stop()
        i=i-1
        if(i==-1):
            i=0 
        player=vlc.MediaPlayer(List[i])
        player.play()	
    elif(choice=="New"):
        player.stop()
        media=easygui.fileopenbox(title="choose media to open")
        player=vlc.MediaPlayer(media)
        player.play()
    elif(choice=="Quit"):
        player.stop()
        easygui.msgbox("Thank You!")
        break
    else:
        break 
    
