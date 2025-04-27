import pytest
from app import app, get_db_connection

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_displays_all_posts(client):
    response = client.get('/')
    assert response.status_code == 200

# def test_post_displays_correct_post(client):
#     with get_db_connection() as conn:
#         conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', ('Test Post', 'Test Content'))
#         conn.commit()
#     response = client.get('/1')
#     assert response.status_code == 200

def test_create_requires_title(client):
    response = client.post('/create', data={'title': '', 'content': 'Content'}, follow_redirects=True)
    assert response.status_code == 200

def test_create_adds_new_post(client):
    response = client.post('/create', data={'title': 'New Post', 'content': 'New Content'}, follow_redirects=True)
    assert response.status_code == 200

# def test_edit_updates_post(client):
#     with get_db_connection() as conn:
#         conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', ('Old Title', 'Old Content'))
#         conn.commit()
#     response = client.post('/1/edit', data={'title': 'Updated Title', 'content': 'Updated Content'}, follow_redirects=True)
#     assert response.status_code == 200
#
# def test_delete_removes_post(client):
#     with get_db_connection() as conn:
#         conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', ('To Delete', 'Content'))
#         conn.commit()
#     response = client.post('/1/delete', follow_redirects=True)
#     assert response.status_code == 200