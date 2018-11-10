from flask import Flask, request
from  twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)   #работа с вебом

@app.route('/outbound1', methods=['GET', 'POST'])   #работа с вебом
def outbound1():
    strr = request.form.get('SpeechResult')   #работа с вебом
    print(strr)
    twiml_response = VoiceResponse()                                            #twiML элемент response с него всегда нужно начинать twiML
    twiml_response.say('hi silly boy')                                          #twiML текст2спич
    twiml_response.play('http://k003.kiwi6.com/hotlink/9njt732wby/lol.mp3')     #twiML проигрование mp3
    twiml_xml = twiml_response.to_xml()                                         #twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)   #twiML в конце перевожу в строку, потому что так было в примерчике


if __name__=='__main__':
    app.run()       #работа с вебом