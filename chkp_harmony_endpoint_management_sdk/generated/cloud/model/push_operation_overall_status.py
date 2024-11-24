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


class PushOperationOverallStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ABORTED": "ABORTED",
            "NOT_STARTED": "NOT_STARTED",
            "COMPLETED": "COMPLETED",
            "COMPLETED_WITH_WARNINGS": "COMPLETED_WITH_WARNINGS",
            "IN_PROGRESS": "IN_PROGRESS",
        }
    
    @schemas.classproperty
    def ABORTED(cls):
        return cls("ABORTED")
    
    @schemas.classproperty
    def NOT_STARTED(cls):
        return cls("NOT_STARTED")
    
    @schemas.classproperty
    def COMPLETED(cls):
        return cls("COMPLETED")
    
    @schemas.classproperty
    def COMPLETED_WITH_WARNINGS(cls):
        return cls("COMPLETED_WITH_WARNINGS")
    
    @schemas.classproperty
    def IN_PROGRESS(cls):
        return cls("IN_PROGRESS")