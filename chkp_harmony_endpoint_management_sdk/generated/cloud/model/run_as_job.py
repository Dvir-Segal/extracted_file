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


class RunAsJob(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Depicts values that, when used in the header specified by RestHeaders.USE_JOB, determines whether a given operation will run as a job (asynchronously)
    """


    class MetaOapg:
        enum_value_to_name = {
            "on": "ON",
            "off": "OFF",
        }
    
    @schemas.classproperty
    def ON(cls):
        return cls("on")
    
    @schemas.classproperty
    def OFF(cls):
        return cls("off")
