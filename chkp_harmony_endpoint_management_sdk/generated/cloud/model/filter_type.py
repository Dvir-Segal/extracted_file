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


class FilterType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "Contains": "CONTAINS",
            "StartsWith": "STARTS_WITH",
            "EndsWith": "ENDS_WITH",
            "Exact": "EXACT",
            "Grater": "GRATER",
            "Smaller": "SMALLER",
            "BitOr": "BIT_OR",
            "BitAnd": "BIT_AND",
            "IsNull": "IS_NULL",
            "NotNull": "NOT_NULL",
            "Not": "NOT",
            "JsonbExact": "JSONB_EXACT",
            "JsonbContainsAnd": "JSONB_CONTAINS_AND",
            "JsonbContainsOr": "JSONB_CONTAINS_OR",
            "NestedJsonbContainsAnd": "NESTED_JSONB_CONTAINS_AND",
            "NestedJsonbContainsOr": "NESTED_JSONB_CONTAINS_OR",
            "NestedJsonbExactAnd": "NESTED_JSONB_EXACT_AND",
            "NestedJsonbExactOr": "NESTED_JSONB_EXACT_OR",
            "NestedJsonbDateRange": "NESTED_JSONB_DATE_RANGE",
            "ArrayContains": "ARRAY_CONTAINS",
            "Between": "BETWEEN",
        }
    
    @schemas.classproperty
    def CONTAINS(cls):
        return cls("Contains")
    
    @schemas.classproperty
    def STARTS_WITH(cls):
        return cls("StartsWith")
    
    @schemas.classproperty
    def ENDS_WITH(cls):
        return cls("EndsWith")
    
    @schemas.classproperty
    def EXACT(cls):
        return cls("Exact")
    
    @schemas.classproperty
    def GRATER(cls):
        return cls("Grater")
    
    @schemas.classproperty
    def SMALLER(cls):
        return cls("Smaller")
    
    @schemas.classproperty
    def BIT_OR(cls):
        return cls("BitOr")
    
    @schemas.classproperty
    def BIT_AND(cls):
        return cls("BitAnd")
    
    @schemas.classproperty
    def IS_NULL(cls):
        return cls("IsNull")
    
    @schemas.classproperty
    def NOT_NULL(cls):
        return cls("NotNull")
    
    @schemas.classproperty
    def NOT(cls):
        return cls("Not")
    
    @schemas.classproperty
    def JSONB_EXACT(cls):
        return cls("JsonbExact")
    
    @schemas.classproperty
    def JSONB_CONTAINS_AND(cls):
        return cls("JsonbContainsAnd")
    
    @schemas.classproperty
    def JSONB_CONTAINS_OR(cls):
        return cls("JsonbContainsOr")
    
    @schemas.classproperty
    def NESTED_JSONB_CONTAINS_AND(cls):
        return cls("NestedJsonbContainsAnd")
    
    @schemas.classproperty
    def NESTED_JSONB_CONTAINS_OR(cls):
        return cls("NestedJsonbContainsOr")
    
    @schemas.classproperty
    def NESTED_JSONB_EXACT_AND(cls):
        return cls("NestedJsonbExactAnd")
    
    @schemas.classproperty
    def NESTED_JSONB_EXACT_OR(cls):
        return cls("NestedJsonbExactOr")
    
    @schemas.classproperty
    def NESTED_JSONB_DATE_RANGE(cls):
        return cls("NestedJsonbDateRange")
    
    @schemas.classproperty
    def ARRAY_CONTAINS(cls):
        return cls("ArrayContains")
    
    @schemas.classproperty
    def BETWEEN(cls):
        return cls("Between")
