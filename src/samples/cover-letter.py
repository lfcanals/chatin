from client.client_chatgpt import ChatGPTClient 
import sys

chatGtpClient = ChatGPTClient('http://localhost:5000')

position = open('position.txt', 'r').read()
shortCV = open('miniCV.txt','r').read()

myName = sys.argv[1]
company = sys.argv[2]
jobTitle = sys.argv[3]

request = \
    'Write a cover letter for the job title "[JobTitle]" ' \
    + 'for the company "[Company]" no more than 150 words, ' \
    + 'for this position:\n\n' \
    + '[Position]\n\n\n' \
    + 'adapted to my CV:\n\n' \
    + '[CV]\n'


request = request.replace('[JobTitle]', jobTitle)
request = request.replace('[Company]', company)
request = request.replace('[CV]', shortCV)
request = request.replace('[Position]', position)

print(chatGtpClient.query(request))
