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


class Posture(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
            lastScanStatus = schemas.StrSchema
            lastScanStatusDescription = schemas.StrSchema
            lastScanManualStarted = schemas.StrSchema
            __annotations__ = {
                "lastScanStatus": lastScanStatus,
                "lastScanStatusDescription": lastScanStatusDescription,
                "lastScanManualStarted": lastScanManualStarted,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastScanStatus"]) -> MetaOapg.properties.lastScanStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastScanStatusDescription"]) -> MetaOapg.properties.lastScanStatusDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastScanManualStarted"]) -> MetaOapg.properties.lastScanManualStarted: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lastScanStatus"], typing_extensions.Literal["lastScanStatusDescription"], typing_extensions.Literal["lastScanManualStarted"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastScanStatus"]) -> typing.Union[MetaOapg.properties.lastScanStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastScanStatusDescription"]) -> typing.Union[MetaOapg.properties.lastScanStatusDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastScanManualStarted"]) -> typing.Union[MetaOapg.properties.lastScanManualStarted, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lastScanStatus"], typing_extensions.Literal["lastScanStatusDescription"], typing_extensions.Literal["lastScanManualStarted"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        lastScanStatus: typing.Union[MetaOapg.properties.lastScanStatus, str, schemas.Unset] = schemas.unset,
        lastScanStatusDescription: typing.Union[MetaOapg.properties.lastScanStatusDescription, str, schemas.Unset] = schemas.unset,
        lastScanManualStarted: typing.Union[MetaOapg.properties.lastScanManualStarted, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Posture':
        return super().__new__(
            cls,
            *_args,
            lastScanStatus=lastScanStatus,
            lastScanStatusDescription=lastScanStatusDescription,
            lastScanManualStarted=lastScanManualStarted,
            _configuration=_configuration,
        )