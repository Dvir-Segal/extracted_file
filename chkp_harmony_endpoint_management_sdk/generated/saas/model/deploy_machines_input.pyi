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

from chkp_harmony_endpoint_management_sdk.generated.saas import schemas


class DeployMachinesInput(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "deployInfo",
        }
        
        class properties:
            
            
            class deployInfo(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DeploymentInput']:
                        return DeploymentInput
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DeploymentInput'], typing.List['DeploymentInput']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deployInfo':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DeploymentInput':
                    return super().__getitem__(i)
            __annotations__ = {
                "deployInfo": deployInfo,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    deployInfo: MetaOapg.properties.deployInfo
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deployInfo"]) -> MetaOapg.properties.deployInfo: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["deployInfo"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deployInfo"]) -> MetaOapg.properties.deployInfo: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["deployInfo"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        deployInfo: typing.Union[MetaOapg.properties.deployInfo, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DeployMachinesInput':
        return super().__new__(
            cls,
            *_args,
            deployInfo=deployInfo,
            _configuration=_configuration,
        )

from chkp_harmony_endpoint_management_sdk.generated.saas.model.deployment_input import DeploymentInput