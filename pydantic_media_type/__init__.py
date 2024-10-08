from mimetypes import MimeTypes
from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, PydanticCustomError, core_schema


class MediaType(str):
    types: list[str] = []

    @classmethod
    def _init_types(cls) -> None:
        if len(cls.types) == 0:
            mime_types = MimeTypes()
            for types_map in mime_types.types_map_inv:
                for mime_type in types_map.keys():
                    if mime_type not in cls.types:
                        cls.types.append(mime_type)

    @classmethod
    def _validate(cls, value: str, source_type: Any) -> str:
        cls._init_types()

        if value not in cls.types:
            raise PydanticCustomError(
                "media_type_unsupported", "Provided media type is not valid"
            )

        return value

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.with_info_before_validator_function(
            cls._validate,
            core_schema.str_schema(),
        )
