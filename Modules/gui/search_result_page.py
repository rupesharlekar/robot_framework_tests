from robotpageobjects import Page
from robot.api import logger
from Modules.util import NonPageUtils
from bs4 import BeautifulSoup
from robot.utils import asserts

class SearchResultPage(Page):

    NonPageUtils = NonPageUtils()
    selectors = NonPageUtils.get_selectors_from_obj_file("obj_search_result_page.py")

    def verify_results_counts_non_zero(self,searched_text):
        """
        verifies if the page title is contains the searched text
        verifies if the result count displayed greater than zero
        """

        current_title = self.get_title()
        asserts.assert_true(searched_text in current_title)
        logger.info("searched text %s is present in page title" %searched_text)

        refr = self.get_reference_elements('total_results')
        logger.info("web element for result is %s" %refr)

        result_stats = refr[0].get_attribute("innerHTML").split(" ")[1]
        total_result_fetched = int(result_stats.replace(',', ''))
        logger.info("total_result_fetched for searched_text is %s" %total_result_fetched)

        asserts.assert_true(total_result_fetched > 0, "Zero number of results were displayed")
        logger.info("Non zero number of result were displayed for searched_text")

        return self

    def verify_each_description_contains_searched_text(self,searched_text):
        """
        verifies if each of the result displayed on 1st google result page contains the search term atleast once
        """

        refr = self.get_reference_elements('elements_description_section')

        for i in range(1,len(refr)):
            web_html_content = refr[i].get_attribute("innerHTML")
            logger.info("web_html_content %s" %web_html_content)

            soup = BeautifulSoup(web_html_content, 'html.parser')

            len_em = soup.findAll('em')
            logger.info('number of bold searched term count in each search: %s' %len_em)

            # check that result set does not include '5 days ago or 19th March 2019 type of text'
            each_result = [em.string.lower() for em in len_em if 'ago' or '2019' not in web_html_content]
            logger.info('each_result %s' %each_result)

            if each_result:
                asserts.assert_true(searched_text.lower() in each_result)

        return self