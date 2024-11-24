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


class RemoveRegistryKeyParams(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "hive",
            "key",
        }
        
        class properties:
        
            @staticmethod
            def hive() -> typing.Type['RegistryHive']:
                return RegistryHive
            key = schemas.StrSchema
            informUser = schemas.BoolSchema
            allowPostpone = schemas.BoolSchema
            valueName = schemas.StrSchema
            isRedirected = schemas.BoolSchema
            __annotations__ = {
                "hive": hive,
                "key": key,
                "informUser": informUser,
                "allowPostpone": allowPostpone,
                "valueName": valueName,
                "isRedirected": isRedirected,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    hive: 'RegistryHive'
    key: MetaOapg.properties.key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hive"]) -> 'RegistryHive': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["informUser"]) -> MetaOapg.properties.informUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowPostpone"]) -> MetaOapg.properties.allowPostpone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["valueName"]) -> MetaOapg.properties.valueName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isRedirected"]) -> MetaOapg.properties.isRedirected: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hive"], typing_extensions.Literal["key"], typing_extensions.Literal["informUser"], typing_extensions.Literal["allowPostpone"], typing_extensions.Literal["valueName"], typing_extensions.Literal["isRedirected"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hive"]) -> 'RegistryHive': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["informUser"]) -> typing.Union[MetaOapg.properties.informUser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowPostpone"]) -> typing.Union[MetaOapg.properties.allowPostpone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["valueName"]) -> typing.Union[MetaOapg.properties.valueName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isRedirected"]) -> typing.Union[MetaOapg.properties.isRedirected, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hive"], typing_extensions.Literal["key"], typing_extensions.Literal["informUser"], typing_extensions.Literal["allowPostpone"], typing_extensions.Literal["valueName"], typing_extensions.Literal["isRedirected"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        hive: 'RegistryHive',
        key: typing.Union[MetaOapg.properties.key, str, ],
        informUser: typing.Union[MetaOapg.properties.informUser, bool, schemas.Unset] = schemas.unset,
        allowPostpone: typing.Union[MetaOapg.properties.allowPostpone, bool, schemas.Unset] = schemas.unset,
        valueName: typing.Union[MetaOapg.properties.valueName, str, schemas.Unset] = schemas.unset,
        isRedirected: typing.Union[MetaOapg.properties.isRedirected, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'RemoveRegistryKeyParams':
        return super().__new__(
            cls,
            *_args,
            hive=hive,
            key=key,
            informUser=informUser,
            allowPostpone=allowPostpone,
            valueName=valueName,
            isRedirected=isRedirected,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.registry_hive import RegistryHive