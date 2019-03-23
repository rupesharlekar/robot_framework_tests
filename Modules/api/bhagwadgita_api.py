import json
from robot.api import logger
import __builtin__
import Config
import requests
from Modules.api_util import APIUtil
from robot.utils import asserts

class ChapterVerse(object):

    def __init__(self):
        self.base_url = Config.HTTP_SCHEME + Config.BASE_URL
        self.api_url = self.base_url + '/api' + Config.API_VERSION

    def authenticate_client(self):
        """
        Generates the Access Token using https://bhagavadgita.io/auth/oauth/token
        Prepare the Authentication Header for other APIs to use
        """
        # import pdb;pdb.set_trace()
        client_id = Config.CLIENT_ID
        client_secret = Config.CLIENT_SECRET

        request_url = self.base_url + Config.OAUTH_URL
        data = {'grant_type': 'client_credentials', 'scope': 'verse chapter'}

        access_token_response = APIUtil.get_auth_token(request_url, data, client_id, client_secret)
        bearer_token = json.loads(access_token_response.text)['access_token']
        api_call_headers = {'Authorization': 'Bearer ' + bearer_token}
        logger.info("api_call_headers %s" %api_call_headers)
        __builtin__.api_call_headers = api_call_headers
        return self

    def verify_chapters_count(self,exp_chapter_count):
        """
        Verify the response for API https://bhagavadgita.io/api/v1/chapters
        :param exp_chapter_count: expected chapter count
        """
        request_url = self.api_url + Config.CHAPTER
        headers = __builtin__.api_call_headers

        response = APIUtil.execute_get_request(request_url, headers)
        logger.info("verify_chapters_count HTTP Response code is %s" % response.status_code)
        asserts.assert_true(response.status_code == requests.codes.ok, "Response code do not match")

        chapters_resp = json.loads(response.text)
        logger.info("chapters_resp %s" % chapters_resp)
        asserts.assert_true(int(exp_chapter_count) == len(chapters_resp), "Expected and Actual Chapter do not match")

    def verify_chapter_meaning(self,chapter_no, exp_name_meaning):
        """
        Verify the response for API https://bhagavadgita.io/api/v1/chapters/2
        :param chapter_no: chapter number to GET
        :param exp_name_meaning: Expected name_meaning response parameter value
        """
        request_url = self.api_url + Config.CHAPTER + '/' + chapter_no
        headers = __builtin__.api_call_headers

        response = APIUtil.execute_get_request(request_url, headers)
        logger.info("verify_chapter_meaning HTTP Response code is %s" % response.status_code)
        asserts.assert_true(response.status_code == requests.codes.ok, "Response code do not match")

        act_name_meaning = json.loads(response.text)['name_meaning']
        logger.info("act_name_meaning %s" % act_name_meaning)
        logger.info("exp_name_meaning %s" % exp_name_meaning)
        asserts.assert_true(act_name_meaning == exp_name_meaning, "Expected and Actual name meaning do not match")

    def verify_verse_count_in_chapter(self,chapter_no,verse_count):
        """
        Verify the response for API https://bhagavadgita.io/api/v1/chapters/2/verses
        :param chapter_no: chapter number to GET
        :param verse_count: Expected total number of verses in chapter number
        """
        request_url = self.api_url + Config.CHAPTER + '/' + chapter_no + Config.VERSE
        headers = __builtin__.api_call_headers

        response = APIUtil.execute_get_request(request_url, headers)
        logger.info("verify_chapter_meaning HTTP Response code is %s" % response.status_code)
        asserts.assert_true(response.status_code == requests.codes.ok, "Response code do not match")

        verse_resp = json.loads(response.text)
        logger.info("Actual verse count %s" % len(verse_resp))
        logger.info("Expected verse count %s" % verse_count)
        asserts.assert_true(int(verse_count) == len(verse_resp), "Expected and Actual verse count do not match")

    def verify_meaning_of_verse_number(self,verse_number,chapter_no,meaning):
        """
        Verify the response for API https://bhagavadgita.io/api/v1/chapters/2/verses/15
        :param verse_number: verse number to GET
        :param chapter_no: chapter number to GET
        :param meaning: Expected meaning Prefix of the verse
        """
        request_url = self.api_url + Config.CHAPTER + '/' + chapter_no + Config.VERSE + '/' + verse_number
        headers = __builtin__.api_call_headers

        response = APIUtil.execute_get_request(request_url, headers)
        logger.info("verify_meaning_of_verse_number HTTP Response code is %s" % response.status_code)
        asserts.assert_true(response.status_code == requests.codes.ok, "Response code do not match")

        verse_meaning = json.loads(response.text)['meaning']
        logger.info("Actual verse_meaning %s" % verse_meaning)
        asserts.assert_true(verse_meaning.startswith(meaning,0),"Verse meaning does not start with {}".format(meaning))