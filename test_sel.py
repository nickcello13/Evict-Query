from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


def main():
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()

    court_view_root_uri = "https://eaccess.dccourts.gov/eaccess/home.page.2"

    driver.get(court_view_root_uri)
    driver.implicitly_wait(1)
    captcha_element = driver.find_element_by_class_name("captchaImg")

    src_img_url = captcha_element.get_property("src")
    print(src_img_url)

    # Not how the actual server would do it, but...
    possible_caption = input("What is the CAPTCHA for this image?")
    captcha_text_input_box = driver.find_element_by_id("id3")
    captcha_text_input_box.click()
    captcha_text_input_box.send_keys(possible_caption)
    captcha_text_input_box.send_keys(Keys.RETURN)  # press the return key

    # Now that we are "authenticated", let's get a case
    case_num_text_input_box = driver.find_element_by_id("caseDscr")
    sample_case_num_qry = "2017 LTB 000001"  # LTB = Landlord & Tenant Branch
    case_num_text_input_box.send_keys(sample_case_num_qry)
    case_num_text_input_box.send_keys(Keys.RETURN)

    # Take the first result, TODO: filter by isDefendant
    first_case_link = driver.find_element_by_id("grid$row:1$cell:3$link")
    first_case_link.click()

    # For proof of concept purposes, get the names of defendant and plaintiff.
    # In the real thing we'd probably download the HTML and process it later.
    party_info_box = driver.find_element_by_id("ptyInfo")
    party_1 = party_info_box.find_element_by_class_name("rowodd")
    party_2 = party_info_box.find_element_by_class_name("roweven")
    party_1_descr = party_1.find_element_by_class_name("subSectionHeader2")
    party_2_descr = party_2.find_element_by_class_name("subSectionHeader2")
    party_1_name, party_1_role = parse_party_descr(party_1_descr.text)
    party_2_name, party_2_role = parse_party_descr(party_2_descr.text)

    print(party_1_role + ": " + party_1_name)
    print(party_2_role + ": " + party_2_name)


def parse_party_descr(party_elem):
    normalized_descr = party_elem.strip().upper()
    if "DEFENDANT" in normalized_descr:
        role = "DEFENDANT"
    else:
        role = "PLAINTIFF"
    name = normalized_descr.replace(role, "").replace("-", "").strip()
    return name, role


if __name__ == '__main__':
    main()
