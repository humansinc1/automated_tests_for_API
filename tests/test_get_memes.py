from conftest import get_all_memes_endpoint, get_one_meme_endpoint, create_token, create_and_delete_meme


def test_get_memes_list(get_all_memes_endpoint, create_token):
    get_all_memes_endpoint.get_all_memes(create_token)
    get_all_memes_endpoint.is_response_status_200()
    get_all_memes_endpoint.is_result_not_empty()


def test_get_memes_list_without_authorization_is_failed(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes(token=None)
    get_all_memes_endpoint.is_response_status_401()


def test_get_one_meme(get_one_meme_endpoint, create_token, create_and_delete_meme):
    get_one_meme_endpoint.get_one_meme(create_and_delete_meme.meme_id, create_token)
    get_one_meme_endpoint.is_response_status_200()
    get_one_meme_endpoint.is_id_the_same_as_in_request(create_and_delete_meme.meme_id)


def test_get_one_meme_without_authorization_is_failed(get_one_meme_endpoint, create_and_delete_meme):
    get_one_meme_endpoint.get_one_meme(create_and_delete_meme, token=None)
    get_one_meme_endpoint.is_response_status_401()


def test_get_one_meme_without_meme_id_is_failed(get_one_meme_endpoint, create_token):
    get_one_meme_endpoint.get_one_meme(None, create_token)
    get_one_meme_endpoint.is_response_status_404()
