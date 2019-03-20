import json
from robot.api import logger
import __builtin__
import Config
from Modules.api_util import APIUtil
from robot.utils import asserts

class ChapterVerse(object):

    __builtin__.base_url = Config.HTTP_SCHEME + Config.BASE_URL
    __builtin__.api_url = __builtin__.base_url + '/api' + Config.API_VERSION

    def authenticate_client(self):
        # import pdb;pdb.set_trace()
        client_id = Config.CLIENT_ID
        client_secret = Config.CLIENT_SECRET

        request_url = __builtin__.base_url + Config.OAUTH_URL
        data = {'grant_type': 'client_credentials', 'scope': 'verse chapter'}

        access_token_response = APIUtil.get_auth_token(request_url, data, client_id, client_secret)
        bearer_token = json.loads(access_token_response.text)['access_token']
        api_call_headers = {'Authorization': 'Bearer ' + bearer_token}
        logger.info("api_call_headers %s" %api_call_headers)
        __builtin__.api_call_headers = api_call_headers
        return self

    def verify_chapters_count(self,exp_chapter_count):
        request_url = __builtin__.api_url + Config.CHAPTER
        headers = __builtin__.api_call_headers

        response = APIUtil.execute_get_request(request_url, headers)

        chapters_resp = json.loads(response.text)
        logger.info("chapters_resp %s" % chapters_resp)

        asserts.assert_true(int(exp_chapter_count) == len(chapters_resp), "Expected and Actual Chapter do not match")

    def verify_chapter_meaning(self,chapter_no, exp_name_meaning):
        request_url = __builtin__.api_url + Config.CHAPTER + '/' + chapter_no
        headers = __builtin__.api_call_headers

        response = APIUtil.execute_get_request(request_url, headers)

        act_name_meaning = json.loads(response.text)['name_meaning']

        logger.info("act_name_meaning %s" % act_name_meaning)
        logger.info("exp_name_meaning %s" % exp_name_meaning)

        asserts.assert_true(act_name_meaning == exp_name_meaning, "Expected and Actual name meaning do not match")

    def verify_verse_count_in_chapter(self,chapter_no,verse_count):
        request_url = __builtin__.api_url + Config.CHAPTER + '/' + chapter_no + Config.VERSE
        headers = __builtin__.api_call_headers

        response = APIUtil.execute_get_request(request_url, headers)
        verse_resp = json.loads(response.text)
        logger.info("Actual verse count %s" % len(verse_resp))
        logger.info("Expected verse count %s" % verse_count)

        asserts.assert_true(int(verse_count) == len(verse_resp), "Expected and Actual verse count do not match")

    def verify_meaning_of_verse_number(self,verse_number,chapter_no,meaning):
        request_url = __builtin__.api_url + Config.CHAPTER + '/' + chapter_no + Config.VERSE + '/' + verse_number
        headers = __builtin__.api_call_headers

        response = APIUtil.execute_get_request(request_url, headers)
        verse_meaning = json.loads(response.text)['meaning']

        logger.info("Actual verse_meaning %s" % verse_meaning)
        asserts.assert_true(verse_meaning.startswith(meaning,0))
