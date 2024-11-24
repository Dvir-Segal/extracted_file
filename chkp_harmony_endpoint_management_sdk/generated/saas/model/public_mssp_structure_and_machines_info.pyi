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


class PublicMsspStructureAndMachinesInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "tenantName",
            "tenantId",
            "machines",
            "type",
            "childTenants",
        }
        
        class properties:
            tenantId = schemas.StrSchema
            tenantName = schemas.StrSchema
        
            @staticmethod
            def type() -> typing.Type['TenantType']:
                return TenantType
            
            
            class machines(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PublicServiceInfoLight']:
                        return PublicServiceInfoLight
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['PublicServiceInfoLight'], typing.List['PublicServiceInfoLight']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'machines':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PublicServiceInfoLight':
                    return super().__getitem__(i)
            
            
            class childTenants(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                        class MetaOapg:
                            required = {
                                "tenantName",
                                "tenantId",
                                "machines",
                                "type",
                            }
                            
                            class properties:
                                
                                
                                class machines(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['PublicServiceInfoLight']:
                                            return PublicServiceInfoLight
                                
                                    def __new__(
                                        cls,
                                        _arg: typing.Union[typing.Tuple['PublicServiceInfoLight'], typing.List['PublicServiceInfoLight']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'machines':
                                        return super().__new__(
                                            cls,
                                            _arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'PublicServiceInfoLight':
                                        return super().__getitem__(i)
                            
                                @staticmethod
                                def type() -> typing.Type['TenantType']:
                                    return TenantType
                                tenantName = schemas.StrSchema
                                tenantId = schemas.StrSchema
                                __annotations__ = {
                                    "machines": machines,
                                    "type": type,
                                    "tenantName": tenantName,
                                    "tenantId": tenantId,
                                }
                        
                        tenantName: MetaOapg.properties.tenantName
                        tenantId: MetaOapg.properties.tenantId
                        machines: MetaOapg.properties.machines
                        type: 'TenantType'
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["machines"]) -> MetaOapg.properties.machines: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'TenantType': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["tenantName"]) -> MetaOapg.properties.tenantName: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["machines", "type", "tenantName", "tenantId", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["machines"]) -> MetaOapg.properties.machines: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'TenantType': ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["tenantName"]) -> MetaOapg.properties.tenantName: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["machines", "type", "tenantName", "tenantId", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            tenantName: typing.Union[MetaOapg.properties.tenantName, str, ],
                            tenantId: typing.Union[MetaOapg.properties.tenantId, str, ],
                            machines: typing.Union[MetaOapg.properties.machines, list, tuple, ],
                            type: 'TenantType',
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                tenantName=tenantName,
                                tenantId=tenantId,
                                machines=machines,
                                type=type,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'childTenants':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "tenantId": tenantId,
                "tenantName": tenantName,
                "type": type,
                "machines": machines,
                "childTenants": childTenants,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    tenantName: MetaOapg.properties.tenantName
    tenantId: MetaOapg.properties.tenantId
    machines: MetaOapg.properties.machines
    type: 'TenantType'
    childTenants: MetaOapg.properties.childTenants
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantName"]) -> MetaOapg.properties.tenantName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["machines"]) -> MetaOapg.properties.machines: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'TenantType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["childTenants"]) -> MetaOapg.properties.childTenants: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tenantName"], typing_extensions.Literal["tenantId"], typing_extensions.Literal["machines"], typing_extensions.Literal["type"], typing_extensions.Literal["childTenants"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantName"]) -> MetaOapg.properties.tenantName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["machines"]) -> MetaOapg.properties.machines: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'TenantType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["childTenants"]) -> MetaOapg.properties.childTenants: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tenantName"], typing_extensions.Literal["tenantId"], typing_extensions.Literal["machines"], typing_extensions.Literal["type"], typing_extensions.Literal["childTenants"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tenantName: typing.Union[MetaOapg.properties.tenantName, str, ],
        tenantId: typing.Union[MetaOapg.properties.tenantId, str, ],
        machines: typing.Union[MetaOapg.properties.machines, list, tuple, ],
        type: 'TenantType',
        childTenants: typing.Union[MetaOapg.properties.childTenants, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PublicMsspStructureAndMachinesInfo':
        return super().__new__(
            cls,
            *_args,
            tenantName=tenantName,
            tenantId=tenantId,
            machines=machines,
            type=type,
            childTenants=childTenants,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.saas.model.public_service_info_light import PublicServiceInfoLight
from chkp_harmony_endpoint_management_sdk.generated.saas.model.tenant_type import TenantType