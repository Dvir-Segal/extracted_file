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


class IThreatPreventionProtections(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def network() -> typing.Type['IThreatPreventionProtectionsNetwork']:
                return IThreatPreventionProtectionsNetwork
        
            @staticmethod
            def system() -> typing.Type['IThreatPreventionProtectionsSystem']:
                return IThreatPreventionProtectionsSystem
            __annotations__ = {
                "network": network,
                "system": system,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> 'IThreatPreventionProtectionsNetwork': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["system"]) -> 'IThreatPreventionProtectionsSystem': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["network"], typing_extensions.Literal["system"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> typing.Union['IThreatPreventionProtectionsNetwork', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["system"]) -> typing.Union['IThreatPreventionProtectionsSystem', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["network"], typing_extensions.Literal["system"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        network: typing.Union['IThreatPreventionProtectionsNetwork', schemas.Unset] = schemas.unset,
        system: typing.Union['IThreatPreventionProtectionsSystem', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IThreatPreventionProtections':
        return super().__new__(
            cls,
            *_args,
            network=network,
            system=system,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_threat_prevention_protections_network import IThreatPreventionProtectionsNetwork
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_threat_prevention_protections_system import IThreatPreventionProtectionsSystem
