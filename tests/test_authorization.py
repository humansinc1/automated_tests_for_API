from conftest import authorization_endpoint


def test_authorization_is_success(authorization_endpoint):
    authorization_endpoint.get_token()
    authorization_endpoint.is_response_status_200()
    authorization_endpoint.is_user_name_correct()
    authorization_endpoint.is_token_created()


def test_authorization_with_wrong_body_key_name_is_failed(authorization_endpoint):
    body = {"adsofiujsad": "SergeiL"}
    authorization_endpoint.get_token(body)
    authorization_endpoint.is_response_status_400()


def test_authorization_with_empty_name_value_is_failed(authorization_endpoint):
    body = {"name": ""}
    authorization_endpoint.get_token(body)
    authorization_endpoint.is_response_status_400()


def test_authorization_with_wrong_name_type_is_failed(authorization_endpoint):
    body = {"name": 2}
    authorization_endpoint.get_token(body)
    authorization_endpoint.is_response_status_400()
