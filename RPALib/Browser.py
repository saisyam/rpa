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
    def check_if_title_is(self, title):
        print(self.browser.title)
        assert self.browser.title == title
    
    @keyword
    def close_browser(self):
        self.browser.quit()
        return