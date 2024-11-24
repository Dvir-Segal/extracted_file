# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import urllib3
from urllib3._collections import HTTPHeaderDict

from chkp_harmony_endpoint_management_sdk.generated.cloud import api_client, exceptions
from datetime import date, datetime
import decimal
import functools
import io
import re
import typing
import typing_extensions
import uuid

import frozendict

from chkp_harmony_endpoint_management_sdk.generated.cloud import schemas

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.job_status import JobStatus

from . import path

# Path params
JobIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'jobId': typing.Union[JobIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_job_id = api_client.PathParameter(
    name="jobId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=JobIdSchema,
    required=True,
)
_auth = [
    'cloudInfraJwt',
    'apiJwt',
]
SchemaFor200ResponseBodyApplicationJson = JobStatus


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


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
)
_status_code_to_response = {
    '200': _response_for_200,
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
        self.payload: JobStatus = None
        self.http_response = None
        self.is_job = None
        self.duration: Duration = None
        self.request_id = None
        self.job_id = None


class BaseApi(api_client.Api):
    @typing.overload
    def _get_job_by_id_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor403,
        ApiResponseFor500,
    ]: ...

    @typing.overload
    def _get_job_by_id_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_job_by_id_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor403,
        ApiResponseFor500,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_job_by_id_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = True,
    ) -> HarmonyResponse:
        """
        Retrieves the status and result (if any) of a given asynchronous operation. <p>A Job is a way to monitor the progress of an asynchronous operation whilst avoiding issues that may manifest during long synchronous waits.</p>  <p>For example, a search for a particular computer in the organization may take a considerable amount of time in large organizations so the '/computers/by-filter' API has been made to return a Job. </br>This means that, when invoked, the operation returns an object with a 'jobId' field. That Job can then be queried and, when completed, will contain the result of the '/computers/by-filter' operation.</p> <p><h3>It is important to note that once a job concludes (i.e. is 'DONE' or 'FAILED') it has fulfilled its purpose and is no longer useful</h3></p> <p>As such, Jobs should be treated as 'single-use'. Once concluded, they should be 'discarded'</p>
    
        API Parameters:
         - jobId: str - Mandatory placed in "path_params" param, The ID of the operation to query the status of
        """
        """
        Retrieve the status and result of an asynchronous operation
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_job_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
        prefix_separator_iterator = None

        session_id = self.api_client.configuration.api_key['session']['session_id']
        request_id = self.api_client.configuration.api_key['session']['request_id']

        parameter = api_client.QueryParameter(
                name="operationName",
                style=api_client.ParameterStyle.FORM,
                schema=str)
        
        if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
        
        serialized_data = parameter.serialize('GetJobById', prefix_separator_iterator)
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

        logger(f'Sending operation "get_job_by_id" url "{final_url}" ...')

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
            error_logger(f'Receiving operation "get_job_by_id" communication error for url "{final_url}" with status, reason "{e.reason}"')
            network_logger(f'Receiving "{final_url}" with reason "{e.reason}"')
            raise e

    
        response_payload = response.data.decode('utf-8') if response.data else ''

        response_options = {
            "status": response.status,
            "headers": dict(response.headers),
            "payload": response_payload,
        }

        logger(f'Receiving operation "get_job_by_id" url "{final_url}" with status code "{response.status}"')
        network_logger(f'Receiving "{final_url}" with options: "{response_options}"')
    
        if not 200 <= response.status <= 299:
            error_logger(f'Receiving error operation "get_job_by_id" url "{final_url}" with "{response_options}"')
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



class GetJobById(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names



    def get_job_by_id(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),

        do_not_handle_job = False,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> HarmonyResponse:
        """
        Retrieves the status and result (if any) of a given asynchronous operation. <p>A Job is a way to monitor the progress of an asynchronous operation whilst avoiding issues that may manifest during long synchronous waits.</p>  <p>For example, a search for a particular computer in the organization may take a considerable amount of time in large organizations so the '/computers/by-filter' API has been made to return a Job. </br>This means that, when invoked, the operation returns an object with a 'jobId' field. That Job can then be queried and, when completed, will contain the result of the '/computers/by-filter' operation.</p> <p><h3>It is important to note that once a job concludes (i.e. is 'DONE' or 'FAILED') it has fulfilled its purpose and is no longer useful</h3></p> <p>As such, Jobs should be treated as 'single-use'. Once concluded, they should be 'discarded'</p>
    
        API Parameters:
         - jobId: str - Mandatory placed in "path_params" param, The ID of the operation to query the status of
        """
        skip_deserialization = True
        content_type: str = 'application/json'
        accept_content_types: str = ('application/json',)
        self.api_client.configuration.api_key['session']['do_not_handle_job'] = do_not_handle_job
        return self._get_job_by_id_oapg(
            path_params=path_params,
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
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor403,
        ApiResponseFor500,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor403,
        ApiResponseFor500,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = True,
    ) -> HarmonyResponse:
        """
        Retrieves the status and result (if any) of a given asynchronous operation. <p>A Job is a way to monitor the progress of an asynchronous operation whilst avoiding issues that may manifest during long synchronous waits.</p>  <p>For example, a search for a particular computer in the organization may take a considerable amount of time in large organizations so the '/computers/by-filter' API has been made to return a Job. </br>This means that, when invoked, the operation returns an object with a 'jobId' field. That Job can then be queried and, when completed, will contain the result of the '/computers/by-filter' operation.</p> <p><h3>It is important to note that once a job concludes (i.e. is 'DONE' or 'FAILED') it has fulfilled its purpose and is no longer useful</h3></p> <p>As such, Jobs should be treated as 'single-use'. Once concluded, they should be 'discarded'</p>
    
        API Parameters:
         - jobId: str - Mandatory placed in "path_params" param, The ID of the operation to query the status of
        """
        return self._get_job_by_id_oapg(
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


