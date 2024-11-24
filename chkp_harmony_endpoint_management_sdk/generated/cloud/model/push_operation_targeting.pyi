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


class PushOperationTargeting(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Defines a Push Operation\'s targeting, i.e. what computers the operation would apply to
    """

    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def query() -> typing.Type['ComputersQuery']:
                return ComputersQuery
        
            @staticmethod
            def exclude() -> typing.Type['TargetingExclusions']:
                return TargetingExclusions
        
            @staticmethod
            def include() -> typing.Type['TargetingInclusions']:
                return TargetingInclusions
            __annotations__ = {
                "query": query,
                "exclude": exclude,
                "include": include,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> 'ComputersQuery': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude"]) -> 'TargetingExclusions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include"]) -> 'TargetingInclusions': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["query"], typing_extensions.Literal["exclude"], typing_extensions.Literal["include"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union['ComputersQuery', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude"]) -> typing.Union['TargetingExclusions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include"]) -> typing.Union['TargetingInclusions', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["query"], typing_extensions.Literal["exclude"], typing_extensions.Literal["include"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        query: typing.Union['ComputersQuery', schemas.Unset] = schemas.unset,
        exclude: typing.Union['TargetingExclusions', schemas.Unset] = schemas.unset,
        include: typing.Union['TargetingInclusions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PushOperationTargeting':
        return super().__new__(
            cls,
            *_args,
            query=query,
            exclude=exclude,
            include=include,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.computers_query import ComputersQuery
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.targeting_exclusions import TargetingExclusions
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.targeting_inclusions import TargetingInclusions