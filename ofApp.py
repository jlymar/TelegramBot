from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
import spacy
from  ents import Ents

ngrok_url = 'http://28e81dff.ngrok.io/outbound'
nlp = spacy.load('en_core_web_sm')  # type: object
entities = Ents()
step = 1
negativ = False
positiv = False
app = Flask(__name__)  # работа с вебом


@app.route('/outboundP', methods=['GET', 'POST'])  # работа с вебом
def outboundP(text, hints, sufix='', add_step=True):
    global step, ngrok_url
    if add_step:
        step += 1
    twiml_response = VoiceResponse()
    gather = Gather(action=ngrok_url + str(step) + sufix, input='speech', speechTimeout='auto', hints=hints)
    gather.say(text)
    twiml_response.append(gather)
    twiml_response.say('We didn\'t receive any input. Goodbye!')
    return twiml_response.to_xml()


@app.route('/outboundN', methods=['GET', 'POST'])  # работа с вебом
def outboundN(text):
    twiml_response = VoiceResponse()
    twiml_response.say(text)  # twiML текст2спич
    twiml_response.hangup()
    return twiml_response.to_xml()


@app.route('/outboundCheck', methods=['GET', 'POST'])  # работа с вебом
def outboundCheck(strr):
    global positiv, negativ
    positiv, negativ = (False, False)

    print(strr)

    for i in entities.positive and not positiv:
        indx = strr.find(i)
        if indx != -1:
            positiv = True

    for i in entities.negative and not negativ:
        indx = strr.find(i)
        if indx != -1:
            negativ = True


@app.route('/outboundRepeat', methods=['GET', 'POST'])  # работа с вебом
def outboundRepeat():
    global step, ngrok_url
    response = VoiceResponse()
    gather = Gather(action=ngrok_url + str(step), input='speech', speechTimeout='auto')
    gather.say('could you reapeat your answer, please')
    response.append(gather)
    response.say('We didn\'t receive any input. Goodbye!')
    twiml_xml = response.to_xml()
    return str(twiml_xml)


@app.route('/outboundGlobal', methods=['GET', 'POST'])  # работа с вебом
def outboundGlobal(positive_text, negative_text, positive_hint=''):
    global positiv, negativ
    outboundCheck(request.form.get('SpeechResult'))

    if positiv:
        twiml_xml = outboundP(text=positive_text,
                              hints=positive_hint)

    elif negativ:
        twiml_xml = outboundN(negative_text)

    else:
        return outboundRepeat()

    return str(twiml_xml)


@app.route('/outbound1', methods=['GET', 'POST'])  # работа с вебом
def outbound1():
    global positiv, negativ
    outboundCheck(request.form.get('SpeechResult'))

    if positiv:
        twiml_xml = outboundP(text='Hi, my name is Gary I am calling from a company called "Sell my car" we buy cars direct from consumers.'
                   'Would you be interested in us making you an offer for your car? It takes just two minutes, and is valid for 7 days.',
                              hints='')

    elif negativ:
        twiml_xml = outboundN('Take care and goodbye for now.')

    else:
        return outboundRepeat()

    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound2', methods=['GET', 'POST'])  # работа с вебом
def outbound2():
    global positiv, negativ
    outboundCheck(request.form.get('SpeechResult'))

    if positiv:
        twiml_xml = outboundP(
            text='Can I start by confirming your vehicle registration number is?' + '',
            hints='')

    elif negativ:
        twiml_xml = outboundN('OK, thanks and sorry for bothering you.')

    else:
        return outboundRepeat()

    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound3', methods=['GET', 'POST'])  # работа с вебом
def outbound3():
    global positiv, negativ
    outboundCheck(request.form.get('SpeechResult'))

    if positiv:
        twiml_xml = outboundP(
            text='Can I confirm the mileage as ?' + '',
            hints='')

    elif negativ:
        twiml_xml = outboundP(
            text='Sorry can I take your registration please?',
            hints='', sufix='_1', add_step=False)

    else:
        return outboundRepeat()

    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound3_1', methods=['GET', 'POST'])  # работа с вебом
def outbound3_1():
    global negativ
    strr = request.form.get('SpeechResult')  # работа с вебом
    outboundCheck(strr)

    doc = nlp(strr)
    """
    
    
    """
    found = True
    if found:
        twiml_xml = outboundP(text='Can I confirm the mileage as ?' + '',
                              hints='')

    elif negativ:
        twiml_xml = outboundN('OK, thanks and sorry for bothering you.')

    else:
        return outboundRepeat()

    return str(twiml_xml)


