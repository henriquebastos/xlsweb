def test_home_get(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert 'index.html' in (t.name for t in resp.templates)


def test_home_post(client):
    with open('contrib/card.xls', 'rb') as f:
        resp = client.post('/', {'range': 'B3:E13', 'xls': f})

    assert resp.status_code == 200
    assert resp.content == open('contrib/golden.txt', 'rb').read()

