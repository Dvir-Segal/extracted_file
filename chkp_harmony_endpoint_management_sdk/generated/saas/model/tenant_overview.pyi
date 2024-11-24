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


class TenantOverview(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "tenantId",
            "status",
        }
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['MSSPStatus']:
                return MSSPStatus
            tenantId = schemas.StrSchema
        
            @staticmethod
            def data() -> typing.Type['MsspDeploymentOverview']:
                return MsspDeploymentOverview
            error = schemas.StrSchema
            __annotations__ = {
                "status": status,
                "tenantId": tenantId,
                "data": data,
                "error": error,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    tenantId: MetaOapg.properties.tenantId
    status: 'MSSPStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'MSSPStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'MsspDeploymentOverview': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tenantId"], typing_extensions.Literal["status"], typing_extensions.Literal["data"], typing_extensions.Literal["error"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'MSSPStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['MsspDeploymentOverview', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tenantId"], typing_extensions.Literal["status"], typing_extensions.Literal["data"], typing_extensions.Literal["error"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tenantId: typing.Union[MetaOapg.properties.tenantId, str, ],
        status: 'MSSPStatus',
        data: typing.Union['MsspDeploymentOverview', schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TenantOverview':
        return super().__new__(
            cls,
            *_args,
            tenantId=tenantId,
            status=status,
            data=data,
            error=error,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.saas.model.mssp_deployment_overview import MsspDeploymentOverview
from chkp_harmony_endpoint_management_sdk.generated.saas.model.mssp_status import MSSPStatus
