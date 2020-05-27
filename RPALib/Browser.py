import splinter
from robot.api.deco import keyword, library

@library
class Browser:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    
    def __init__(self):
        self.browser = None

    @keyword
    def open_chrome_browser(self):
        self.browser = splinter.Browser('chrome')
        return

    @keyword
    def open_chrome_browser_headless(self):
        self.browser = splinter.Browser('chrome', headless=True)
        return
    
    @keyword
    def open_url(self, url):
        self.browser.visit(url)
        return

    @keyword
    def get_title(self):
        return self.browser.title

    @keyword
    def check_if_title_is(self, title):
        assert self.browser.title == title
    
    @keyword
    def close_browser(self):
        self.browser.quit()
        return
    
    @keyword
    def input_text(self, field, text):
        self.browser.fill(field, text)
        return

    @keyword
    def click_button(self, locator):
        element = self.get_element(locator)
        element.click()
        return

    @keyword
    def click_item_by_class(self, locator):
        key, value = locator.split(":")
        element = self.browser.find_by_css(''+key+'[class="'+value+'"]')
        element.click()
        return
    
    @keyword
    def click_item_by_text(self, text):
        element = self.browser.find_by_text(text)
        element.click()
        return
    
    @keyword
    def is_text_present(self, text):
        assert self.browser.is_text_present(text)

    def get_element(self, locator):
        key, value = locator.split(":")
        element = None
        try:
            if key == "id":
                element = self.browser.find_by_id(value)
            elif key == "name":
                element = self.browser.find_by_name(value)
        except Exception as e:
            element = None
        return element