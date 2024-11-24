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


class PolicySettingsIPasswordReuseProtectionBladeThreatEmulation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "settings",
        }
        
        class properties:
        
            @staticmethod
            def settings() -> typing.Type['IPasswordReuseProtection']:
                return IPasswordReuseProtection
        
            @staticmethod
            def metadata() -> typing.Type['PolicySettingsIFilesProtectionBladeThreatEmulationMetadata']:
                return PolicySettingsIFilesProtectionBladeThreatEmulationMetadata
            __annotations__ = {
                "settings": settings,
                "metadata": metadata,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    settings: 'IPasswordReuseProtection'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'IPasswordReuseProtection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'PolicySettingsIFilesProtectionBladeThreatEmulationMetadata': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["settings"], typing_extensions.Literal["metadata"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> 'IPasswordReuseProtection': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['PolicySettingsIFilesProtectionBladeThreatEmulationMetadata', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["settings"], typing_extensions.Literal["metadata"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        settings: 'IPasswordReuseProtection',
        metadata: typing.Union['PolicySettingsIFilesProtectionBladeThreatEmulationMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PolicySettingsIPasswordReuseProtectionBladeThreatEmulation':
        return super().__new__(
            cls,
            *_args,
            settings=settings,
            metadata=metadata,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_password_reuse_protection import IPasswordReuseProtection
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.policy_settings_i_files_protection_blade_threat_emulation_metadata import PolicySettingsIFilesProtectionBladeThreatEmulationMetadata
