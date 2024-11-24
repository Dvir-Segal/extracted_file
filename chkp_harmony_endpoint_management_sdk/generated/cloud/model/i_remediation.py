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


class IRemediation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def mode() -> typing.Type['RemediationMode']:
                return RemediationMode
        
            @staticmethod
            def quarantine() -> typing.Type['IRemediationQuarantine']:
                return IRemediationQuarantine
        
            @staticmethod
            def file() -> typing.Type['IRemediationFile']:
                return IRemediationFile
            __annotations__ = {
                "mode": mode,
                "quarantine": quarantine,
                "file": file,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> 'RemediationMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quarantine"]) -> 'IRemediationQuarantine': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> 'IRemediationFile': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["mode"], typing_extensions.Literal["quarantine"], typing_extensions.Literal["file"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> typing.Union['RemediationMode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quarantine"]) -> typing.Union['IRemediationQuarantine', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> typing.Union['IRemediationFile', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mode"], typing_extensions.Literal["quarantine"], typing_extensions.Literal["file"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        mode: typing.Union['RemediationMode', schemas.Unset] = schemas.unset,
        quarantine: typing.Union['IRemediationQuarantine', schemas.Unset] = schemas.unset,
        file: typing.Union['IRemediationFile', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IRemediation':
        return super().__new__(
            cls,
            *_args,
            mode=mode,
            quarantine=quarantine,
            file=file,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_remediation_file import IRemediationFile
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.i_remediation_quarantine import IRemediationQuarantine
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.remediation_mode import RemediationMode