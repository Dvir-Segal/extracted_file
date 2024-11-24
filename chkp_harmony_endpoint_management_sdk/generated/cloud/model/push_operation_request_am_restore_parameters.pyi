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


class PushOperationRequestAmRestoreParameters(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "targets",
        }
        
        class properties:
        
            @staticmethod
            def targets() -> typing.Type['PushOperationTargeting']:
                return PushOperationTargeting
            comment = schemas.StrSchema
        
            @staticmethod
            def timing() -> typing.Type['PushOperationTiming']:
                return PushOperationTiming
        
            @staticmethod
            def operationParameters() -> typing.Type['AmRestoreParameters']:
                return AmRestoreParameters
            __annotations__ = {
                "targets": targets,
                "comment": comment,
                "timing": timing,
                "operationParameters": operationParameters,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    targets: 'PushOperationTargeting'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targets"]) -> 'PushOperationTargeting': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timing"]) -> 'PushOperationTiming': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operationParameters"]) -> 'AmRestoreParameters': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["targets"], typing_extensions.Literal["comment"], typing_extensions.Literal["timing"], typing_extensions.Literal["operationParameters"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targets"]) -> 'PushOperationTargeting': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timing"]) -> typing.Union['PushOperationTiming', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operationParameters"]) -> typing.Union['AmRestoreParameters', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["targets"], typing_extensions.Literal["comment"], typing_extensions.Literal["timing"], typing_extensions.Literal["operationParameters"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        targets: 'PushOperationTargeting',
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        timing: typing.Union['PushOperationTiming', schemas.Unset] = schemas.unset,
        operationParameters: typing.Union['AmRestoreParameters', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PushOperationRequestAmRestoreParameters':
        return super().__new__(
            cls,
            *_args,
            targets=targets,
            comment=comment,
            timing=timing,
            operationParameters=operationParameters,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.am_restore_parameters import AmRestoreParameters
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.push_operation_targeting import PushOperationTargeting
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.push_operation_timing import PushOperationTiming
