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


class AntiBot(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
            abLastUpdate = schemas.StrSchema
            __annotations__ = {
                "abLastUpdate": abLastUpdate,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["abLastUpdate"]) -> MetaOapg.properties.abLastUpdate: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["abLastUpdate"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["abLastUpdate"]) -> typing.Union[MetaOapg.properties.abLastUpdate, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["abLastUpdate"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        abLastUpdate: typing.Union[MetaOapg.properties.abLastUpdate, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AntiBot':
        return super().__new__(
            cls,
            *_args,
            abLastUpdate=abLastUpdate,
            _configuration=_configuration,
        )