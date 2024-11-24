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


class ApplianceEmulationEnvironment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "fallbackToCloud",
            "appliances",
        }
        
        class properties:
            fallbackToCloud = schemas.BoolSchema
            
            
            class appliances(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ThreatEmulationAppliance']:
                        return ThreatEmulationAppliance
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ThreatEmulationAppliance'], typing.List['ThreatEmulationAppliance']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'appliances':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ThreatEmulationAppliance':
                    return super().__getitem__(i)
            __annotations__ = {
                "fallbackToCloud": fallbackToCloud,
                "appliances": appliances,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    fallbackToCloud: MetaOapg.properties.fallbackToCloud
    appliances: MetaOapg.properties.appliances
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fallbackToCloud"]) -> MetaOapg.properties.fallbackToCloud: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appliances"]) -> MetaOapg.properties.appliances: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fallbackToCloud"], typing_extensions.Literal["appliances"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fallbackToCloud"]) -> MetaOapg.properties.fallbackToCloud: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appliances"]) -> MetaOapg.properties.appliances: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fallbackToCloud"], typing_extensions.Literal["appliances"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        fallbackToCloud: typing.Union[MetaOapg.properties.fallbackToCloud, bool, ],
        appliances: typing.Union[MetaOapg.properties.appliances, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ApplianceEmulationEnvironment':
        return super().__new__(
            cls,
            *_args,
            fallbackToCloud=fallbackToCloud,
            appliances=appliances,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.threat_emulation_appliance import ThreatEmulationAppliance
