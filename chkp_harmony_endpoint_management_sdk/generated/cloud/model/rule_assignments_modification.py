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


class RuleAssignmentsModification(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Assignment modifications made to a rule
    """

    class MetaOapg:
        required = {
            "modified",
        }
        
        class properties:
            modified = schemas.BoolSchema
            
            
            class added(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RuleAssignment']:
                        return RuleAssignment
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RuleAssignment'], typing.List['RuleAssignment']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'added':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RuleAssignment':
                    return super().__getitem__(i)
            
            
            class removed(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RuleAssignment']:
                        return RuleAssignment
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RuleAssignment'], typing.List['RuleAssignment']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'removed':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RuleAssignment':
                    return super().__getitem__(i)
            __annotations__ = {
                "modified": modified,
                "added": added,
                "removed": removed,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    modified: MetaOapg.properties.modified
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified"]) -> MetaOapg.properties.modified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added"]) -> MetaOapg.properties.added: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["removed"]) -> MetaOapg.properties.removed: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["modified"], typing_extensions.Literal["added"], typing_extensions.Literal["removed"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified"]) -> MetaOapg.properties.modified: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added"]) -> typing.Union[MetaOapg.properties.added, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["removed"]) -> typing.Union[MetaOapg.properties.removed, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["modified"], typing_extensions.Literal["added"], typing_extensions.Literal["removed"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        modified: typing.Union[MetaOapg.properties.modified, bool, ],
        added: typing.Union[MetaOapg.properties.added, list, tuple, schemas.Unset] = schemas.unset,
        removed: typing.Union[MetaOapg.properties.removed, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'RuleAssignmentsModification':
        return super().__new__(
            cls,
            *_args,
            modified=modified,
            added=added,
            removed=removed,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.rule_assignment import RuleAssignment