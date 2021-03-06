# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.controllers.routes_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..exceptions.error_exception import ErrorException
from ..exceptions.api_exception import APIException
import json

class RoutesController(BaseController):

    """A Controller to access Endpoints in the flowroutenumbersandmessaging API."""


    def create_an_inbound_route(self, body):
        """Does a POST request to /v2/routes.

        Creates a new inbound route which can then be associated with phone
        numbers. Please see "List Inbound Routes" to review the route values
        that you can associate with your Flowroute phone numbers.

        Args:
            body (NewRoute): The new inbound route to be created.

        Returns:
            mixed: Response from the API. CREATED

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/routes'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(json.loads(body)))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('401 Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 403:
            raise ErrorException('403 Forbidden – The server understood the request but refuses to authorize it.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('404 The specified resource was not found', _context)
        self.validate_response(_context)


        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def list_inbound_routes(self,
                            limit=None,
                            offset=None):
        """Does a GET request to /v2/routes.

        Returns a list of your inbound routes. From the list, you can then
        select routes to use as the primary and failover routes for a phone
        number, which you can do via "Update Primary Voice Route for a Phone
        Number" and "Update Failover Voice Route for a Phone Number".

        Args:
            limit (int, optional): Limits the number of routes to retrieve. A
                maximum of 200 items can be retrieved.
            offset (int, optional): Offsets the list of routes by your
                specified value. For example, if you have 4 inbound routes and
                you entered 1 as your offset value, then only 3 of your routes
                will be displayed in the response.

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/routes'
        _query_parameters = {
            'limit': limit,
            'offset': offset
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Unauthorized', _context)
        elif _context.response.status_code == 404:
            raise APIException('Not Found', _context)
        self.validate_response(_context)

        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_primary_voice_route(self, number_id, body):
        """Does a PATCH request to /v2/numbers/{number_id}/relationships/primary_route.

        Use this endpoint to update the primary voice route for a phone
        number. You must create the route first by following "Create an
        Inbound Route". You can then assign the created route by specifying
        its value in a PATCH request.

        Args:
            number_id (int): The phone number in E.164 11-digit North American
                format to which the primary route for voice will be assigned.
            body (void): The primary route to be assigned.

        Returns:
            void: Response from the API. NO CONTENT

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{number_id}/relationships/primary_route'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, {
            'number_id': number_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, parameters=APIHelper.json_serialize(json.loads(body)))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)

    def update_failover_voice_route(self,
                                                       number_id,
                                                       body):
        """Does a PATCH request to /v2/numbers/{number_id}/relationships/failover_route.

        Use this endpoint to update the failover voice route for a phone
        number. You must create the route first by following "Create an
        Inbound Route". You can then assign the created route by specifying
        its value in a PATCH request.

        Args:
            number_id (int): The phone number in E.164 11-digit North American
                format to which the failover route for voice will be
                assigned.
            body (void): The failover route to be assigned.

        Returns:
            void: Response from the API. NO CONTENT

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{number_id}/relationships/failover_route'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, {
            'number_id': number_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, parameters=APIHelper.json_serialize(json.loads(body)))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)
