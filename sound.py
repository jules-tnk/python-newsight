from playsound import playsound
from gtts import gTTS  # to send text to google and retrieve the corresponding audio
# from googletrans import Translator
from translate import Translator

audio_count = 1  # handle the name of the output audio file


def say(text, lang):
    global audio_count
    if text == "" or text == " ":
        print('Pas de texte')
        say("Pas de texte", 'fr')
        return
    # correct the format
    text = text.replace('_', ' ')

    # translate the text
    translator = Translator(to_lang=lang)
    text = translator.translate(text)
    print(text)
    # send the request and retrieve the reponse
    request = gTTS(text=text, lang=lang, slow=False)
    file = f"audio_output/{audio_count}.mp3"
    request.save(file)
    playsound(file)
    audio_count += 1  # change the name of the output_file
    print("Sortie audio terminée...")


if __name__ == '__main__':
    say("Hello how are you", 'fr')
