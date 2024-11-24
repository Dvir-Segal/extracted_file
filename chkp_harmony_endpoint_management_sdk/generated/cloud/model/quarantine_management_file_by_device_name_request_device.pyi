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


class QuarantineManagementFileByDeviceNameRequestDevice(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
            commonName = schemas.StrSchema
            domainName = schemas.StrSchema
            id = schemas.StrSchema
            __annotations__ = {
                "commonName": commonName,
                "domainName": domainName,
                "id": id,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commonName"]) -> MetaOapg.properties.commonName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domainName"]) -> MetaOapg.properties.domainName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["commonName"], typing_extensions.Literal["domainName"], typing_extensions.Literal["id"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commonName"]) -> typing.Union[MetaOapg.properties.commonName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domainName"]) -> typing.Union[MetaOapg.properties.domainName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["commonName"], typing_extensions.Literal["domainName"], typing_extensions.Literal["id"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        commonName: typing.Union[MetaOapg.properties.commonName, str, schemas.Unset] = schemas.unset,
        domainName: typing.Union[MetaOapg.properties.domainName, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'QuarantineManagementFileByDeviceNameRequestDevice':
        return super().__new__(
            cls,
            *_args,
            commonName=commonName,
            domainName=domainName,
            id=id,
            _configuration=_configuration,
        )
