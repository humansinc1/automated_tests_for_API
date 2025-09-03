from conftest import delete_meme_endpoint, create_meme, create_token


def test_delete_meme(delete_meme_endpoint, create_meme, create_token):
    delete_meme_endpoint.delete_meme(create_token, create_meme)
    delete_meme_endpoint.is_response_status_200()
    delete_meme_endpoint.is_deleted_meme_id_absent_in_meme_list(create_meme, create_token)
