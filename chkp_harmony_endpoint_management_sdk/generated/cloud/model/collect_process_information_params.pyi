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


class CollectProcessInformationParams(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
            informUser = schemas.BoolSchema
            allowPostpone = schemas.BoolSchema
            processName = schemas.StrSchema
            
            
            class additionalFields(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['ProcessProperties']:
                                return ProcessProperties
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['ProcessProperties'], typing.List['ProcessProperties']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_0':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ProcessProperties':
                            return super().__getitem__(i)
                    
                    
                    class any_of_1(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_1':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'additionalFields':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "informUser": informUser,
                "allowPostpone": allowPostpone,
                "processName": processName,
                "additionalFields": additionalFields,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["informUser"]) -> MetaOapg.properties.informUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowPostpone"]) -> MetaOapg.properties.allowPostpone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processName"]) -> MetaOapg.properties.processName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalFields"]) -> MetaOapg.properties.additionalFields: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["informUser"], typing_extensions.Literal["allowPostpone"], typing_extensions.Literal["processName"], typing_extensions.Literal["additionalFields"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["informUser"]) -> typing.Union[MetaOapg.properties.informUser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowPostpone"]) -> typing.Union[MetaOapg.properties.allowPostpone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processName"]) -> typing.Union[MetaOapg.properties.processName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionalFields"]) -> typing.Union[MetaOapg.properties.additionalFields, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["informUser"], typing_extensions.Literal["allowPostpone"], typing_extensions.Literal["processName"], typing_extensions.Literal["additionalFields"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        informUser: typing.Union[MetaOapg.properties.informUser, bool, schemas.Unset] = schemas.unset,
        allowPostpone: typing.Union[MetaOapg.properties.allowPostpone, bool, schemas.Unset] = schemas.unset,
        processName: typing.Union[MetaOapg.properties.processName, str, schemas.Unset] = schemas.unset,
        additionalFields: typing.Union[MetaOapg.properties.additionalFields, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CollectProcessInformationParams':
        return super().__new__(
            cls,
            *_args,
            informUser=informUser,
            allowPostpone=allowPostpone,
            processName=processName,
            additionalFields=additionalFields,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.process_properties import ProcessProperties