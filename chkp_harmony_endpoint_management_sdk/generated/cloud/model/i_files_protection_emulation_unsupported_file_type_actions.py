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


class IFilesProtectionEmulationUnsupportedFileTypeActions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "downloadAction",
            "comment",
            "uploadAction",
            "fileType",
        }
        
        class properties:
        
            @staticmethod
            def uploadAction() -> typing.Type['TeUnsupportedFileAction']:
                return TeUnsupportedFileAction
        
            @staticmethod
            def downloadAction() -> typing.Type['TeUnsupportedFileAction']:
                return TeUnsupportedFileAction
            comment = schemas.StrSchema
            fileType = schemas.StrSchema
            __annotations__ = {
                "uploadAction": uploadAction,
                "downloadAction": downloadAction,
                "comment": comment,
                "fileType": fileType,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    downloadAction: 'TeUnsupportedFileAction'
    comment: MetaOapg.properties.comment
    uploadAction: 'TeUnsupportedFileAction'
    fileType: MetaOapg.properties.fileType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["downloadAction"]) -> 'TeUnsupportedFileAction': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uploadAction"]) -> 'TeUnsupportedFileAction': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileType"]) -> MetaOapg.properties.fileType: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["downloadAction"], typing_extensions.Literal["comment"], typing_extensions.Literal["uploadAction"], typing_extensions.Literal["fileType"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["downloadAction"]) -> 'TeUnsupportedFileAction': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uploadAction"]) -> 'TeUnsupportedFileAction': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileType"]) -> MetaOapg.properties.fileType: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["downloadAction"], typing_extensions.Literal["comment"], typing_extensions.Literal["uploadAction"], typing_extensions.Literal["fileType"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        downloadAction: 'TeUnsupportedFileAction',
        comment: typing.Union[MetaOapg.properties.comment, str, ],
        uploadAction: 'TeUnsupportedFileAction',
        fileType: typing.Union[MetaOapg.properties.fileType, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IFilesProtectionEmulationUnsupportedFileTypeActions':
        return super().__new__(
            cls,
            *_args,
            downloadAction=downloadAction,
            comment=comment,
            uploadAction=uploadAction,
            fileType=fileType,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.te_unsupported_file_action import TeUnsupportedFileAction