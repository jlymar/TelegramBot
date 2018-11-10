from twilio.rest import Client


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


"""


params = {
    'to': '2222222222',    # The phone numer to which the call will be placed     
    'from' : '1111111111', # The phone number to be used as the caller id 
    # answer_url is the URL invoked by Plivo when the outbound call is answered     
    # and contains instructions telling Plivo what to do with the call     
    'answer_url' : "https://s3.amazonaws.com/static.plivo.com/answer.xml",
    'answer_method' : "GET", # The method used to call the answer_url  }

# Make an outbound call and print the response response = p.make_call(params)
print str(response)





https://pythonspot.com/

https://www.twilio.com/docs/voice/tutorials/ivr-phone-tree-python-flask

https://www.twilio.com/docs/voice/twiml/record?code-sample=code-transcribe-a-recording&code-language=Python&code-sdk-version=6.x

"""