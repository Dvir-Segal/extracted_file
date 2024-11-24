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


class TenantsOverviewInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "tenantsAggregatedInfo",
            "tenantsInfo",
            "totalCount",
        }
        
        class properties:
            totalCount = schemas.Float64Schema
        
            @staticmethod
            def tenantsAggregatedInfo() -> typing.Type['MsspDeploymentOverview']:
                return MsspDeploymentOverview
            
            
            class tenantsInfo(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TenantOverview']:
                        return TenantOverview
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TenantOverview'], typing.List['TenantOverview']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tenantsInfo':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TenantOverview':
                    return super().__getitem__(i)
            __annotations__ = {
                "totalCount": totalCount,
                "tenantsAggregatedInfo": tenantsAggregatedInfo,
                "tenantsInfo": tenantsInfo,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    tenantsAggregatedInfo: 'MsspDeploymentOverview'
    tenantsInfo: MetaOapg.properties.tenantsInfo
    totalCount: MetaOapg.properties.totalCount
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantsAggregatedInfo"]) -> 'MsspDeploymentOverview': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantsInfo"]) -> MetaOapg.properties.tenantsInfo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tenantsAggregatedInfo"], typing_extensions.Literal["tenantsInfo"], typing_extensions.Literal["totalCount"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantsAggregatedInfo"]) -> 'MsspDeploymentOverview': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantsInfo"]) -> MetaOapg.properties.tenantsInfo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tenantsAggregatedInfo"], typing_extensions.Literal["tenantsInfo"], typing_extensions.Literal["totalCount"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tenantsAggregatedInfo: 'MsspDeploymentOverview',
        tenantsInfo: typing.Union[MetaOapg.properties.tenantsInfo, list, tuple, ],
        totalCount: typing.Union[MetaOapg.properties.totalCount, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TenantsOverviewInfo':
        return super().__new__(
            cls,
            *_args,
            tenantsAggregatedInfo=tenantsAggregatedInfo,
            tenantsInfo=tenantsInfo,
            totalCount=totalCount,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.saas.model.mssp_deployment_overview import MsspDeploymentOverview
from chkp_harmony_endpoint_management_sdk.generated.saas.model.tenant_overview import TenantOverview