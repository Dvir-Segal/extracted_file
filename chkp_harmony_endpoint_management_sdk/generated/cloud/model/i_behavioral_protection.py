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


class IBehavioralProtection(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
            enabled = schemas.BoolSchema
            enableNetworkShareProtection = schemas.BoolSchema
            enableLowMemoryMode = schemas.BoolSchema
        
            @staticmethod
            def antiRansomware() -> typing.Type['IBehavioralProtectionAntiRansomware']:
                return IBehavioralProtectionAntiRansomware
        
            @staticmethod
            def backup() -> typing.Type['IBehavioralProtectionBackup']:
                return IBehavioralProtectionBackup
        
            @staticmethod
            def restoration() -> typing.Type['BehavioralGuardRestoration']:
                return BehavioralGuardRestoration
        
            @staticmethod
            def forensics() -> typing.Type['IBehavioralProtectionForensics']:
                return IBehavioralProtectionForensics
        
            @staticmethod
            def edr() -> typing.Type['IBehavioralProtectionEdr']:
                return IBehavioralProtectionEdr
            __annotations__ = {
                "enabled": enabled,
                "enableNetworkShareProtection": enableNetworkShareProtection,
                "enableLowMemoryMode": enableLowMemoryMode,
                "antiRansomware": antiRansomware,
                "backup": backup,
                "restoration": restoration,
                "forensics": forensics,
                "edr": edr,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableNetworkShareProtection"]) -> MetaOapg.properties.enableNetworkShareProtection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableLowMemoryMode"]) -> MetaOapg.properties.enableLowMemoryMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["antiRansomware"]) -> 'IBehavioralProtectionAntiRansomware': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backup"]) -> 'IBehavioralProtectionBackup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restoration"]) -> 'BehavioralGuardRestoration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forensics"]) -> 'IBehavioralProtectionForensics': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edr"]) -> 'IBehavioralProtectionEdr': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enabled"], typing_extensions.Literal["enableNetworkShareProtection"], typing_extensions.Literal["enableLowMemoryMode"], typing_extensions.Literal["antiRansomware"], typing_extensions.Literal["backup"], typing_extensions.Literal["restoration"], typing_extensions.Literal["forensics"], typing_extensions.Literal["edr"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableNetworkShareProtection"]) -> typing.Union[MetaOapg.properties.enableNetworkShareProtection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableLowMemoryMode"]) -> typing.Union[MetaOapg.properties.enableLowMemoryMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["antiRansomware"]) -> typing.Union['IBehavioralProtectionAntiRansomware', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backup"]) -> typing.Union['IBehavioralProtectionBackup', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restoration"]) -> typing.Union['BehavioralGuardRestoration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forensics"]) -> typing.Union['IBehavioralProtectionForensics', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edr"]) -> typing.Union['IBehavioralProtectionEdr', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enabled"], typing_extensions.Literal["enableNetworkShareProtection"], typing_extensions.Literal["enableLowMemoryMode"], typing_extensions.Literal["antiRansomware"], typing_extensions.Literal["backup"], typing_extensions.Literal["restoration"], typing_extensions.Literal["forensics"], typing_extensions.Literal["edr"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
        enableNetworkShareProtection: typing.Union[MetaOapg.properties.enableNetworkShareProtection, bool, schemas.Unset] = schemas.unset,
        enableLowMemoryMode: typing.Union[MetaOapg.properties.enableLowMemoryMode, bool, schemas.Unset] = schemas.unset,
        antiRansomware: typing.Union['IBehavioralProtectionAntiRansomware', schemas.Unset] = schemas.unset,
        backup: typing.Union['IBehavioralProtectionBackup', schemas.Unset] = schemas.unset,
        restoration: typing.Union['BehavioralGuardRestoration', schemas.Unset] = schemas.unset,
        forensics: typing.Union['IBehavioralProtectionForensics', schemas.Unset] = schemas.unset,
        edr: typing.Union['IBehavioralProtectionEdr', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IBehavioralProtection':
        return super().__new__(
            cls,
            *_args,
            enabled=enabled,
            enableNetworkShareProtection=enableNetworkShareProtection,
            enableLowMemoryMode=enableLowMemoryMode,
            antiRansomware=antiRansomware,
            backup=backup,
            restoration=restoration,
            forensics=forensics,
            edr=edr,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.behavioral_guard_restoration import BehavioralGuardRestoration
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_behavioral_protection_anti_ransomware import IBehavioralProtectionAntiRansomware
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_behavioral_protection_backup import IBehavioralProtectionBackup
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_behavioral_protection_edr import IBehavioralProtectionEdr
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_behavioral_protection_forensics import IBehavioralProtectionForensics
