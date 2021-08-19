from time import sleep

import undetected_chromedriver.v2 as uc

driver = ''
options = ''


def setup(url):
    options = uc.ChromeOptions()

    # setting profile
    options.user_data_dir = "c:\\temp\\profile"

    driver = uc.Chrome(options=options)
    with driver:
        driver.get(url)

if __name__ == '__main__':
    setup('google.ca')

    exit_str = 'form'
    while not driver.current_url.__contains__(exit_str):
        sleep(0.5)

    # sleep 10 seconds to make sure form loads
    sleep(10)
    i = 0
    while i <= 1000:
        val = ''
        if i <= 9:
            val += '0'
        if i <= 99:
            val += '0'

        submit = "submit"
        text_box = "text_box"
        val += str(i)
        try:
            print("Inputting: " + str(i))
            cvc = driver.find_element_by_id(text_box)
            activate = driver.find_element_by_id(submit)
            # clear the form input
            cvc.clear()

            # input the number
            cvc.send_keys(val)

            # click the submit button
            activate.click()

            # sleep 2 seconds to make sure the form reloads
            sleep(2)

            i = i + 1
        # if the form is unable to load
        except Exception:
            # sleep to ensure it loads
            sleep(15)
            # continue in the loop
            continue


