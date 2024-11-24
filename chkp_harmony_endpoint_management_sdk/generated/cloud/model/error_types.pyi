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


class ErrorTypes(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def GENERIC(cls):
        return cls("generic")
    
    @schemas.classproperty
    def CONFLICT(cls):
        return cls("conflict")
    
    @schemas.classproperty
    def INPUTVALIDATIONFAILURE(cls):
        return cls("input-validation-failure")
    
    @schemas.classproperty
    def GENERICUNAUTHORIZED(cls):
        return cls("generic-unauthorized")
    
    @schemas.classproperty
    def ROUTENOTFOUND(cls):
        return cls("route-not-found")
    
    @schemas.classproperty
    def GENERICCANNOTAUTHORIZE(cls):
        return cls("generic-cannot-authorize")
    
    @schemas.classproperty
    def SESSIONMISMATCH(cls):
        return cls("session-mismatch")
    
    @schemas.classproperty
    def GENERICFORBIDDEN(cls):
        return cls("generic-forbidden")
    
    @schemas.classproperty
    def MISSINGCITOKEN(cls):
        return cls("missing-ci-token")
    
    @schemas.classproperty
    def CITOKENEXPIRED(cls):
        return cls("ci-token-expired")
    
    @schemas.classproperty
    def CITOKENNOTYETVALID(cls):
        return cls("ci-token-not-yet-valid")
    
    @schemas.classproperty
    def CITOKENINVALID(cls):
        return cls("ci-token-invalid")
    
    @schemas.classproperty
    def CITOKENMISMATCH(cls):
        return cls("ci-token-mismatch")
    
    @schemas.classproperty
    def MISSINGAPITOKEN(cls):
        return cls("missing-api-token")
    
    @schemas.classproperty
    def APITOKENEXPIRED(cls):
        return cls("api-token-expired")
    
    @schemas.classproperty
    def APITOKENNOTYETVALID(cls):
        return cls("api-token-not-yet-valid")
    
    @schemas.classproperty
    def APITOKENINVALID(cls):
        return cls("api-token-invalid")
    
    @schemas.classproperty
    def APITOKENMALFORMED(cls):
        return cls("api-token-malformed")
    
    @schemas.classproperty
    def NORESPONSEFROMSERVICE(cls):
        return cls("no-response-from-service")
    
    @schemas.classproperty
    def JOBRETURNEDFAILURE(cls):
        return cls("job-returned-failure")
    
    @schemas.classproperty
    def RATELIMITEDGENERAL(cls):
        return cls("rate-limited-general")
    
    @schemas.classproperty
    def MISSINGTENANTMETADATA(cls):
        return cls("missing-tenant-metadata")
