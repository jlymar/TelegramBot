import spacy
import time

# from spacy.language import Language
# nlp = Language().from_disk('/home/user/Model1')
nlp = spacy.load('/home/user/Model1')











































"""

start = time.time()
# Process whole documents
text = (u"When Sebastian Thrun started working on self-driving cars at "
        u"Google in 2007, few people outside of the company took him "
        u"seriously. “I can tell you very senior CEOs of major American "
        u"car companies would shake my hand and turn away because I wasn’t "
        u"worth talking to,” said Thrun, now the co-founder and CEO of "
        u"online higher education startup Udacity, in an interview with? yes or not "
        u"Recode earlier this week.")
doc = nlp(text)

# Find named entities, phrases and concepts
for ent in doc.ents:
    print(ent.label_, ent.text)
finish1 = time.time() - start


output_dir='/home/user/Model1'
test_text = 'yes it is still available but I am at work right now, can I call you back?'
print("Loading from", output_dir)
nlp2 = spacy.load(output_dir)
doc2 = nlp2(test_text)
for ent in doc2.ents:
    print(ent.label_, ent.text)

"""



'''
nlp = spacy.load('en_core_web_lg')



start = time.time()

# Process whole documents
text = (u"When Sebastian Thrun started working on self-driving cars at "
        u"Google in 2007, few people outside of the company took him "
        u"seriously. “I can tell you very senior CEOs of major American "
        u"car companies would shake my hand and turn away because I wasn’t "
        u"worth talking to,” said Thrun, now the co-founder and CEO of "
        u"online higher education startup Udacity, in an interview with "
        u"Recode earlier this week.")
doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
finish2 = time.time() - start


print(finish1, "/////", finish2)
'''

'''

from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import random

# ASCII A to Z are 65 to 90

hel = [75, 25, 15, 130, 120]
beb = [110, 2, 60, 135, 150]


#use a truetype font
#font = ImageFont.truetype("Helvetica-Bold.ttf", 120)
font = ImageFont.truetype("BebasNeueBold.ttf", 150)


rtc = 67
bias = 10
for r in range(rtc+1):
    if r < 4:
        for k in range(1000):
            if r < 10:
                number_plate_1 = "KA 0" + str(r)
            else:
                number_plate_1 = "KA " + str(r)
            number_plate_2 = (chr(random.randint(65, 90))+chr(random.randint(65, 90))+" " + str(random.randint(1000, 9999)))
            img = np.zeros((256, 512, 3), np.uint8)
            pil_img = Image.fromarray(img)
            draw = ImageDraw.Draw(pil_img)

            draw.text((75, 25), number_plate_1, font=font)
            draw.text((15, 130), number_plate_2, font=font)
            cv2_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            cv2_img = cv2.bitwise_not(cv2_img)

            #cv2.imshow("number_plate", cv2_img)
            cv2.imwrite(number_plate_1+" "+number_plate_2+".png", cv2_img)
            #cv2.waitKey(10)
    else:
        for k in range(100):
            if r < 10:
                number_plate_1 = "KA 0" + str(r)
            else:
                number_plate_1 = "KA " + str(r)
            number_plate_2 = (chr(random.randint(65, 90))+chr(random.randint(65, 90))+" " + str(random.randint(1000, 9999)))
            img = np.zeros((256, 512, 3), np.uint8)
            pil_img = Image.fromarray(img)
            draw = ImageDraw.Draw(pil_img)

            draw.text((75, 25), number_plate_1, font=font)
            draw.text((15, 130), number_plate_2, font=font)
            cv2_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            cv2_img = cv2.bitwise_not(cv2_img)

            #cv2.imshow("number_plate", cv2_img)
            cv2.imwrite(number_plate_1+" "+number_plate_2+".png", cv2_img)
            #cv2.waitKey(10)



cv2.destroyAllWindows()

'''