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


class JobOrResultIndicatorOfCompromiseArray(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Either an object containing a Job ID *OR* schema 'IndicatorOfCompromise-Array'
<p>The actual return value varies depending on whether the request specified header <em>x-mgmt-run-as-job</em> '<em>ON</em>' or '<em>OFF</em>'.</p>
<p>When set to '<em>ON</em>', operations will run asynchronously and return the <em>JobCreationResult</em> schema</p>
<p>When set to '<em>OFF</em>', operations will run synchronously and return a concrete response of type <em>IndicatorOfCompromise-Array</em></p>
    """


    class MetaOapg:
        
        
        class one_of_0(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                
                @staticmethod
                def items() -> typing.Type['IndicatorOfCompromise']:
                    return IndicatorOfCompromise
        
            def __new__(
                cls,
                _arg: typing.Union[typing.Tuple['IndicatorOfCompromise'], typing.List['IndicatorOfCompromise']],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    _arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> 'IndicatorOfCompromise':
                return super().__getitem__(i)
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                JobCreationResult,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobOrResultIndicatorOfCompromiseArray':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from chkp_harmony_endpoint_management_sdk.generated.cloud.model.indicator_of_compromise import IndicatorOfCompromise
from chkp_harmony_endpoint_management_sdk.generated.cloud.model.job_creation_result import JobCreationResult