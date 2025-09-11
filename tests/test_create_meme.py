import pytest
from conftest import create_meme_endpoint, create_token


def test_create_meme(create_meme_endpoint, create_token):
    create_meme_endpoint.create_meme(create_token)
    create_meme_endpoint.is_response_status_200()
    create_meme_endpoint.is_body_text_correct()
    create_meme_endpoint.is_body_url_correct()
    create_meme_endpoint.is_body_tags_correct()
    create_meme_endpoint.is_body_info_correct()


@pytest.mark.parametrize(
    "text,body_url,tags,info",
    [
        pytest.param(
            {"text": 2},
            {"url": "https..."},
            {"tags": ["grumpy"]},
            {"info": {"subject": "test"}},
            id="wrong text value type",
        ),
        pytest.param(
            {"text": "test"},
            {"url": ["https..."]},
            {"tags": ["grumpy"]},
            {"info": {"subject": "test"}},
            id="wrong url value type",
        ),
        pytest.param(
            {"text": "test"},
            {"url": "https..."},
            {"tags": {"grumpy": "cat"}},
            {"info": {"subject": "test"}},
            id="wrong tags value type",
        ),
        pytest.param(
            {"text": "test"},
            {"url": "https..."},
            {"tags": ["grumpy"]},
            {"info": ["subject", "test"]},
            id="wrong info value type",
        ),
        pytest.param(
            {},
            {"url": "https..."},
            {"tags": ["grumpy"]},
            {"info": {"subject": "test"}},
            id="without text",
        ),
        pytest.param(
            {"text": "test"},
            {},
            {"tags": ["grumpy"]},
            {"info": {"subject": "test"}},
            id="without url",
        ),
        pytest.param(
            {"text": "test"},
            {"url": "https..."},
            {},
            {"info": {"subject": "test"}},
            id="without tags",
        ),
        pytest.param(
            {"text": "test"},
            {"url": "https..."},
            {"tags": ["grumpy"]},
            {},
            id="without info",
        ),
    ],
)
def test_create_meme_with_wrong_value_type_is_failed(
    create_meme_endpoint, create_token, text, body_url, tags, info
):
    body = {
        **text,
        **body_url,
        **tags,
        **info
    }
    create_meme_endpoint.create_meme(create_token, body)
    create_meme_endpoint.is_response_status_400()
