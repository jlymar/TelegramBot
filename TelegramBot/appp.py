from flask import Flask, request
from  twilio.twiml.voice_response import VoiceResponse, Gather
import spacy

app = Flask(__name__)   #работа с вебом

@app.route('/outbound1', methods=['GET', 'POST'])   #работа с вебом
def outbound1():
    strr = request.form.get('SpeechResult')   #работа с вебом
    print(strr)
    #doc = nlp(strr)
    #print(doc.ents)
    '''
    
    if 'Color' in doc.ents.keys:
        add to db and form next question
    else:
        form reanswer request
        
    
    
    '''
    twiml_response = VoiceResponse()                                            #twiML элемент response с него всегда нужно начинать twiML
    twiml_response.say('hi silly boy')                                          #twiML текст2спич
    twiml_response.play('http://k003.kiwi6.com/hotlink/9njt732wby/lol.mp3')     #twiML проигрование mp3
    # gather = Gather(action='http://28e81dff.ngrok.io/outbound2', input='speech', speechTimeout='auto')
    # gather.say('what car do you have?')
    # twiml_response.append(gather)
    # twiml_response.say('We didn\'t receive any input. Goodbye!')
    twiml_xml = twiml_response.to_xml()                                         #twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)   #twiML в конце перевожу в строку, потому что так было в примерчике




@app.route('/outbound2', methods=['GET', 'POST'])   #работа с вебом
def outbound2():
    strr = request.form.get('SpeechResult')   #работа с вебом
    print(strr)
    twiml_response = VoiceResponse()                                            #twiML элемент response с него всегда нужно начинать twiML
    twiml_response.say('hi silly boy')                                          #twiML текст2спич
    twiml_response.play('http://k003.kiwi6.com/hotlink/9njt732wby/lol.mp3')     #twiML проигрование mp3
    twiml_xml = twiml_response.to_xml()                                         #twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)   #twiML в конце перевожу в строку, потому что так было в примерчике




if __name__=='__main__':
    # nlp = spacy.load('en_core_web_sm')
    app.run()       #работа с вебом