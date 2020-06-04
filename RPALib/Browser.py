import splinter
from robot.api.deco import keyword, library

@library
class Browser:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    
    def __init__(self):
        self.browser = None
        self.btype = None

    @keyword
    def open_firefox_browser(self):
        self.browser = splinter.Browser('firefox')
        self.btype = "firefox"
        return
    
    @keyword
    def open_firefox_browser_incognito(self):
        self.browser = splinter.Browser('firefox', incognito=True)
        self.btype = "firefox"
        return

    @keyword
    def open_firefox_browser_headless(self):
        self.browser = splinter.Browser('firefox', headless=True)
        self.btype = "firefox"
        return
    
    @keyword
    def open_firefox_browser_headless_incognito(self):
        self.browser = splinter.Browser('firefox', headless=True, incognito=True)
        self.btype = "firefox"
        return

    @keyword
    def open_chrome_browser(self):
        self.browser = splinter.Browser('chrome')
        self.btype = "chrome"
        return
    
    @keyword
    def open_chrome_browser_incognito(self):
        self.browser = splinter.Browser('chrome', incognito=True)
        self.btype = "chrome"
        return

    @keyword
    def open_chrome_browser_headless(self):
        self.browser = splinter.Browser('chrome', headless=True)
        self.btype = "chrome"
        return
    
    @keyword
    def open_chrome_browser_headless_incognito(self):
        self.browser = splinter.Browser('chrome', headless=True, incognito=True)
        self.btype = "chrome"
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
    def input_text(self, locator, text):
        element = self.get_element(locator)
        element.click()
        element.fill(text)
        return

    @keyword
    def click(self, locator):
        element = self.get_element(locator)
        element.click()            
        return
   
    @keyword
    def check_item(self, text):
        self.browser.check(text)
        return
           
    @keyword
    def is_text_present(self, text):
        assert self.browser.is_text_present(text)

    @keyword
    def url_contains(self, text):
        if text in self.browser.url:
            return True
        return False

    def get_element(self, locator):
        key, value = locator.split(":")
        element = None
        try:
            if key == "id":
                if self.browser.is_element_present_by_id(value, wait_time=5):
                    element = self.browser.find_by_id(value)
            elif key == "name":
                if self.browser.is_element_present_by_name(value, wait_time=5):
                    element = self.browser.find_by_name(value)
            elif key == "tag":
                if self.browser.is_element_present_by_tag(value, wait_time=5):
                    element = self.browser.find_by_tag(value)
            elif key == 'text':
                if self.browser.is_element_present_by_text(value, wait_time=5):
                    element = self.browser.find_by_text(value)
            elif key == 'xpath':
                if self.browser.is_element_present_by_xpath(value, wait_time=5):
                    element = self.browser.find_by_xpath(value)
            elif key == 'css':
                cval = ''+key+'[class="'+value+'"]'
                if self.browser.is_element_present_by_css(cval, wait_time=5):
                    element = self.browser.find_by_css(cval)
        except Exception as e:
            print(e)
            element = None
        return element