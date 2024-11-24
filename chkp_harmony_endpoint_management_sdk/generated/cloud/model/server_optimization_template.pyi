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


class ServerOptimizationTemplate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "templateName",
            "templateHash",
            "templateDescription",
            "templateId",
        }
        
        class properties:
            templateId = schemas.StrSchema
            templateName = schemas.StrSchema
            templateDescription = schemas.StrSchema
            templateHash = schemas.StrSchema
            __annotations__ = {
                "templateId": templateId,
                "templateName": templateName,
                "templateDescription": templateDescription,
                "templateHash": templateHash,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    templateName: MetaOapg.properties.templateName
    templateHash: MetaOapg.properties.templateHash
    templateDescription: MetaOapg.properties.templateDescription
    templateId: MetaOapg.properties.templateId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateName"]) -> MetaOapg.properties.templateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateHash"]) -> MetaOapg.properties.templateHash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateDescription"]) -> MetaOapg.properties.templateDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["templateName"], typing_extensions.Literal["templateHash"], typing_extensions.Literal["templateDescription"], typing_extensions.Literal["templateId"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateName"]) -> MetaOapg.properties.templateName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateHash"]) -> MetaOapg.properties.templateHash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateDescription"]) -> MetaOapg.properties.templateDescription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["templateName"], typing_extensions.Literal["templateHash"], typing_extensions.Literal["templateDescription"], typing_extensions.Literal["templateId"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        templateName: typing.Union[MetaOapg.properties.templateName, str, ],
        templateHash: typing.Union[MetaOapg.properties.templateHash, str, ],
        templateDescription: typing.Union[MetaOapg.properties.templateDescription, str, ],
        templateId: typing.Union[MetaOapg.properties.templateId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ServerOptimizationTemplate':
        return super().__new__(
            cls,
            *_args,
            templateName=templateName,
            templateHash=templateHash,
            templateDescription=templateDescription,
            templateId=templateId,
            _configuration=_configuration,
        )