import pytest

from endpoints.authorization import Authorization, CheckToken
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_memes import GetAllMemes, GetOneMeme
from endpoints.put_meme import PutMeme


@pytest.fixture(scope='session')
def authorization_endpoint():
    return Authorization()


@pytest.fixture()
def check_token_endpoint():
    return CheckToken()


@pytest.fixture()
def get_all_memes_endpoint():
    return GetAllMemes()


@pytest.fixture()
def get_one_meme_endpoint():
    return GetOneMeme()


@pytest.fixture(scope='session')
def create_token(authorization_endpoint):
    return authorization_endpoint.get_token()


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def create_and_delete_meme(create_token, create_meme_endpoint, delete_meme_endpoint):
    create_meme_endpoint.create_meme(create_token)
    meme_id = create_meme_endpoint.meme_id
    yield create_meme_endpoint
    delete_meme_endpoint.delete_meme(create_token, meme_id)


@pytest.fixture()
def create_meme(create_token, create_meme_endpoint,):
    create_meme_endpoint.create_meme(create_token)
    return create_meme_endpoint.meme_id


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def put_meme_endpoint():
    return PutMeme()
