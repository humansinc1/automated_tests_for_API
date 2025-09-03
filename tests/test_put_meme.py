from conftest import put_meme_endpoint, create_and_delete_meme, create_token


def test_update_meme(create_and_delete_meme, put_meme_endpoint, create_token):
    put_meme_endpoint.put_meme(create_and_delete_meme.meme_id, create_token)
    put_meme_endpoint.is_response_status_200()
    put_meme_endpoint.is_body_text_changed()


def test_is_update_meme_without_id_failed(create_and_delete_meme, put_meme_endpoint, create_token):
    body = {
        "text": "text",
        "url": "updated",
        "tags": ["updated", "qa", "fun"],
        "info": {"updated": ["qa", "bugs"], "color": "sand"},
    }
    put_meme_endpoint.put_meme(create_and_delete_meme.meme_id, create_token, body)
    put_meme_endpoint.is_response_status_400()


def test_is_update_meme_with_wrong_id_type_failed(create_and_delete_meme, put_meme_endpoint, create_token):
    body = {
        "id": "id",
        "text": "text",
        "url": "updated",
        "tags": ["updated", "qa", "fun"],
        "info": {"updated": ["qa", "bugs"], "color": "sand"},
    }
    put_meme_endpoint.put_meme(create_and_delete_meme.meme_id, create_token, body)
    put_meme_endpoint.is_response_status_400()
