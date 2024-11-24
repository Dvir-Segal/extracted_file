# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import urllib3
from urllib3._collections import HTTPHeaderDict

from chkp_harmony_endpoint_management_sdk.generated.saas import api_client, exceptions
from datetime import date, datetime
import decimal
import functools
import io
import re
import typing
import typing_extensions
import uuid

import frozendict

from chkp_harmony_endpoint_management_sdk.generated.saas import schemas

from chkp_harmony_endpoint_management_sdk.generated.saas.model.public_mssp_structure_and_machines_info import PublicMsspStructureAndMachinesInfo
from chkp_harmony_endpoint_management_sdk.generated.saas.model.unauthorized_error_example import UnauthorizedErrorExample
from chkp_harmony_endpoint_management_sdk.generated.saas.model.internal_error_example import InternalErrorExample
from chkp_harmony_endpoint_management_sdk.generated.saas.model.forbidden_error_example import ForbiddenErrorExample

from . import path

_auth = [
    'cloudInfraJwt',
]
SchemaFor200ResponseBodyApplicationJson = PublicMsspStructureAndMachinesInfo


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    # GTO-E-1-2
    body: SchemaFor200ResponseBodyApplicationJson
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = UnauthorizedErrorExample


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    # GTO-E-1-2
    body: SchemaFor401ResponseBodyApplicationJson
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ForbiddenErrorExample


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    # GTO-E-1-2
    body: SchemaFor403ResponseBodyApplicationJson
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = InternalErrorExample


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    # GTO-E-1-2
    body: SchemaFor500ResponseBodyApplicationJson
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)

from unitsnet_py import Duration
import time
import json
from chkp_harmony_endpoint_management_sdk.core.job_manager import await_for_job
from chkp_harmony_endpoint_management_sdk.core.logger import logger, error_logger, network_logger
from chkp_harmony_endpoint_management_sdk.classes.harmony_api_exception import HarmonyApiException, HarmonyErrorScope

class HarmonyResponse:
    def __init__(self):
        self.payload: PublicMsspStructureAndMachinesInfo = None
        self.http_response = None
        self.is_job = None
        self.duration: Duration = None
        self.request_id = None
        self.job_id = None


class BaseApi(api_client.Api):
    @typing.overload
    def _tenants_status_oapg(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor401,
        ApiResponseFor403,
        ApiResponseFor500,
    ]: ...

    @typing.overload
    def _tenants_status_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _tenants_status_oapg(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor401,
        ApiResponseFor403,
        ApiResponseFor500,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _tenants_status_oapg(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = True,
    ) -> HarmonyResponse:
        """
        Gets the information about all the tenants in the MSSP account. The information includes: • Tenant name • Tenant ID • Endpoint servers’ status • Other operational related data if available.
    
        API Parameters:
        """
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
        prefix_separator_iterator = None

        session_id = self.api_client.configuration.api_key['session']['session_id']
        request_id = self.api_client.configuration.api_key['session']['request_id']

        parameter = api_client.QueryParameter(
                name="operationName",
                style=api_client.ParameterStyle.FORM,
                schema=str)
        
        if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
        
        serialized_data = parameter.serialize('TenantsStatus', prefix_separator_iterator)
        for serialized_value in serialized_data.values():
            used_path += serialized_value

        parameter = api_client.QueryParameter(
                name="requestId",
                style=api_client.ParameterStyle.FORM,
                schema=str)
        
        prefix_separator_iterator = parameter.get_prefix_separator_iterator()
        
        serialized_data = parameter.serialize(request_id, prefix_separator_iterator)
        for serialized_value in serialized_data.values():
            used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _headers.add("x-mgmt-data-session-id", session_id)
        _headers.add("x-mgmt-data-request-id", request_id)

        source_header = self.api_client.configuration.api_key['session']['source_header']
        if source_header:
            _headers.add("x-mgmt-data-request-source", source_header) 

        endpoint_token = self.api_client.configuration.api_key['session']['endpoint_token']
        if endpoint_token:
            _headers.add("x-mgmt-api-token", endpoint_token)

        infinity_portal_token = self.api_client.configuration.api_key['session']['infinity_portal_token']
        if infinity_portal_token:
            _headers.add("Authorization", f'Bearer {infinity_portal_token}')

        final_url = self.api_client.configuration.host + used_path

        logger(f'Sending operation "tenants_status" url "{final_url}" ...')

        request_options = {
            "method": 'get'.upper(),
            "headers": dict(_headers),
        }
        network_logger(f'Sending "{final_url}" with options: "{request_options}"')
        start_time = time.time()  
        try:

            response = self.api_client.call_api(
                resource_path=used_path,
                method='get'.upper(),
                headers=_headers,
                auth_settings=_auth,
                stream=stream,
                timeout=timeout,
            )
        except Exception as e:
            error_logger(f'Receiving operation "tenants_status" communication error for url "{final_url}" with status, reason "{e.reason}"')
            network_logger(f'Receiving "{final_url}" with reason "{e.reason}"')
            raise e

    
        response_payload = response.data.decode('utf-8') if response.data else ''

        response_options = {
            "status": response.status,
            "headers": dict(response.headers),
            "payload": response_payload,
        }

        logger(f'Receiving operation "tenants_status" url "{final_url}" with status code "{response.status}"')
        network_logger(f'Receiving "{final_url}" with options: "{response_options}"')
    
        if not 200 <= response.status <= 299:
            error_logger(f'Receiving error operation "tenants_status" url "{final_url}" with "{response_options}"')
            raise HarmonyApiException(
                error_scope=HarmonyErrorScope.SERVICE,
                request_id=request_id,
                payload_error=response_payload,
                url=final_url,
                status_code=response.status,
            )

        harmony_response = HarmonyResponse()

        json_payload = True

        harmony_response.http_response = response
        harmony_response.is_job = _headers.get('x-mgmt-run-as-job') == 'on'
        harmony_response.request_id = request_id

        if json_payload or harmony_response.is_job:
            harmony_response.payload = response.json()

        if (harmony_response.is_job):
            harmony_response.job_id = harmony_response.payload['jobId']
        
        if (harmony_response.is_job and not self.api_client.configuration.api_key['session']['do_not_handle_job']):
            job_status_operation = self.api_client.configuration.api_key['session']['job_status_operation']
            harmony_response.payload = await_for_job(job_id=harmony_response.job_id, job_status_operation=job_status_operation, request_id=request_id)

        end_time = time.time()
        harmony_response.duration = Duration.from_seconds(end_time - start_time)
        return harmony_response



class TenantsStatus(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names



    def tenants_status(
        self,

        do_not_handle_job = False,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> HarmonyResponse:
        """
        Gets the information about all the tenants in the MSSP account. The information includes: • Tenant name • Tenant ID • Endpoint servers’ status • Other operational related data if available.
    
        API Parameters:
        """
        skip_deserialization = True
        content_type: str = 'application/json'
        accept_content_types: str = ('application/json',)
        self.api_client.configuration.api_key['session']['do_not_handle_job'] = do_not_handle_job
        return self._tenants_status_oapg(
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor401,
        ApiResponseFor403,
        ApiResponseFor500,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor401,
        ApiResponseFor403,
        ApiResponseFor500,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = True,
    ) -> HarmonyResponse:
        """
        Gets the information about all the tenants in the MSSP account. The information includes: • Tenant name • Tenant ID • Endpoint servers’ status • Other operational related data if available.
    
        API Parameters:
        """
        return self._tenants_status_oapg(
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


