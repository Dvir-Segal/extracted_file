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


class StandardTimestamp(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A timestamp
    """

    class MetaOapg:
        required = {
            "iso8601",
            "utcEpoch",
        }
        
        class properties:
            
            
            class utcEpoch(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    format = 'double'
                    inclusive_maximum = 9007199254740991
                    inclusive_minimum = 0
            iso8601 = schemas.DateTimeSchema
            __annotations__ = {
                "utcEpoch": utcEpoch,
                "iso8601": iso8601,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    iso8601: MetaOapg.properties.iso8601
    utcEpoch: MetaOapg.properties.utcEpoch
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso8601"]) -> MetaOapg.properties.iso8601: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["utcEpoch"]) -> MetaOapg.properties.utcEpoch: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["iso8601"], typing_extensions.Literal["utcEpoch"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso8601"]) -> MetaOapg.properties.iso8601: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["utcEpoch"]) -> MetaOapg.properties.utcEpoch: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["iso8601"], typing_extensions.Literal["utcEpoch"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        iso8601: typing.Union[MetaOapg.properties.iso8601, str, datetime, ],
        utcEpoch: typing.Union[MetaOapg.properties.utcEpoch, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'StandardTimestamp':
        return super().__new__(
            cls,
            *_args,
            iso8601=iso8601,
            utcEpoch=utcEpoch,
            _configuration=_configuration,
        )
