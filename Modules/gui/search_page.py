from robotpageobjects import Page
from robot.api import logger
from Modules.util import NonPageUtils
from robot.utils import asserts
import time

class SearchPage(Page):

    NonPageUtils = NonPageUtils()
    selectors = NonPageUtils.get_selectors_from_obj_file("obj_search_page.py")

    def verify_google_landing_page(self):
        """

        :return:
        """
        self.title_should_be("Google")
        self.wait_until_element_is_visible("google_logo", 5)
        logger.info("Landed on Google Main Page")
        return self

    def enter_search_text(self,search_text):
        """

        :param search_text:
        :return:
        """
        self.input_text('input_search_textbx', search_text)
        logger.info("entered text in search box")
        return self

    def click_google_search_button(self):
        """

        :return:
        """
        self.click_element('btn_google_search')
        logger.info("clicked on 'google search' button")
        return self

    def click_i_am_feeling_lucky_button(self):
        """

        :return:
        """
        self.click_element('btn_i_am_feeling_lucky')
        logger.info("clicked on 'i am feeling lucky' button")
        return self

    def enter_search_text_scroll_through_suggestion(self, search_text, select_option=2):
        """

        :param search_text:
        :param select_option:
        """
        logger.info("starting to select from auto suggest")
        self.input_text('input_search_textbx', search_text)
        logger.info("entered text in search box")
        time.sleep(1)

        li_locator = self.selectors['auto_suggest_list_common_xpath'].replace("v", select_option)
        logger.info("li_locator: %s" %li_locator)

        self.click_element(li_locator)
        logger.info("clicked on %s option from auto suggestion list" %select_option)

        return self
