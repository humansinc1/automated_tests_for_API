from conftest import delete_meme_endpoint, create_meme, create_token


def test_delete_meme(delete_meme_endpoint, create_meme, create_token):
    delete_meme_endpoint.delete_meme(create_token, create_meme)
    delete_meme_endpoint.is_response_status_200()
    delete_meme_endpoint.is_deleted_meme_id_absent_in_meme_list(create_meme, create_token)


def test_non_existed_meme_failed(delete_meme_endpoint, create_token):
    delete_meme_endpoint.delete_meme(create_token, '-1')
    delete_meme_endpoint.is_response_status_404()


def test_deleting_meme_without_authorization(delete_meme_endpoint):
    delete_meme_endpoint.delete_meme('123', '1')
    delete_meme_endpoint.is_response_status_401()


def test_deleting_not_your_meme(delete_meme_endpoint, create_token):
    delete_meme_endpoint.delete_meme(create_token, '1')
    delete_meme_endpoint.is_response_status_403()