@app.route('/outbound4', methods=['GET', 'POST'])  # работа с вебом
def outbound4():
    global positiv, negativ
    outboundCheck(request.form.get('SpeechResult'))

    if positiv:
        twiml_xml = outboundP(
            text='Can I just confirm you live in ?' + '',
            hints='')

    elif negativ:
        twiml_xml = outboundP(
            text='What is the correct mileage please?',
            hints='', sufix='_1', add_step=False)

    else:
        return outboundRepeat()

    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound4_1', methods=['GET', 'POST'])  # работа с вебом
def outbound4_1():
    global negativ
    strr = request.form.get('SpeechResult')  # работа с вебом
    outboundCheck(strr)

    doc = nlp(strr)
    """


    """
    found = True
    if found:
        twiml_xml = outboundP(text='Can I just confirm you live in ?' + '',
                              hints='')

    elif negativ:
        twiml_xml = outboundN('OK, thanks and sorry for bothering you.')

    else:
        return outboundRepeat()

    return str(twiml_xml)


@app.route('/outbound5', methods=['GET', 'POST'])  # работа с вебом
def outbound5():
    global positiv, negativ
    outboundCheck(request.form.get('SpeechResult'))

    if positiv:
        twiml_xml = outboundP(
            text='Can I confirm that your mobile number is ?' + '',
            hints='')

    elif negativ:
        twiml_xml = outboundP(
            text='What is the nearest town or city to you?',
            hints='', sufix='_1', add_step=False)

    else:
        return outboundRepeat()

    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound5_1', methods=['GET', 'POST'])  # работа с вебом
def outbound5_1():
    global negativ
    strr = request.form.get('SpeechResult')  # работа с вебом
    outboundCheck(strr)

    doc = nlp(strr)
    """


    """
    found = True
    if found:
        twiml_xml = outboundP(text='Can I confirm that your mobile number is ?' + '',
                              hints='')

    elif negativ:
        twiml_xml = outboundN('OK, thanks and sorry for bothering you.')

    else:
        return outboundRepeat()

    return str(twiml_xml)


@app.route('/outbound6', methods=['GET', 'POST'])  # работа с вебом
def outbound6():
    global positiv, negativ
    outboundCheck(request.form.get('SpeechResult'))

    if positiv:
        twiml_xml = outboundP(
            text='Which of the following describes your car service history'
                    'A. Full service history'
                    'B. Part service history'
                    'C. No service history',
            hints='')

    elif negativ:
        twiml_xml = outboundP(
            text='Can I take your mobile number please? We need this so we can text you your offer.',
            hints='', sufix='_1', add_step=False)

    else:
        return outboundRepeat()

    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound6_1', methods=['GET', 'POST'])  # работа с вебом
def outbound6_1():
    global negativ
    strr = request.form.get('SpeechResult')  # работа с вебом
    outboundCheck(strr)

    doc = nlp(strr)
    """


    """
    found = True
    if found:
        twiml_xml = outboundP(text='Which of the following describes your car service history'
                    'A. Full service history'
                    'B. Part service history'
                    'C. No service history',
                              hints='')

    elif negativ:
        twiml_xml = outboundN('OK, thanks and sorry for bothering you.')

    else:
        return outboundRepeat()

    return str(twiml_xml)


@app.route('/outbound7', methods=['GET', 'POST'])  # работа с вебом
def outbound7():
    strr = request.form.get('SpeechResult')  # работа с вебом
    doc = nlp(strr)
    """


    """

    twiml_xml = outboundP(
            text='''OK, thats the questions completed. In the next few minutes you will receive an offer from ourselves and a link to our website,
     where you can accept or decline our offer. If you choose to accept our offer you will then be able to book an appointment to drop your car off and collect your payment. 
     This can be done in as little as two hours. Thank you for your time today, I really hope you find our offer acceptable?
    ''',
            hints='')

    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


@app.route('/outbound8', methods=['GET', 'POST'])  # работа с вебом
def outbound8():
    global positiv
    outboundCheck(request.form.get('SpeechResult'))

    if positiv:
        twiml_xml = outboundN('Take care and goodbye for now.')

    else:
        twiml_xml = outboundN('If any of the above, say. OK no worries I have deleted your details, '
                           'if you change your mind just log on to www.sellmycar.direct.'
                           'Take care and goodbye for now.')

    return str(twiml_xml)  # twiML в конце перевожу в строку, потому что так было в примерчике


if __name__ == '__main__':
    app.run()  # работа с вебом