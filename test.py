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






from twilio.rest import Client
from  twilio.twiml.voice_response import VoiceResponse, Gather, Say
from urllib.parse import urlencode

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC1e3a0dedbebe1ff677302e6436b59792'
auth_token = 'e72aed42d09e8e28b9b521e5b8518b95'
client = Client(account_sid, auth_token)

# Use the Twilio-provided site for the TwiML response.
url = "http://twimlets.com/message?"
echo_ur = 'http://twimlets.com/echo?'





response = VoiceResponse()
gather = Gather(action='https://910224e8.ngrok.io/outbound1', input='speech', speechTimeout='auto')
gather.say('say yes if you would like hear Vlad?')
response.append(gather)
response.say('We didn\'t receive any input. Goodbye!')
twiml_xml = response.to_xml()

call = client.calls.create(
                        url=echo_ur + urlencode({'Twiml': twiml_xml}),
                        to='+380938482501',
                        from_='+15172732542')


print(call.sid)



"""
https://handler.twilio.com/twiml/EHba3d144940b832f2a9cc667b546b4091

"""





"""
from twilio.twiml.voice_response import Play, VoiceResponse

response = VoiceResponse()
response.play('https://api.twilio.com/cowbell.mp3')

print(response)



from twilio.twiml.voice_response import Record, VoiceResponse

response = VoiceResponse()
response.record(timeout=10, transcribe=True)
print(response)


response = VoiceResponse()
response.record()


print(response)



from twilio.twiml.voice_response import Record, VoiceResponse, Say

response = VoiceResponse()
response.say(
    'Please leave a message at the beep.\nPress the star key when finished.'
)
response.record(
    action='http://foo.edu/handleRecording.php',
    method='GET',
    max_length=20,
    finish_on_key='*'
)
response.say('I did not receive a recording')

print(response)












print('Making a call...')
new_call = client.calls.create(to='XXXX', from_='YYYY', method='GET')

print('Serving TwiML')
twiml_response = VoiceResponse()
twiml_response.say('Hello!')
twiml_response.hangup()
twiml_xml = twiml_response.to_xml()
print('Generated twiml: {}'.format(twiml_xml))
"""
"""

https://www.twilio.com/docs/voice/tutorials/ivr-phone-tree-python-flask

https://www.twilio.com/docs/voice/twiml/record?code-sample=code-transcribe-a-recording&code-language=Python&code-sdk-version=6.x

"""