import pygame

songs = {
    "happy": "songs/happy.mp3",
    "angry": "songs/angry.mp3",
    "disgust": "songs/disgust.mp3",
    "fear": "songs/fear.mp3",
    "neutral": "songs/neutral.mp3",
    "sad": "songs/sad.mp3",
    "surprise": "songs/surprise.mp3"
}

isSongPlay = False
previosEmotion = None


def pause_audio():
    global isSongPlay
    pygame.mixer.music.pause()
    isSongPlay = False

def play_audio(emotion):
    global isSongPlay, previosEmotion
    
    if previosEmotion == emotion:
        return
    

    if isSongPlay:
        pause_audio()

    file_path = songs[emotion]
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    isSongPlay = True
    previosEmotion = emotion

