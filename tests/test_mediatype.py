import pytest
from pydantic import BaseModel, ValidationError

from pydantic_media_type import MediaType


class Model(BaseModel):
    media_type: MediaType


def test_mediatype() -> None:
    assert Model(media_type=MediaType("image/png")).media_type == "image/png"


def test_mediatype_invalid() -> None:
    with pytest.raises(ValidationError, match="media_type_unsupported"):
        Model(media_type=MediaType("invalid"))
