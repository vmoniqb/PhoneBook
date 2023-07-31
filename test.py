import unittest
from main import app


class PhoneBookTest(unittest.TestCase):

    # Test user can list all entries they've created
    def test_list_all(self):
        test_call = app.test_client(self)
        response = test_call.get('/contacts')
        self.assertEqual(response.status_code, 200)

    # Test get by id fails for non-existing ids
    def test_view_by_id(self):
        test_call = app.test_client(self)
        response = test_call.get('/contacts/0')
        self.assertEqual(response.status_code, 404)

    # Test existing and non-existent searches are successful
    def test_search_by_name(self):
        test_call = app.test_client(self)
        response = test_call.get('contacts/search/name/S')
        response_empty = test_call.get('contacts/search/name/xyl')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_empty.status_code, 200)

    # Test existing and non-existent searches are successful
    def test_search_by_phone(self):
        test_call = app.test_client(self)
        response_success = test_call.get('/contacts/search/phone/1')
        response_fail = test_call.get('/contacts/search/phone/xyl')
        self.assertEqual(response_success.status_code, 200)
        self.assertEqual(response_fail.status_code, 200)

if __name__ == '__main__':
    unittest.main()
