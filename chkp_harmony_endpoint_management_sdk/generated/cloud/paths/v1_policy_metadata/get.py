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

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.blade_family import BladeFamily
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.run_as_job import RunAsJob
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.job_or_result_rule_metadata_array import JobOrResultRuleMetadataArray
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.connection_state import ConnectionState

from . import path

# Query params
RuleFamilySchema = BladeFamily
ConnectionStateSchema = ConnectionState
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'ruleFamily': typing.Union[RuleFamilySchema, ],
        'connectionState': typing.Union[ConnectionStateSchema, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_rule_family = api_client.QueryParameter(
    name="ruleFamily",
    style=api_client.ParameterStyle.FORM,
    schema=RuleFamilySchema,
    explode=True,
)
request_query_connection_state = api_client.QueryParameter(
    name="connectionState",
    style=api_client.ParameterStyle.FORM,
    schema=ConnectionStateSchema,
    explode=True,
)
# Header params
XMgmtRunAsJobSchema = RunAsJob
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'x-mgmt-run-as-job': XMgmtRunAsJobSchema # GTO-EPSAD-1-1,
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_mgmt_run_as_job = api_client.HeaderParameter(
    name="x-mgmt-run-as-job",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XMgmtRunAsJobSchema,
    required=True,
)
_auth = [
    'cloudInfraJwt',
    'apiJwt',
]
SchemaFor200ResponseBodyApplicationJson = JobOrResultRuleMetadataArray


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
        self.payload: JobOrResultRuleMetadataArray = None
        self.http_response = None
        self.is_job = None
        self.duration: Duration = None
        self.request_id = None
        self.job_id = None


class BaseApi(api_client.Api):
    @typing.overload
    def _get_all_rules_metadata_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
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
    def _get_all_rules_metadata_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_all_rules_metadata_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
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

    def _get_all_rules_metadata_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = True,
    ) -> HarmonyResponse:
        """
        Gets the metadata of all runes. <p>Metadata refers to all information relating to the rule except it's actual settings</p>
    
        API Parameters:
         - x-mgmt-run-as-job: RunAsJob - Mandatory placed in "header_params" param
         - ruleFamily: BladeFamily - placed in "query_params" param, An optional 'Rule Family' filter. Used to filter the results to only the selected capability family (e.g. only 'Threat Prevention')
         - connectionState: ConnectionState - placed in "query_params" param, An optional 'Connection State' filter. Used to filter the results to only the selected Connection State (e.g. only  rules pertaining to policies for 'Connected' clients)
        """
        """
        Get the metadata of all rules
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
        prefix_separator_iterator = None
        for parameter in (
            request_query_rule_family,
            request_query_connection_state,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        session_id = self.api_client.configuration.api_key['session']['session_id']
        request_id = self.api_client.configuration.api_key['session']['request_id']

        parameter = api_client.QueryParameter(
                name="operationName",
                style=api_client.ParameterStyle.FORM,
                schema=str)
        
        if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
        
        serialized_data = parameter.serialize('GetAllRulesMetadata', prefix_separator_iterator)
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
        for parameter in (
            request_header_x_mgmt_run_as_job,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
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

        logger(f'Sending operation "get_all_rules_metadata" url "{final_url}" ...')

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
            error_logger(f'Receiving operation "get_all_rules_metadata" communication error for url "{final_url}" with status, reason "{e.reason}"')
            network_logger(f'Receiving "{final_url}" with reason "{e.reason}"')
            raise e

    
        response_payload = response.data.decode('utf-8') if response.data else ''

        response_options = {
            "status": response.status,
            "headers": dict(response.headers),
            "payload": response_payload,
        }

        logger(f'Receiving operation "get_all_rules_metadata" url "{final_url}" with status code "{response.status}"')
        network_logger(f'Receiving "{final_url}" with options: "{response_options}"')
    
        if not 200 <= response.status <= 299:
            error_logger(f'Receiving error operation "get_all_rules_metadata" url "{final_url}" with "{response_options}"')
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



class GetAllRulesMetadata(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names



    def get_all_rules_metadata(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),

        do_not_handle_job = False,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> HarmonyResponse:
        """
        Gets the metadata of all runes. <p>Metadata refers to all information relating to the rule except it's actual settings</p>
    
        API Parameters:
         - x-mgmt-run-as-job: RunAsJob - Mandatory placed in "header_params" param
         - ruleFamily: BladeFamily - placed in "query_params" param, An optional 'Rule Family' filter. Used to filter the results to only the selected capability family (e.g. only 'Threat Prevention')
         - connectionState: ConnectionState - placed in "query_params" param, An optional 'Connection State' filter. Used to filter the results to only the selected Connection State (e.g. only  rules pertaining to policies for 'Connected' clients)
        """
        skip_deserialization = True
        content_type: str = 'application/json'
        accept_content_types: str = ('application/json',)
        self.api_client.configuration.api_key['session']['do_not_handle_job'] = do_not_handle_job
        return self._get_all_rules_metadata_oapg(
            query_params=query_params,
            header_params=header_params,
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
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
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
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
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
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,

        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = True,
    ) -> HarmonyResponse:
        """
        Gets the metadata of all runes. <p>Metadata refers to all information relating to the rule except it's actual settings</p>
    
        API Parameters:
         - x-mgmt-run-as-job: RunAsJob - Mandatory placed in "header_params" param
         - ruleFamily: BladeFamily - placed in "query_params" param, An optional 'Rule Family' filter. Used to filter the results to only the selected capability family (e.g. only 'Threat Prevention')
         - connectionState: ConnectionState - placed in "query_params" param, An optional 'Connection State' filter. Used to filter the results to only the selected Connection State (e.g. only  rules pertaining to policies for 'Connected' clients)
        """
        return self._get_all_rules_metadata_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


