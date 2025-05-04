from app import handler

def test_handler():
    assert handler()["status"] == "success"
