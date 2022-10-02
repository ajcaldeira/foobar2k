import pyfoobar2k
import time
import os
import random
## Available commands
# print(remote.cmd('Browse',pathToAd))
# print(remote.cmd('QueueItems',))
# print(remote.cmd('play'))
# print(remote.cmd('Start'))
# print(remote.cmd('Del',idOfAd))
class AdTimer:

    def __init__(self, counterForAd, pathToMusic, pathToAd):
        self.foobarRemote = self.DefineRemote()
        self.path_to_music = pathToMusic
        self.path_to_ad = pathToAd
        self.musicList, self.musicDict = self.MusicFilepathToList()
        self.counterToPlayAd = counterForAd

    def CreateDictFromList(self, musicLst):
        valueLst = list(range(0, len(musicLst)))
        d = dict(zip(musicLst, valueLst))
        return d

    ## Define the remote
    def DefineRemote(self):
        FoobarRemote = pyfoobar2k.FoobarRemote(host='127.0.0.1', port=6565)
        # idOfAd = 1 ## always make this 0
        return FoobarRemote

    def MusicFilepathToList(self):
        ## add filepath of each song into a list
        # path_to_music, path_to_ad = self.ConfigPaths()
        musicList = []
        for index,file in enumerate(os.listdir(self.path_to_music)):
            filename = os.fsdecode(file)
            filePath = os.path.join(str(self.path_to_music),str(filename))
            musicList.append(filePath)
        ## Shuffle Dict
        random.shuffle(musicList)   
        musicDict = self.CreateDictFromList(musicList)
        return musicList,musicDict

    ## Add songs to foobar in the random order
    def AddSongsToFoobar(self):
        print("You are adding",  len(self.musicDict), "songs to FooBar!")
        print("Every",  self.counterToPlayAd, "songs the add will play.")
        #songCounter to ad add
        songCounter = 0
        for key in self.musicDict:
            if songCounter == self.counterToPlayAd:
                self.AdAdd()
                self.foobarRemote.cmd('Browse',os.path.abspath(key))
                songCounter = 1
            else:
                self.foobarRemote.cmd('Browse',os.path.abspath(key))
                songCounter = songCounter+1
            time.sleep(0.2) ## Need this to make it slower so it doesnt skip songs
        
    ## Play Music List from FooBar
    def PlayMusic(self):
        print(self.foobarRemote.cmd('Start'))
        print('Playing')

    ## Remove song once its playing
    ## Handle The Ad Every x seconds
    def AdAdd(self):
        self.foobarRemote.cmd('Browse',os.path.abspath(self.path_to_ad)) ## add the ad into the mix at the end
        time.sleep(0.2)
        

    def QueueAd(self,index=0):
        # remote.cmd('QueueItems',len(musicList))  ## Queue it as the next song (id is the last one)
        self.foobarRemote.cmd('QueueItems',0)  ## Queue it as the next song (id is the last one)
        print('Ad added successfully!! ')
        time.sleep(5)
        self.foobarRemote.cmd('Del', len(self.musicList)) ## Delete it
        self.foobarRemote.cmd('Del', 0) ## Delete it
        print('ad deleted')

    # def RemoveSongPlaying(musicDic):
    #     try:
    #         ## Easy way to do it:
    #         remote.cmd('Del', len(musicList))
    #         print(f'Removing: {musicList[0]}')
    #         musicList.pop(0)
    #     except Exception as e:
    #         print(e)
    #         print('No song is playing! Trying again in 5 seconds...')
    #         time.sleep(5)
    #         RemoveSongPlaying(musicDic)
        
    # Declaring variables
    

    #print(musicList)

    # AddSongsToFoobar(FoobarRemote, musicDict)
    # PlayMusic()


    ## only run this if no song is playing
    # RemoveSongPlaying(musicDict) ## Should only run when a new song plays