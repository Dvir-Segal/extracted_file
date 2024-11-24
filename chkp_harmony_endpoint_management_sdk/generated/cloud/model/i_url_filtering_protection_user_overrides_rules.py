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


class IUrlFilteringProtectionUserOverridesRules(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
            
            
            class blockedUrls(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'blockedUrls':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class categories(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UrlFilteringCategoryRule']:
                        return UrlFilteringCategoryRule
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['UrlFilteringCategoryRule'], typing.List['UrlFilteringCategoryRule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'categories':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UrlFilteringCategoryRule':
                    return super().__getitem__(i)
            __annotations__ = {
                "blockedUrls": blockedUrls,
                "categories": categories,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockedUrls"]) -> MetaOapg.properties.blockedUrls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["categories"]) -> MetaOapg.properties.categories: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["blockedUrls"], typing_extensions.Literal["categories"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockedUrls"]) -> typing.Union[MetaOapg.properties.blockedUrls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["categories"]) -> typing.Union[MetaOapg.properties.categories, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["blockedUrls"], typing_extensions.Literal["categories"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        blockedUrls: typing.Union[MetaOapg.properties.blockedUrls, list, tuple, schemas.Unset] = schemas.unset,
        categories: typing.Union[MetaOapg.properties.categories, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IUrlFilteringProtectionUserOverridesRules':
        return super().__new__(
            cls,
            *_args,
            blockedUrls=blockedUrls,
            categories=categories,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.url_filtering_category_rule import UrlFilteringCategoryRule