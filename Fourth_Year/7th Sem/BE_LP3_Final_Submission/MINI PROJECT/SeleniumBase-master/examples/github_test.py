from seleniumbase import BaseCase


class GitHubTests(BaseCase):
    def test_github(self):
        if self.headless:
            self.open_if_not_url("about:blank")
            print("\n  This test is not for Headless Mode.")
            self.skip('Do not use "--headless" with this test.')
        self.open("https://github.com/search?q=SeleniumBase")
        self.slow_click('a[href="/seleniumbase/SeleniumBase"]')
        self.click_if_visible('[data-action="click:signup-prompt#dismiss"]')
        self.highlight("div.Layout-main")
        self.highlight("div.Layout-sidebar")
        self.assert_element("div.repository-content")
        self.assert_text("SeleniumBase", "strong a")
        self.click('a[title="seleniumbase"]')
        self.slow_click('a[title="fixtures"]')
        self.assert_element('a[title="base_case.py"]')
