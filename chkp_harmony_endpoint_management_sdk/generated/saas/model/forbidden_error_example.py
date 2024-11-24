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


class ForbiddenErrorExample(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "instance",
            "detail",
            "source",
            "httpCode",
            "title",
            "type",
            "referenceId",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['ErrorTypesGenericForbidden']:
                return ErrorTypesGenericForbidden
            
            
            class title(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "You do not have permissions to perform the operation": "YOU_DO_NOT_HAVE_PERMISSIONS_TO_PERFORM_THE_OPERATION",
                    }
                
                @schemas.classproperty
                def YOU_DO_NOT_HAVE_PERMISSIONS_TO_PERFORM_THE_OPERATION(cls):
                    return cls("You do not have permissions to perform the operation")
            
            
            class detail(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class instance(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
        
            @staticmethod
            def source() -> typing.Type['ErrorSourceClient']:
                return ErrorSourceClient
            
            
            class httpCode(
                schemas.EnumBase,
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        403: "POSITIVE_403",
                    }
                
                @schemas.classproperty
                def POSITIVE_403(cls):
                    return cls(403)
            
            
            class referenceId(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "9f56db42-8005-42dc-85cc-3ee5df1d67dc": "F56DB42800542DC85CC3EE5DF1D67DC",
                    }
                
                @schemas.classproperty
                def F56DB42800542DC85CC3EE5DF1D67DC(cls):
                    return cls("9f56db42-8005-42dc-85cc-3ee5df1d67dc")
            extensions = schemas.DictSchema
            __annotations__ = {
                "type": type,
                "title": title,
                "detail": detail,
                "instance": instance,
                "source": source,
                "httpCode": httpCode,
                "referenceId": referenceId,
                "extensions": extensions,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    instance: MetaOapg.properties.instance
    detail: MetaOapg.properties.detail
    source: 'ErrorSourceClient'
    httpCode: MetaOapg.properties.httpCode
    title: MetaOapg.properties.title
    type: 'ErrorTypesGenericForbidden'
    referenceId: MetaOapg.properties.referenceId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instance"]) -> MetaOapg.properties.instance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'ErrorSourceClient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpCode"]) -> MetaOapg.properties.httpCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ErrorTypesGenericForbidden': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceId"]) -> MetaOapg.properties.referenceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extensions"]) -> MetaOapg.properties.extensions: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["instance"], typing_extensions.Literal["detail"], typing_extensions.Literal["source"], typing_extensions.Literal["httpCode"], typing_extensions.Literal["title"], typing_extensions.Literal["type"], typing_extensions.Literal["referenceId"], typing_extensions.Literal["extensions"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instance"]) -> MetaOapg.properties.instance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> 'ErrorSourceClient': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpCode"]) -> MetaOapg.properties.httpCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'ErrorTypesGenericForbidden': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceId"]) -> MetaOapg.properties.referenceId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extensions"]) -> typing.Union[MetaOapg.properties.extensions, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["instance"], typing_extensions.Literal["detail"], typing_extensions.Literal["source"], typing_extensions.Literal["httpCode"], typing_extensions.Literal["title"], typing_extensions.Literal["type"], typing_extensions.Literal["referenceId"], typing_extensions.Literal["extensions"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        instance: typing.Union[MetaOapg.properties.instance, str, ],
        detail: typing.Union[MetaOapg.properties.detail, str, ],
        source: 'ErrorSourceClient',
        httpCode: typing.Union[MetaOapg.properties.httpCode, decimal.Decimal, int, float, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        type: 'ErrorTypesGenericForbidden',
        referenceId: typing.Union[MetaOapg.properties.referenceId, str, ],
        extensions: typing.Union[MetaOapg.properties.extensions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ForbiddenErrorExample':
        return super().__new__(
            cls,
            *_args,
            instance=instance,
            detail=detail,
            source=source,
            httpCode=httpCode,
            title=title,
            type=type,
            referenceId=referenceId,
            extensions=extensions,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.saas.model.error_source_client import ErrorSourceClient
from chkp_harmony_endpoint_management_sdk.generated.saas.model.error_types_generic_forbidden import ErrorTypesGenericForbidden
