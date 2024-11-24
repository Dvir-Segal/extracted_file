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


class PolicySettingsIUrlFilteringProtectionBladeAntiBot(
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
            def settings() -> typing.Type['IUrlFilteringProtection']:
                return IUrlFilteringProtection
        
            @staticmethod
            def metadata() -> typing.Type['PolicySettingsIUrlFilteringProtectionBladeAntiBotMetadata']:
                return PolicySettingsIUrlFilteringProtectionBladeAntiBotMetadata
            __annotations__ = {
                "settings": settings,
                "metadata": metadata,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    settings: 'IUrlFilteringProtection'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'IUrlFilteringProtection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'PolicySettingsIUrlFilteringProtectionBladeAntiBotMetadata': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["settings"], typing_extensions.Literal["metadata"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> 'IUrlFilteringProtection': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['PolicySettingsIUrlFilteringProtectionBladeAntiBotMetadata', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["settings"], typing_extensions.Literal["metadata"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        settings: 'IUrlFilteringProtection',
        metadata: typing.Union['PolicySettingsIUrlFilteringProtectionBladeAntiBotMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PolicySettingsIUrlFilteringProtectionBladeAntiBot':
        return super().__new__(
            cls,
            *_args,
            settings=settings,
            metadata=metadata,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_url_filtering_protection import IUrlFilteringProtection
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.policy_settings_i_url_filtering_protection_blade_anti_bot_metadata import PolicySettingsIUrlFilteringProtectionBladeAntiBotMetadata
