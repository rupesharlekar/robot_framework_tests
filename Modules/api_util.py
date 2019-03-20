# -*- coding: utf-8 -*-
import requests
import  traceback
import json
import __builtin__
from robot.api import logger

class APIUtil():

    @staticmethod
    def get_auth_token(request_url, form_data, client_id ,client_secret):
        session = requests.Session()
        __builtin__.session = session

        try:
            logger.info(
                "Execute post request, url-[%s], form_data-[%s], client_id-[%s], client_secret-[%s]"
                % (request_url, form_data, client_id, client_secret))

            response = session.post(request_url, data=form_data, verify=False, allow_redirects=False,
                                        auth=(client_id, client_secret))
            logger.debug("response - [%s]" % response)

            response.raise_for_status()
            if 'error' in response.text:
                raise Exception("Error in API response")
            else:
                pass

            logger.info("Post request executed successfully.")
            logger.debug("cookies - [%s]" % session.cookies.get_dict())
            logger.debug("response status - [%s]" % response.status_code)
            logger.debug("response headers - %s" % response.headers)
            logger.debug("response content - %s" % response.text)

            return response
        except Exception as ex:
            traceback.print_exc()
            msg = str(ex) + '\n' + "Exception while executing post request. Request detail : " \
                                   "url - [%s], form_data - [%s], headers - [%s]" % (request_url, form_data, headers)
            raise Exception(msg)

    @staticmethod
    def execute_get_request(request_url, headers=None):
        session = __builtin__.session
        try:
            logger.info("Execute get request, url - [%s], headers - [%s]" % (request_url, headers))

            if headers is not None:
                response = session.get(request_url, headers=headers, verify=False)
            else:
                response = session.get(request_url, verify=False)

            response.raise_for_status()
            if 'error' in response.text:
                raise Exception("Error in API response")
            else:
                pass

            logger.info("Get request executed successfully.")
            logger.debug("cookies - [%s]" % session.cookies.get_dict())
            logger.debug("response status - [%s]" % response.status_code)
            logger.debug("response headers - %s" % response.headers)
            logger.debug("response content - %s" % response.text)

            return response
        except Exception as ex:
            traceback.print_exc()
            msg = str(ex) + '\n' + "Exception while executing get request. Request detail : " \
                                   "url - [%s], headers - [%s]" % (request_url, headers)
            raise Exception(msg)