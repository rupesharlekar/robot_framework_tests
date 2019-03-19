import os
from robot.api import logger

class NonPageUtils():

    def get_selectors_from_obj_file(self, file_name):
        """
        this file is used to collect all the locators from ObjectRepo/obj_*_page.py file
        """
        fullfilename = os.path.join(os.getcwd(), "ObjectRepo", file_name)
        objfile = file(fullfilename, "U").read()
        page_dict = {}
        exec objfile in page_dict
        selectors = page_dict['selectors']
        logger.info(selectors)

        return selectors
