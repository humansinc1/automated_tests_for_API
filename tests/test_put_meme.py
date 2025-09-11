import pytest

from conftest import put_meme_endpoint, create_and_delete_meme, create_token


def test_update_meme(create_and_delete_meme, put_meme_endpoint, create_token):
    put_meme_endpoint.put_meme(create_and_delete_meme.meme_id, create_token)
    put_meme_endpoint.is_response_status_200()
    put_meme_endpoint.is_body_text_changed()
    put_meme_endpoint.is_body_text_correct()
    put_meme_endpoint.is_body_url_correct()
    put_meme_endpoint.is_body_tags_correct()
    put_meme_endpoint.is_body_info_correct()


@pytest.mark.parametrize(
    "id,text,url,tags,info",
    [
        pytest.param(
            {},
            {"text": "text"},
            {"url": "updated"},
            {"tags": ["updated", "qa", "fun"]},
            {"info": {"updated": ["qa", "bugs"], "color": "sand"}},
            id="without id",
        ),
        pytest.param(
            {"id": "id"},
            {"text": "text"},
            {"url": "updated"},
            {"tags": ["updated", "qa", "fun"]},
            {"info": {"updated": ["qa", "bugs"], "color": "sand"}},
            id="with wrong id value type",
        ),
    ],
)
def test_is_update_meme_without_id_failed(
    create_and_delete_meme, put_meme_endpoint, create_token, id, text, url, tags, info
):
    body = {
        **id,
        **text,
        **url,
        **tags,
        **info
    }
    put_meme_endpoint.put_meme(create_and_delete_meme.meme_id, create_token, body)
    put_meme_endpoint.is_response_status_400()
