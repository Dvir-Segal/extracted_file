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


class LoginStatusResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    LoginStatusResponse objects return from login request.
    """

    class MetaOapg:
        required = {
            "role",
            "totalSuccess",
            "totalTenants",
            "sessionId",
            "tenantsLoginStatus",
        }
        
        class properties:
            sessionId = schemas.StrSchema
            totalTenants = schemas.Float64Schema
            totalSuccess = schemas.Float64Schema
            
            
            class tenantsLoginStatus(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                        class MetaOapg:
                            required = {
                                "tenantId",
                                "status",
                            }
                            
                            class properties:
                                
                                
                                class status(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                    
                                    @schemas.classproperty
                                    def OK(cls):
                                        return cls("OK")
                                    
                                    @schemas.classproperty
                                    def ERROR(cls):
                                        return cls("ERROR")
                                tenantId = schemas.StrSchema
                                __annotations__ = {
                                    "status": status,
                                    "tenantId": tenantId,
                                }
                        
                        tenantId: MetaOapg.properties.tenantId
                        status: MetaOapg.properties.status
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "tenantId", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "tenantId", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            tenantId: typing.Union[MetaOapg.properties.tenantId, str, ],
                            status: typing.Union[MetaOapg.properties.status, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                tenantId=tenantId,
                                status=status,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tenantsLoginStatus':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def role() -> typing.Type['SupportedLoginRole']:
                return SupportedLoginRole
            __annotations__ = {
                "sessionId": sessionId,
                "totalTenants": totalTenants,
                "totalSuccess": totalSuccess,
                "tenantsLoginStatus": tenantsLoginStatus,
                "role": role,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    role: 'SupportedLoginRole'
    totalSuccess: MetaOapg.properties.totalSuccess
    totalTenants: MetaOapg.properties.totalTenants
    sessionId: MetaOapg.properties.sessionId
    tenantsLoginStatus: MetaOapg.properties.tenantsLoginStatus
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> 'SupportedLoginRole': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalSuccess"]) -> MetaOapg.properties.totalSuccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalTenants"]) -> MetaOapg.properties.totalTenants: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessionId"]) -> MetaOapg.properties.sessionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantsLoginStatus"]) -> MetaOapg.properties.tenantsLoginStatus: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["role"], typing_extensions.Literal["totalSuccess"], typing_extensions.Literal["totalTenants"], typing_extensions.Literal["sessionId"], typing_extensions.Literal["tenantsLoginStatus"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> 'SupportedLoginRole': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalSuccess"]) -> MetaOapg.properties.totalSuccess: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalTenants"]) -> MetaOapg.properties.totalTenants: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessionId"]) -> MetaOapg.properties.sessionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantsLoginStatus"]) -> MetaOapg.properties.tenantsLoginStatus: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["role"], typing_extensions.Literal["totalSuccess"], typing_extensions.Literal["totalTenants"], typing_extensions.Literal["sessionId"], typing_extensions.Literal["tenantsLoginStatus"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        role: 'SupportedLoginRole',
        totalSuccess: typing.Union[MetaOapg.properties.totalSuccess, decimal.Decimal, int, float, ],
        totalTenants: typing.Union[MetaOapg.properties.totalTenants, decimal.Decimal, int, float, ],
        sessionId: typing.Union[MetaOapg.properties.sessionId, str, ],
        tenantsLoginStatus: typing.Union[MetaOapg.properties.tenantsLoginStatus, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LoginStatusResponse':
        return super().__new__(
            cls,
            *_args,
            role=role,
            totalSuccess=totalSuccess,
            totalTenants=totalTenants,
            sessionId=sessionId,
            tenantsLoginStatus=tenantsLoginStatus,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.saas.model.supported_login_role import SupportedLoginRole