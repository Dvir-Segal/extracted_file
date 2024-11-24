# coding: utf-8

# GTO-MO-1-1 - Removed partial_header
# flake8: noqa

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


class JobStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "statusType",
            "status",
            "statusCode",
        }
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['JobState']:
                return JobState
        
            @staticmethod
            def statusCode() -> typing.Type['StatusCodes']:
                return StatusCodes
            
            
            class statusType(
                schemas.Int32Schema
            ):
                pass
            data = schemas.AnyTypeSchema
            __annotations__ = {
                "status": status,
                "statusCode": statusCode,
                "statusType": statusType,
                "data": data,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    statusType: MetaOapg.properties.statusType
    status: 'JobState'
    statusCode: 'StatusCodes'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusType"]) -> MetaOapg.properties.statusType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'JobState': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusCode"]) -> 'StatusCodes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["statusType"], typing_extensions.Literal["status"], typing_extensions.Literal["statusCode"], typing_extensions.Literal["data"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusType"]) -> MetaOapg.properties.statusType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'JobState': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusCode"]) -> 'StatusCodes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["statusType"], typing_extensions.Literal["status"], typing_extensions.Literal["statusCode"], typing_extensions.Literal["data"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        statusType: typing.Union[MetaOapg.properties.statusType, decimal.Decimal, int, ],
        status: 'JobState',
        statusCode: 'StatusCodes',
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'JobStatus':
        return super().__new__(
            cls,
            *_args,
            statusType=statusType,
            status=status,
            statusCode=statusCode,
            data=data,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.job_state import JobState
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.status_codes import StatusCodes