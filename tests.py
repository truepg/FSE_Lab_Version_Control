from storage import Storage

def test_add():
    st = Storage({'a': 1, 'b': 2})
    
    key, val = 'c', 3
    st.add(key, val)
    assert st.get(key) == val, "Value for the key {} is not equal to excepted".format(key)

    key, val = 'b', 20
    try:
        st.add(key, val)
    except KeyError:
        pass
    else:
        raise Exception

def test_remove():
    pass

def test_set():
    stor = Storage({'a' : 1, 'b' : 2})
    key = 'a'
    new_value = 0
    stor.set(key, new_value)
    assert stor.get(key) == new_value, "New key-value pair not found"
    key = 'c'
    try:
        stor.set(key, new_value)
    except Exception:
        assert True

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
