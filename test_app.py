from app import app, storage


def test_home():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b'DevOps' in res.data


def test_echo():
    """Test the POST /echo endpoint."""
    client = app.test_client()
    payload = {"msg": "ping"}
    response = client.post('/echo', json=payload)
    assert response.status_code == 201
    assert response.get_json() == payload


def test_echo_complex():
    """Test echo with more complex data."""
    client = app.test_client()
    payload = {"name": "Alice", "age": 30, "skills": ["Python", "Flask"]}
    response = client.post('/echo', json=payload)
    assert response.status_code == 201
    assert response.get_json() == payload


def test_reverse():
    """Test the PUT /reverse endpoint."""
    client = app.test_client()
    payload = {"text": "hello"}
    response = client.put('/reverse', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data['original'] == "hello"
    assert data['reversed'] == "olleh"


def test_reverse_missing_field():
    """Test reverse with missing 'text' field."""
    client = app.test_client()
    payload = {"wrong_field": "data"}
    response = client.put('/reverse', json=payload)
    assert response.status_code == 400
    assert 'error' in response.get_json()


def test_get_jokes():
    """Test the GET /jokes endpoint."""
    client = app.test_client()
    response = client.get('/jokes')
    assert response.status_code == 200
    data = response.get_json()
    assert 'joke' in data
    assert isinstance(data['joke'], str)
    assert len(data['joke']) > 0


def test_storage_workflow():
    """Test the complete storage workflow: GET, POST, DELETE."""
    client = app.test_client()

    # Clear storage first
    storage.clear()

    # Get empty storage
    response = client.get('/storage')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 0
    assert data['items'] == []

    # Add item to storage
    response = client.post('/storage', json={'item': 'test item 1'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Item added'
    assert data['item'] == 'test item 1'

    # Add another item
    response = client.post('/storage', json={'item': 'test item 2'})
    assert response.status_code == 201

    # Get storage with items
    response = client.get('/storage')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 2
    assert 'test item 1' in data['items']
    assert 'test item 2' in data['items']

    # Clear storage
    response = client.delete('/storage')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 2

    # Verify storage is empty
    response = client.get('/storage')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 0


def test_storage_missing_item():
    """Test POST /storage with missing 'item' field."""
    client = app.test_client()
    response = client.post('/storage', json={'wrong_field': 'data'})
    assert response.status_code == 400
    assert 'error' in response.get_json()
