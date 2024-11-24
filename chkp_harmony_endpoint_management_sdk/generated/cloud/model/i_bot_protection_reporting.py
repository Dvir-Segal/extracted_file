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


class IBotProtectionReporting(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        
        class properties:
            botReportingRemovalDays = schemas.Float64Schema
            logSuppressionHours = schemas.Float64Schema
            __annotations__ = {
                "botReportingRemovalDays": botReportingRemovalDays,
                "logSuppressionHours": logSuppressionHours,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["botReportingRemovalDays"]) -> MetaOapg.properties.botReportingRemovalDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logSuppressionHours"]) -> MetaOapg.properties.logSuppressionHours: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["botReportingRemovalDays"], typing_extensions.Literal["logSuppressionHours"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["botReportingRemovalDays"]) -> typing.Union[MetaOapg.properties.botReportingRemovalDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logSuppressionHours"]) -> typing.Union[MetaOapg.properties.logSuppressionHours, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["botReportingRemovalDays"], typing_extensions.Literal["logSuppressionHours"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        botReportingRemovalDays: typing.Union[MetaOapg.properties.botReportingRemovalDays, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        logSuppressionHours: typing.Union[MetaOapg.properties.logSuppressionHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IBotProtectionReporting':
        return super().__new__(
            cls,
            *_args,
            botReportingRemovalDays=botReportingRemovalDays,
            logSuppressionHours=logSuppressionHours,
            _configuration=_configuration,
        )