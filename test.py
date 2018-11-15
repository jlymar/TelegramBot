from nltk import FreqDist
from twilio.rest import Client
from  twilio.twiml.voice_response import VoiceResponse, Gather, Say
from urllib.parse import urlencode

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC671c96430c658ba3dcad064799a76411'
auth_token = '99cd9a620ebde1854eb5ba2b6ac31eaa'
client = Client(account_sid, auth_token)

# начало url для Say
url = "http://twimlets.com/message?"

# начало url для twiML
echo_ur = 'http://twimlets.com/echo?'

#twiML элемент response с него всегда нужно начинать twiML
response = VoiceResponse()
FreqDist
"""
Gather ==> тег собиратель данных. 
может возвращать цифры нажатые на клаве телефона.
или спич2текст текст. реагирует на паузу человека при разговоре.
ПАРАМЕТРЫ:
action ==> url webhook-а который обработает спич2текст текст и вернёт следующий twiML
input ==> speech/digit
speechTimeout ==> после какой паузы в речи (в секундах) заканчивать запись
"""
gather = Gather(action='https://71dd78c8.ngrok.io/outbound1', input='speech', speechTimeout=2)

#twiML текст2спич
gather.say('Hi, I am phoning about your car, is it still available?')

#twiML добавить гезер в респонс
response.append(gather)


gather = Gather(action='https://71dd78c8.ngrok.io/outbound1', input='speech', speechTimeout=2)

#twiML текст2спич
gather.say('could you reapeat your answer, please')

#twiML добавить гезер в респонс
response.append(gather)

#twiML текст2спич
response.say('We didn\'t receive any input. Goodbye!')

# twiML обязательный перевод в xml поскольку твилио это чистый xml
twiml_xml = response.to_xml()

# инициализировать звонок используя начало url и twiML переделаный в url адресс
call = client.calls.create(
                        url=echo_ur + urlencode({'Twiml': twiml_xml}),
                        to='+380959293096',
                        from_='+14302058972')



"""

https://www.twilio.com/docs/voice/tutorials/ivr-phone-tree-python-flask

https://www.twilio.com/docs/voice/twiml/record?code-sample=code-transcribe-a-recording&code-language=Python&code-sdk-version=6.x

https://handler.twilio.com/twiml/EHba3d144940b832f2a9cc667b546b4091
"""





"""
# from twilio.rest import Client


# # Your Account Sid and Auth Token from twilio.com/console
# account_sid = 'ACb9a56515df4fa1e373f4efb686ab6a6b'
# auth_token = 'c03ab74bc7f74be5ae61fabadb29fbb8'
# client = Client(account_sid, auth_token)
#
# call = client.calls.create(
#                         url='http://demo.twilio.com/docs/voice.xml',
#                         to='+380983589967',
#                         from_='+16822772468'
#                     )
#
# print(call.sid)
"""