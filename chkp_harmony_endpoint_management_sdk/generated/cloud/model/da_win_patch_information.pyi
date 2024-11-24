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


class DaWinPatchInformation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
            winPatchVersion = schemas.StrSchema
            winPatchDescription = schemas.StrSchema
            __annotations__ = {
                "winPatchVersion": winPatchVersion,
                "winPatchDescription": winPatchDescription,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["winPatchVersion"]) -> MetaOapg.properties.winPatchVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["winPatchDescription"]) -> MetaOapg.properties.winPatchDescription: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["winPatchVersion"], typing_extensions.Literal["winPatchDescription"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["winPatchVersion"]) -> typing.Union[MetaOapg.properties.winPatchVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["winPatchDescription"]) -> typing.Union[MetaOapg.properties.winPatchDescription, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["winPatchVersion"], typing_extensions.Literal["winPatchDescription"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        winPatchVersion: typing.Union[MetaOapg.properties.winPatchVersion, str, schemas.Unset] = schemas.unset,
        winPatchDescription: typing.Union[MetaOapg.properties.winPatchDescription, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DaWinPatchInformation':
        return super().__new__(
            cls,
            *_args,
            winPatchVersion=winPatchVersion,
            winPatchDescription=winPatchDescription,
            _configuration=_configuration,
        )
