import chatgpt_session
import api_server
import sys

driver = chatgpt_session.start(sys.argv[1], sys.argv[2])

api_server.start(driver)
