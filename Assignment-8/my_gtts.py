import gtts

my_text = "i am rezvane a python programmer"

x = gtts.gTTS(my_text, lang="en", slow = False)

x.save("Assignment-8/voice.mp3")

