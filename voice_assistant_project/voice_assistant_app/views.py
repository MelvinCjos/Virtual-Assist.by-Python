import speech_recognition as sr
import pyttsx3
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def process_voice_command(request):
    if request.method == 'POST':
        # Initialize speech recognizer
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print('Listening...')
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        try:
            # Convert speech to text
            command = recognizer.recognize_google(audio)
            print('Command:', command)

            # Process the command and generate a response
            response = process_command(command)

            # Convert the response to speech
            engine = pyttsx3.init()
            engine.say(response)
            engine.runAndWait()

            return render(request, 'home.html', {'response': response})

        except sr.UnknownValueError:
            print('Unable to recognize speech')
            return render(request, 'home.html', {'response': 'Unable to recognize speech'})

        except sr.RequestError as e:
            print('Error occurred while accessing Google Speech Recognition service:', str(e))
            return render(request, 'home.html', {'response': 'Error occurred while accessing speech recognition service'})

    return render(request, 'home.html')

def process_command(command):
    # Process the command and generate a response
    # You can implement your own logic here based on the recognized command
    # For example, check for keywords and perform specific actions or retrieve data from a database
    response = "You said: " + command
    return response
