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


class AcknowledgeResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A response indicating the request has been processed by the server
    """

    class MetaOapg:
        required = {
            "acknowledged",
            "utcEpoch",
        }
        
        class properties:
            acknowledged = schemas.BoolSchema
            utcEpoch = schemas.Float64Schema
            __annotations__ = {
                "acknowledged": acknowledged,
                "utcEpoch": utcEpoch,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    acknowledged: MetaOapg.properties.acknowledged
    utcEpoch: MetaOapg.properties.utcEpoch
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acknowledged"]) -> MetaOapg.properties.acknowledged: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["utcEpoch"]) -> MetaOapg.properties.utcEpoch: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["acknowledged"], typing_extensions.Literal["utcEpoch"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acknowledged"]) -> MetaOapg.properties.acknowledged: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["utcEpoch"]) -> MetaOapg.properties.utcEpoch: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["acknowledged"], typing_extensions.Literal["utcEpoch"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        acknowledged: typing.Union[MetaOapg.properties.acknowledged, bool, ],
        utcEpoch: typing.Union[MetaOapg.properties.utcEpoch, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AcknowledgeResponse':
        return super().__new__(
            cls,
            *_args,
            acknowledged=acknowledged,
            utcEpoch=utcEpoch,
            _configuration=_configuration,
        )