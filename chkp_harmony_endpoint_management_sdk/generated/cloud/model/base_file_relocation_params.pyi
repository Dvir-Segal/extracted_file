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


class BaseFileRelocationParams(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "destinationAbsolutePath",
            "sourceAbsolutePath",
        }
        
        class properties:
            
            
            class sourceAbsolutePath(
                schemas.StrSchema
            ):
                pass
            
            
            class destinationAbsolutePath(
                schemas.StrSchema
            ):
                pass
            informUser = schemas.BoolSchema
            allowPostpone = schemas.BoolSchema
            __annotations__ = {
                "sourceAbsolutePath": sourceAbsolutePath,
                "destinationAbsolutePath": destinationAbsolutePath,
                "informUser": informUser,
                "allowPostpone": allowPostpone,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    destinationAbsolutePath: MetaOapg.properties.destinationAbsolutePath
    sourceAbsolutePath: MetaOapg.properties.sourceAbsolutePath
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationAbsolutePath"]) -> MetaOapg.properties.destinationAbsolutePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceAbsolutePath"]) -> MetaOapg.properties.sourceAbsolutePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["informUser"]) -> MetaOapg.properties.informUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowPostpone"]) -> MetaOapg.properties.allowPostpone: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["destinationAbsolutePath"], typing_extensions.Literal["sourceAbsolutePath"], typing_extensions.Literal["informUser"], typing_extensions.Literal["allowPostpone"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationAbsolutePath"]) -> MetaOapg.properties.destinationAbsolutePath: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceAbsolutePath"]) -> MetaOapg.properties.sourceAbsolutePath: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["informUser"]) -> typing.Union[MetaOapg.properties.informUser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowPostpone"]) -> typing.Union[MetaOapg.properties.allowPostpone, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["destinationAbsolutePath"], typing_extensions.Literal["sourceAbsolutePath"], typing_extensions.Literal["informUser"], typing_extensions.Literal["allowPostpone"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        destinationAbsolutePath: typing.Union[MetaOapg.properties.destinationAbsolutePath, str, ],
        sourceAbsolutePath: typing.Union[MetaOapg.properties.sourceAbsolutePath, str, ],
        informUser: typing.Union[MetaOapg.properties.informUser, bool, schemas.Unset] = schemas.unset,
        allowPostpone: typing.Union[MetaOapg.properties.allowPostpone, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BaseFileRelocationParams':
        return super().__new__(
            cls,
            *_args,
            destinationAbsolutePath=destinationAbsolutePath,
            sourceAbsolutePath=sourceAbsolutePath,
            informUser=informUser,
            allowPostpone=allowPostpone,
            _configuration=_configuration,
        )
