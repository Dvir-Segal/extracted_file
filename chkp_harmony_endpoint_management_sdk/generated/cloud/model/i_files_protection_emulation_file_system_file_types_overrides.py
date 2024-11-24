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


class IFilesProtectionEmulationFileSystemFileTypesOverrides(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "defaultAction",
            "name",
            "action",
            "description",
        }
        
        class properties:
        
            @staticmethod
            def action() -> typing.Type['FileTypeOverrideActions']:
                return FileTypeOverrideActions
        
            @staticmethod
            def defaultAction() -> typing.Type['FileTypeOverrideActions']:
                return FileTypeOverrideActions
            description = schemas.StrSchema
            name = schemas.StrSchema
            __annotations__ = {
                "action": action,
                "defaultAction": defaultAction,
                "description": description,
                "name": name,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    defaultAction: 'FileTypeOverrideActions'
    name: MetaOapg.properties.name
    action: 'FileTypeOverrideActions'
    description: MetaOapg.properties.description
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultAction"]) -> 'FileTypeOverrideActions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> 'FileTypeOverrideActions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["defaultAction"], typing_extensions.Literal["name"], typing_extensions.Literal["action"], typing_extensions.Literal["description"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultAction"]) -> 'FileTypeOverrideActions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> 'FileTypeOverrideActions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["defaultAction"], typing_extensions.Literal["name"], typing_extensions.Literal["action"], typing_extensions.Literal["description"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        defaultAction: 'FileTypeOverrideActions',
        name: typing.Union[MetaOapg.properties.name, str, ],
        action: 'FileTypeOverrideActions',
        description: typing.Union[MetaOapg.properties.description, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IFilesProtectionEmulationFileSystemFileTypesOverrides':
        return super().__new__(
            cls,
            *_args,
            defaultAction=defaultAction,
            name=name,
            action=action,
            description=description,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.file_type_override_actions import FileTypeOverrideActions
