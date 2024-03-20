import ChatGTPClient from ../client/client_chatgtp.py

chatGtpClient = ChatGPTClient('http://localhost:5000')

position = read('position.txt')
shortCv = read('miniCV.txt')
myName = 'Luis Canals'

company = sys.argv[1]
jobTitle = sys.argv[2]

preRequestToChatGPT = \
    'Write a cover letter for the job title "[JobTitle]" ' \
    + 'for the company "[Company]" no more than 150 words, ' \
    + 'for this position:\n\n' \
    + '[Position]\n\n\n' \
    + 'adapted to my CV:\n\n' \
    + '[CV]\n'


request.replace('[JobTitle]', jobTitle)
request.replace('[Company]', company)
request.replace('[CV]', shortCV)
request.replace('[Position]', position)

print(request)
