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


class AmScanParameters(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
            informUser = schemas.BoolSchema
            allowPostpone = schemas.BoolSchema
            scanCritical = schemas.BoolSchema
            scanLocalDrives = schemas.BoolSchema
            scanCdRom = schemas.BoolSchema
            scanRemovable = schemas.BoolSchema
            scanNetwork = schemas.BoolSchema
            scanOther = schemas.BoolSchema
            limitScanBySize = schemas.BoolSchema
            
            
            class fileSizeLimit(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    format = 'double'
                    inclusive_minimum = 1
            skipNonExecutables = schemas.BoolSchema
            __annotations__ = {
                "informUser": informUser,
                "allowPostpone": allowPostpone,
                "scanCritical": scanCritical,
                "scanLocalDrives": scanLocalDrives,
                "scanCdRom": scanCdRom,
                "scanRemovable": scanRemovable,
                "scanNetwork": scanNetwork,
                "scanOther": scanOther,
                "limitScanBySize": limitScanBySize,
                "fileSizeLimit": fileSizeLimit,
                "skipNonExecutables": skipNonExecutables,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["informUser"]) -> MetaOapg.properties.informUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowPostpone"]) -> MetaOapg.properties.allowPostpone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scanCritical"]) -> MetaOapg.properties.scanCritical: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scanLocalDrives"]) -> MetaOapg.properties.scanLocalDrives: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scanCdRom"]) -> MetaOapg.properties.scanCdRom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scanRemovable"]) -> MetaOapg.properties.scanRemovable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scanNetwork"]) -> MetaOapg.properties.scanNetwork: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scanOther"]) -> MetaOapg.properties.scanOther: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limitScanBySize"]) -> MetaOapg.properties.limitScanBySize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileSizeLimit"]) -> MetaOapg.properties.fileSizeLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skipNonExecutables"]) -> MetaOapg.properties.skipNonExecutables: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["informUser"], typing_extensions.Literal["allowPostpone"], typing_extensions.Literal["scanCritical"], typing_extensions.Literal["scanLocalDrives"], typing_extensions.Literal["scanCdRom"], typing_extensions.Literal["scanRemovable"], typing_extensions.Literal["scanNetwork"], typing_extensions.Literal["scanOther"], typing_extensions.Literal["limitScanBySize"], typing_extensions.Literal["fileSizeLimit"], typing_extensions.Literal["skipNonExecutables"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["informUser"]) -> typing.Union[MetaOapg.properties.informUser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowPostpone"]) -> typing.Union[MetaOapg.properties.allowPostpone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scanCritical"]) -> typing.Union[MetaOapg.properties.scanCritical, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scanLocalDrives"]) -> typing.Union[MetaOapg.properties.scanLocalDrives, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scanCdRom"]) -> typing.Union[MetaOapg.properties.scanCdRom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scanRemovable"]) -> typing.Union[MetaOapg.properties.scanRemovable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scanNetwork"]) -> typing.Union[MetaOapg.properties.scanNetwork, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scanOther"]) -> typing.Union[MetaOapg.properties.scanOther, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limitScanBySize"]) -> typing.Union[MetaOapg.properties.limitScanBySize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileSizeLimit"]) -> typing.Union[MetaOapg.properties.fileSizeLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skipNonExecutables"]) -> typing.Union[MetaOapg.properties.skipNonExecutables, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["informUser"], typing_extensions.Literal["allowPostpone"], typing_extensions.Literal["scanCritical"], typing_extensions.Literal["scanLocalDrives"], typing_extensions.Literal["scanCdRom"], typing_extensions.Literal["scanRemovable"], typing_extensions.Literal["scanNetwork"], typing_extensions.Literal["scanOther"], typing_extensions.Literal["limitScanBySize"], typing_extensions.Literal["fileSizeLimit"], typing_extensions.Literal["skipNonExecutables"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        informUser: typing.Union[MetaOapg.properties.informUser, bool, schemas.Unset] = schemas.unset,
        allowPostpone: typing.Union[MetaOapg.properties.allowPostpone, bool, schemas.Unset] = schemas.unset,
        scanCritical: typing.Union[MetaOapg.properties.scanCritical, bool, schemas.Unset] = schemas.unset,
        scanLocalDrives: typing.Union[MetaOapg.properties.scanLocalDrives, bool, schemas.Unset] = schemas.unset,
        scanCdRom: typing.Union[MetaOapg.properties.scanCdRom, bool, schemas.Unset] = schemas.unset,
        scanRemovable: typing.Union[MetaOapg.properties.scanRemovable, bool, schemas.Unset] = schemas.unset,
        scanNetwork: typing.Union[MetaOapg.properties.scanNetwork, bool, schemas.Unset] = schemas.unset,
        scanOther: typing.Union[MetaOapg.properties.scanOther, bool, schemas.Unset] = schemas.unset,
        limitScanBySize: typing.Union[MetaOapg.properties.limitScanBySize, bool, schemas.Unset] = schemas.unset,
        fileSizeLimit: typing.Union[MetaOapg.properties.fileSizeLimit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        skipNonExecutables: typing.Union[MetaOapg.properties.skipNonExecutables, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AmScanParameters':
        return super().__new__(
            cls,
            *_args,
            informUser=informUser,
            allowPostpone=allowPostpone,
            scanCritical=scanCritical,
            scanLocalDrives=scanLocalDrives,
            scanCdRom=scanCdRom,
            scanRemovable=scanRemovable,
            scanNetwork=scanNetwork,
            scanOther=scanOther,
            limitScanBySize=limitScanBySize,
            fileSizeLimit=fileSizeLimit,
            skipNonExecutables=skipNonExecutables,
            _configuration=_configuration,
        )