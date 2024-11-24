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


class ComputersByFilterPaging(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "offset",
            "pageSize",
        }
        
        class properties:
            
            
            class pageSize(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 50
                    inclusive_minimum = 1
            
            
            class offset(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = 0
            __annotations__ = {
                "pageSize": pageSize,
                "offset": offset,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    offset: MetaOapg.properties.offset
    pageSize: MetaOapg.properties.pageSize
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageSize"]) -> MetaOapg.properties.pageSize: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["offset"], typing_extensions.Literal["pageSize"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageSize"]) -> MetaOapg.properties.pageSize: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["offset"], typing_extensions.Literal["pageSize"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        offset: typing.Union[MetaOapg.properties.offset, decimal.Decimal, int, ],
        pageSize: typing.Union[MetaOapg.properties.pageSize, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ComputersByFilterPaging':
        return super().__new__(
            cls,
            *_args,
            offset=offset,
            pageSize=pageSize,
            _configuration=_configuration,
        )
