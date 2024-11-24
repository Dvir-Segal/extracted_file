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

from chkp_harmony_endpoint_management_sdk.generated.saas import schemas


class EndpointTarget(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "machineId",
            "tenantId",
        }
        
        class properties:
            tenantId = schemas.StrSchema
            machineId = schemas.StrSchema
            __annotations__ = {
                "tenantId": tenantId,
                "machineId": machineId,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    machineId: MetaOapg.properties.machineId
    tenantId: MetaOapg.properties.tenantId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["machineId"]) -> MetaOapg.properties.machineId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["machineId"], typing_extensions.Literal["tenantId"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["machineId"]) -> MetaOapg.properties.machineId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["machineId"], typing_extensions.Literal["tenantId"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        machineId: typing.Union[MetaOapg.properties.machineId, str, ],
        tenantId: typing.Union[MetaOapg.properties.tenantId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EndpointTarget':
        return super().__new__(
            cls,
            *_args,
            machineId=machineId,
            tenantId=tenantId,
            _configuration=_configuration,
        )