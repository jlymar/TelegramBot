from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
import spacy

ngrok_url = 'http://28e81dff.ngrok.io/outbound'
step = 1
app = Flask(__name__)  # работа с вебом


@app.route('/outbound1', methods=['GET', 'POST'])  # работа с вебом
def outbound1():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    if 'positive' in doc.ents.keys:

        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Hi, my name is Gary I am calling from a company called "Sell my car" we buy cars direct from consumers.'
                   'Would you be interested in us making you an offer for your car? It takes just two minutes, and is valid for 7 days.')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        twiml_response.say('Take care and goodbye for now.')  # twiML текст2спич
        twiml_response.hangup()
    else:
     return outboundRepeat()


    twiml_xml = twiml_response.to_xml()  # twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound2', methods=['GET', 'POST'])  # работа с вебом
def outbound2():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    if 'positive' in doc.ents.keys:
        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Can I start by confirming your vehicle registration number is?' + '___________')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        twiml_response.say('OK, thanks and sorry for bothering you.')  # twiML текст2спич
        twiml_response.hangup()
    else:
     return outboundRepeat()


    twiml_xml = twiml_response.to_xml()  # twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике



@app.route('/outbound3', methods=['GET', 'POST'])  # работа с вебом
def outbound3():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    if 'positive' in doc.ents.keys:
        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Can I confirm the mileage as ?' + '_____________')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        gather = Gather(action=ngrok_url + str(step) +'_1', input='speech', speechTimeout='auto', hints='')
        gather.say('Sorry can I take your registration please?')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')

    else:
     return outboundRepeat()


    twiml_xml = twiml_response.to_xml()  # twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound3_1', methods=['GET', 'POST'])  # работа с вебом
def outbound3_1():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    found = True
    if found:
        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Can I confirm the mileage as ?' + '_____________')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        twiml_response.say('OK, thanks and sorry for bothering you.')  # twiML текст2спич
        twiml_response.hangup()
    else:
        return outboundRepeat()



@app.route('/outbound4', methods=['GET', 'POST'])  # работа с вебом
def outbound4():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    if 'positive' in doc.ents.keys:
        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Can I just confirm you live in ?' + '_____________')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        gather = Gather(action=ngrok_url + str(step) + '_1', input='speech', speechTimeout='auto', hints='')
        gather.say('What is the correct mileage please?')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    else:
     return outboundRepeat()


    twiml_xml = twiml_response.to_xml()  # twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound4_1', methods=['GET', 'POST'])  # работа с вебом
def outbound4_1():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    found = True
    if found:
        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Can I just confirm you live in ?' + '_____________')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        twiml_response.say('OK, thanks and sorry for bothering you.')  # twiML текст2спич
        twiml_response.hangup()
    else:
        return outboundRepeat()


@app.route('/outbound5', methods=['GET', 'POST'])  # работа с вебом
def outbound5():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    if 'positive' in doc.ents.keys:
        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Can I confirm that your mobile number is ?' + '_____________')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        gather = Gather(action=ngrok_url + str(step) + '_1', input='speech', speechTimeout='auto', hints='')
        gather.say('What is the nearest town or city to you?')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    else:
     return outboundRepeat()


    twiml_xml = twiml_response.to_xml()  # twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике

@app.route('/outbound5_1', methods=['GET', 'POST'])  # работа с вебом
def outbound5_1():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    found = True
    if found:
        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Can I confirm that your mobile number is ?' + '_____________')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        twiml_response.say('OK, thanks and sorry for bothering you.')  # twiML текст2спич
        twiml_response.hangup()
    else:
        return outboundRepeat()



@app.route('/outbound6', methods=['GET', 'POST'])  # работа с вебом
def outbound6():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    if 'positive' in doc.ents.keys:
        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Which of the following describes your car service history'
                    'A. Full service history'
                    'B. Part service history'
                    'C. No service history')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        gather = Gather(action=ngrok_url + str(step) + "_1", input='speech', speechTimeout='auto', hints='')
        gather.say('Can I take your mobile number please? We need this so we can text you your offer.')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    else:
     return outboundRepeat()


    twiml_xml = twiml_response.to_xml()  # twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound6_1', methods=['GET', 'POST'])  # работа с вебом
def outbound6_1():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    found = True
    if found:
        step += 1
        gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
        gather.say('Which of the following describes your car service history'
                    'A. Full service history'
                    'B. Part service history'
                    'C. No service history')
        twiml_response.append(gather)
        twiml_response.say('We didn\'t receive any input. Goodbye!')
    elif 'negative' in doc.ents.keys:
        twiml_response.say('OK, thanks and sorry for bothering you.')  # twiML текст2спич
        twiml_response.hangup()
    else:
        return outboundRepeat()



@app.route('/outbound7', methods=['GET', 'POST'])  # работа с вебом
def outbound7():
    global step
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    step += 1
    gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto', hints='')
    gather.say('''OK, thats the questions completed. In the next few minutes you will receive an offer from ourselves and a link to our website,
     where you can accept or decline our offer. If you choose to accept our offer you will then be able to book an appointment to drop your car off and collect your payment. 
     This can be done in as little as two hours. Thank you for your time today, I really hope you find our offer acceptable?
    ''')
    twiml_response.append(gather)
    twiml_response.say('We didn\'t receive any input. Goodbye!')


    twiml_xml = twiml_response.to_xml()  # twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике





@app.route('/outbound8', methods=['GET', 'POST'])  # работа с вебом
def outbound8():
    global step
    step = 1
    twiml_response = VoiceResponse()
    strr = request.form.get('SpeechResult')  # работа с вебом
    print(strr)
    doc = nlp(strr)

    if 'positive' in doc.ents.keys:
        twiml_response.say('Take care and goodbye for now.')
        twiml_response.hangup()
    else:
        twiml_response.say('If any of the above, say. OK no worries I have deleted your details, '
                           'if you change your mind just log on to www.sellmycar.direct.'
                           'Take care and goodbye for now.')
        twiml_response.hangup()

    twiml_xml = twiml_response.to_xml()  # twiML обязательный перевод в xml поскольку твилио это чистый xml
    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outboundRepeat', methods=['GET', 'POST'])  # работа с вебом
def outboundRepeat():
    global step
    response = VoiceResponse()

    gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto')
    gather.say('could you reapeat your answer, please')
    response.append(gather)
    response.say('We didn\'t receive any input. Goodbye!')
    twiml_xml = response.to_xml()
    return str(twiml_xml)





if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    app.run()  # работа с вебом