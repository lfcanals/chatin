from flask import Flask, jsonify, request
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


app = Flask(__name__)
driver = None

def start(webdriver):
    global driver
    driver = webdriver
    app.run(debug=True, use_reloader=False)


@app.route('/chatin/api/v1.0/query', methods=['POST'])
def query_to_chatgpt():
    if not request.json or not 'message' in request.json:
        abort(400)

    textArea = driver.find_element(By.ID, "prompt-textarea")
    textArea.send_keys(request.json['message'])

    driver.find_element(By.CSS_SELECTOR, "button[data-testid='send-button']")\
            .click()

    # Wait until it finishes.....

    WebDriverWait(driver, 120).until(EC.visibility_of_element_located( \
            (By.CSS_SELECTOR, "button[data-testid='send-button']")))

    print("Response ready...")
    response = driver.find_elements(By.XPATH,"//*[@class='markdown prose w-full break-words dark:prose-invert dark']")
    answer = [ {'message': response[-1].text} ]

    return jsonify(answer)
    

