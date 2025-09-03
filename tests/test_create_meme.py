from conftest import create_meme_endpoint, create_token


def test_create_meme(create_meme_endpoint, create_token):
    create_meme_endpoint.create_and_delete_meme(create_token)
    create_meme_endpoint.is_response_status_200()
    create_meme_endpoint.is_body_text_correct()


def test_create_meme_with_wrong_text_value_type_is_failed(create_meme_endpoint, create_token):
    body = {
        "text": 2,
        "url": "https://imgs.search.brave.com/uxF23AlGbpdMvtkhGF_yNDyCkkiEjG_4JdYd9Pw1GI0/rs:fit:500:0:1:0/g:ce/" +
               "aHR0cHM6Ly93d3cu/c2lsaWNvbnJlcHVi/bGljLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxNS8wNS9R/" +
               "QS1UZXN0ZXItbWVt/ZS0wMy5qcGc",
        "tags": ['grumpy cat', 'qa', 'fun'],
        "info": {'subject': ['qa', 'bugs'], 'color': 'sand'}
    }
    create_meme_endpoint.create_and_delete_meme(create_token, body)
    create_meme_endpoint.is_response_status_400()


def test_create_meme_with_wrong_url_value_type_is_failed(create_meme_endpoint, create_token):
    body = {
        "text": "99 little bugs",
        "url": ["https://imgs.search.brave.com/uxF23AlGbpdMvtkhGF_yNDyCkkiEjG_4JdYd9Pw1GI0/rs:fit:500:0:1:0/g:ce/" +
               "aHR0cHM6Ly93d3cu/c2lsaWNvbnJlcHVi/bGljLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxNS8wNS9R/" +
               "QS1UZXN0ZXItbWVt/ZS0wMy5qcGc"],
        "tags": ['grumpy cat', 'qa', 'fun'],
        "info": {'subject': ['qa', 'bugs'], 'color': 'sand'}
    }
    create_meme_endpoint.create_and_delete_meme(create_token, body)
    create_meme_endpoint.is_response_status_400()


def test_create_meme_with_wrong_tags_value_type_is_failed(create_meme_endpoint, create_token):
    body = {
        "text": "99 little bugs",
        "url": "https://imgs.search.brave.com/uxF23AlGbpdMvtkhGF_yNDyCkkiEjG_4JdYd9Pw1GI0/rs:fit:500:0:1:0/g:ce/" +
               "aHR0cHM6Ly93d3cu/c2lsaWNvbnJlcHVi/bGljLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxNS8wNS9R/" +
               "QS1UZXN0ZXItbWVt/ZS0wMy5qcGc",
        "tags": {'grumpy cat': ['qa', 'fun']},
        "info": {'subject': ['qa', 'bugs'], 'color': 'sand'}
    }
    create_meme_endpoint.create_and_delete_meme(create_token, body)
    create_meme_endpoint.is_response_status_400()


def test_create_meme_with_wrong_info_value_type_is_failed(create_meme_endpoint, create_token):
    body = {
        "text": "99 little bugs",
        "url": "https://imgs.search.brave.com/uxF23AlGbpdMvtkhGF_yNDyCkkiEjG_4JdYd9Pw1GI0/rs:fit:500:0:1:0/g:ce/" +
               "aHR0cHM6Ly93d3cu/c2lsaWNvbnJlcHVi/bGljLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxNS8wNS9R/" +
               "QS1UZXN0ZXItbWVt/ZS0wMy5qcGc",
        "tags": ['grumpy cat', 'qa', 'fun'],
        "info": ['color', 'sand']
    }
    create_meme_endpoint.create_and_delete_meme(create_token, body)
    create_meme_endpoint.is_response_status_400()


def test_create_meme_without_required_url_is_failed(create_meme_endpoint, create_token):
    body = {
        "text": 2,
        "tags": ['grumpy cat', 'qa', 'fun'],
        "info": {'subject': ['qa', 'bugs'], 'color': 'sand'}
    }
    create_meme_endpoint.create_and_delete_meme(create_token, body)
    create_meme_endpoint.is_response_status_400()


def test_create_meme_without_required_text_is_failed(create_meme_endpoint, create_token):
    body = {
        "url": "https://imgs.search.brave.com/uxF23AlGbpdMvtkhGF_yNDyCkkiEjG_4JdYd9Pw1GI0/rs:fit:500:0:1:0/g:ce/" +
                "aHR0cHM6Ly93d3cu/c2lsaWNvbnJlcHVi/bGljLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxNS8wNS9R/" +
                "QS1UZXN0ZXItbWVt/ZS0wMy5qcGc",
        "tags": ['grumpy cat', 'qa', 'fun'],
        "info": {'subject': ['qa', 'bugs'], 'color': 'sand'}
    }
    create_meme_endpoint.create_and_delete_meme(create_token, body)
    create_meme_endpoint.is_response_status_400()


def test_create_meme_without_required_tags_is_failed(create_meme_endpoint, create_token):
    body = {
        "text": "2",
        "url": "https://imgs.search.brave.com/uxF23AlGbpdMvtkhGF_yNDyCkkiEjG_4JdYd9Pw1GI0/rs:fit:500:0:1:0/g:ce/" +
               "aHR0cHM6Ly93d3cu/c2lsaWNvbnJlcHVi/bGljLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxNS8wNS9R/" +
               "QS1UZXN0ZXItbWVt/ZS0wMy5qcGc",
        "info": {'subject': ['qa', 'bugs'], 'color': 'sand'}
    }
    create_meme_endpoint.create_and_delete_meme(create_token, body)
    create_meme_endpoint.is_response_status_400()


def test_create_meme_without_required_info_is_failed(create_meme_endpoint, create_token):
    body = {
        "text": "2",
        "url": "https://imgs.search.brave.com/uxF23AlGbpdMvtkhGF_yNDyCkkiEjG_4JdYd9Pw1GI0/rs:fit:500:0:1:0/g:ce/" +
               "aHR0cHM6Ly93d3cu/c2lsaWNvbnJlcHVi/bGljLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxNS8wNS9R/" +
               "QS1UZXN0ZXItbWVt/ZS0wMy5qcGc",
        "tags": ['grumpy cat', 'qa', 'fun'],
    }
    create_meme_endpoint.create_and_delete_meme(create_token, body)
    create_meme_endpoint.is_response_status_400()
