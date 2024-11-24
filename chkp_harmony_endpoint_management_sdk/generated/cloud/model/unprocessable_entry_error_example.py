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


class UnprocessableEntryErrorExample(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "extensions",
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
            def type() -> typing.Type['ErrorTypesTsoaInputValidation']:
                return ErrorTypesTsoaInputValidation
            
            
            class title(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "The request does not conform to the API schema": "THE_REQUEST_DOES_NOT_CONFORM_TO_THE_API_SCHEMA",
                    }
                
                @schemas.classproperty
                def THE_REQUEST_DOES_NOT_CONFORM_TO_THE_API_SCHEMA(cls):
                    return cls("The request does not conform to the API schema")
            
            
            class detail(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "The request was understood but did not conform to API schema. Further information is available under the 'extensions' object in the reply": "THE_REQUEST_WAS_UNDERSTOOD_BUT_DID_NOT_CONFORM_TO_API_SCHEMA__FURTHER_INFORMATION_IS_AVAILABLE_UNDER_THE_EXTENSIONS_OBJECT_IN_THE_REPLY",
                    }
                
                @schemas.classproperty
                def THE_REQUEST_WAS_UNDERSTOOD_BUT_DID_NOT_CONFORM_TO_API_SCHEMA__FURTHER_INFORMATION_IS_AVAILABLE_UNDER_THE_EXTENSIONS_OBJECT_IN_THE_REPLY(cls):
                    return cls("The request was understood but did not conform to API schema. Further information is available under the 'extensions' object in the reply")
            
            
            class instance(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "base/server/validation/ValidateError": "BASE_SERVER_VALIDATION_VALIDATE_ERROR",
                    }
                
                @schemas.classproperty
                def BASE_SERVER_VALIDATION_VALIDATE_ERROR(cls):
                    return cls("base/server/validation/ValidateError")
        
            @staticmethod
            def source() -> typing.Type['ErrorSourceClient']:
                return ErrorSourceClient
            
            
            class httpCode(
                schemas.EnumBase,
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        422: "POSITIVE_422",
                    }
                
                @schemas.classproperty
                def POSITIVE_422(cls):
                    return cls(422)
            
            
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
            
            
            class extensions(
                schemas.DictSchema
            ):
            
                class MetaOapg:
                    required = {
                        "fields",
                    }
                    
                    class properties:
                        
                        
                        class fields(
                            schemas.DictSchema
                        ):
                        
                            class MetaOapg:
                                required = {
                                    "fieldName",
                                }
                                
                                class properties:
                                    
                                    
                                    class fieldName(
                                        schemas.DictSchema
                                    ):
                                    
                                        class MetaOapg:
                                            required = {
                                                "message",
                                                "value",
                                            }
                                            
                                            class properties:
                                                
                                                
                                                class value(
                                                    schemas.EnumBase,
                                                    schemas.StrSchema
                                                ):
                                                
                                                
                                                    class MetaOapg:
                                                        enum_value_to_name = {
                                                            "B": "B",
                                                        }
                                                    
                                                    @schemas.classproperty
                                                    def B(cls):
                                                        return cls("B")
                                                
                                                
                                                class message(
                                                    schemas.EnumBase,
                                                    schemas.StrSchema
                                                ):
                                                
                                                
                                                    class MetaOapg:
                                                        enum_value_to_name = {
                                                            "Expected A but got B": "EXPECTED_A_BUT_GOT_B",
                                                        }
                                                    
                                                    @schemas.classproperty
                                                    def EXPECTED_A_BUT_GOT_B(cls):
                                                        return cls("Expected A but got B")
                                                __annotations__ = {
                                                    "value": value,
                                                    "message": message,
                                                }
                                        
                                        message: MetaOapg.properties.message
                                        value: MetaOapg.properties.value
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                        
                                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["value", "message", ], str]):
                                            # dict_instance[name] accessor
                                            return super().__getitem__(name)
                                        
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                        
                                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["value", "message", ], str]):
                                            return super().get_item_oapg(name)
                                        
                                    
                                        def __new__(
                                            cls,
                                            *_args: typing.Union[dict, frozendict.frozendict, ],
                                            message: typing.Union[MetaOapg.properties.message, str, ],
                                            value: typing.Union[MetaOapg.properties.value, str, ],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                        ) -> 'fieldName':
                                            return super().__new__(
                                                cls,
                                                *_args,
                                                message=message,
                                                value=value,
                                                _configuration=_configuration,
                                                **kwargs,
                                            )
                                    __annotations__ = {
                                        "fieldName": fieldName,
                                    }
                            
                            fieldName: MetaOapg.properties.fieldName
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["fieldName"]) -> MetaOapg.properties.fieldName: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["fieldName", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["fieldName"]) -> MetaOapg.properties.fieldName: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fieldName", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                fieldName: typing.Union[MetaOapg.properties.fieldName, dict, frozendict.frozendict, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'fields':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    fieldName=fieldName,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "fields": fields,
                        }
                
                fields: MetaOapg.properties.fields
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["fields"]) -> MetaOapg.properties.fields: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["fields", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> MetaOapg.properties.fields: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fields", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    fields: typing.Union[MetaOapg.properties.fields, dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'extensions':
                    return super().__new__(
                        cls,
                        *_args,
                        fields=fields,
                        _configuration=_configuration,
                        **kwargs,
                    )
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
    
    extensions: MetaOapg.properties.extensions
    instance: MetaOapg.properties.instance
    detail: MetaOapg.properties.detail
    source: 'ErrorSourceClient'
    httpCode: MetaOapg.properties.httpCode
    title: MetaOapg.properties.title
    type: 'ErrorTypesTsoaInputValidation'
    referenceId: MetaOapg.properties.referenceId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extensions"]) -> MetaOapg.properties.extensions: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ErrorTypesTsoaInputValidation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceId"]) -> MetaOapg.properties.referenceId: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["extensions"], typing_extensions.Literal["instance"], typing_extensions.Literal["detail"], typing_extensions.Literal["source"], typing_extensions.Literal["httpCode"], typing_extensions.Literal["title"], typing_extensions.Literal["type"], typing_extensions.Literal["referenceId"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extensions"]) -> MetaOapg.properties.extensions: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'ErrorTypesTsoaInputValidation': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceId"]) -> MetaOapg.properties.referenceId: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["extensions"], typing_extensions.Literal["instance"], typing_extensions.Literal["detail"], typing_extensions.Literal["source"], typing_extensions.Literal["httpCode"], typing_extensions.Literal["title"], typing_extensions.Literal["type"], typing_extensions.Literal["referenceId"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        extensions: typing.Union[MetaOapg.properties.extensions, dict, frozendict.frozendict, ],
        instance: typing.Union[MetaOapg.properties.instance, str, ],
        detail: typing.Union[MetaOapg.properties.detail, str, ],
        source: 'ErrorSourceClient',
        httpCode: typing.Union[MetaOapg.properties.httpCode, decimal.Decimal, int, float, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        type: 'ErrorTypesTsoaInputValidation',
        referenceId: typing.Union[MetaOapg.properties.referenceId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UnprocessableEntryErrorExample':
        return super().__new__(
            cls,
            *_args,
            extensions=extensions,
            instance=instance,
            detail=detail,
            source=source,
            httpCode=httpCode,
            title=title,
            type=type,
            referenceId=referenceId,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.error_source_client import ErrorSourceClient
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.error_types_tsoa_input_validation import ErrorTypesTsoaInputValidation
