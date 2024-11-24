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


class IBehavioralProtectionBackupFileTypes(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "extension",
            "maximumSizeMb",
            "ignoreAssociatedApplications",
        }
        
        class properties:
            ignoreAssociatedApplications = schemas.BoolSchema
            
            
            class maximumSizeMb(
                schemas.Float64Schema
            ):
                pass
            extension = schemas.StrSchema
            __annotations__ = {
                "ignoreAssociatedApplications": ignoreAssociatedApplications,
                "maximumSizeMb": maximumSizeMb,
                "extension": extension,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    extension: MetaOapg.properties.extension
    maximumSizeMb: MetaOapg.properties.maximumSizeMb
    ignoreAssociatedApplications: MetaOapg.properties.ignoreAssociatedApplications
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension"]) -> MetaOapg.properties.extension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximumSizeMb"]) -> MetaOapg.properties.maximumSizeMb: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ignoreAssociatedApplications"]) -> MetaOapg.properties.ignoreAssociatedApplications: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["extension"], typing_extensions.Literal["maximumSizeMb"], typing_extensions.Literal["ignoreAssociatedApplications"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension"]) -> MetaOapg.properties.extension: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximumSizeMb"]) -> MetaOapg.properties.maximumSizeMb: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ignoreAssociatedApplications"]) -> MetaOapg.properties.ignoreAssociatedApplications: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["extension"], typing_extensions.Literal["maximumSizeMb"], typing_extensions.Literal["ignoreAssociatedApplications"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        extension: typing.Union[MetaOapg.properties.extension, str, ],
        maximumSizeMb: typing.Union[MetaOapg.properties.maximumSizeMb, decimal.Decimal, int, float, ],
        ignoreAssociatedApplications: typing.Union[MetaOapg.properties.ignoreAssociatedApplications, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IBehavioralProtectionBackupFileTypes':
        return super().__new__(
            cls,
            *_args,
            extension=extension,
            maximumSizeMb=maximumSizeMb,
            ignoreAssociatedApplications=ignoreAssociatedApplications,
            _configuration=_configuration,
        )