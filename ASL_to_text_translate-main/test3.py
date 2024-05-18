import pyttsx3 
speak_engine = pyttsx3.init()
speak_engine.setProperty('rate',120)
speak_engine.setProperty('volume', 0.9)  # Volume level

speak_engine.say("hi")
speak_engine.runAndWait()