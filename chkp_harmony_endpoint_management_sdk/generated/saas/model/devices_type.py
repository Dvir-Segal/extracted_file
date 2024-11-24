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


class DevicesType(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "devicesType",
            "totalCount",
        }
        
        class properties:
            
            
            class devicesType(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['KeyNumericValuePair']:
                        return KeyNumericValuePair
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['KeyNumericValuePair'], typing.List['KeyNumericValuePair']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'devicesType':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'KeyNumericValuePair':
                    return super().__getitem__(i)
            totalCount = schemas.Float64Schema
            __annotations__ = {
                "devicesType": devicesType,
                "totalCount": totalCount,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    devicesType: MetaOapg.properties.devicesType
    totalCount: MetaOapg.properties.totalCount
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["devicesType"]) -> MetaOapg.properties.devicesType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["devicesType"], typing_extensions.Literal["totalCount"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["devicesType"]) -> MetaOapg.properties.devicesType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["devicesType"], typing_extensions.Literal["totalCount"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        devicesType: typing.Union[MetaOapg.properties.devicesType, list, tuple, ],
        totalCount: typing.Union[MetaOapg.properties.totalCount, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DevicesType':
        return super().__new__(
            cls,
            *_args,
            devicesType=devicesType,
            totalCount=totalCount,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.saas.model.key_numeric_value_pair import KeyNumericValuePair
