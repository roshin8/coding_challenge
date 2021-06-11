import unittest

# To test the following, I would probably implement a spy with mock or magic mock with some handrolled test classes

class TestStats(unittest.TestCase):

    def test_get_github_stats(self):
        """
        Mock the api to return predefined values and have them asserted 
        """
        pass

    def test_get_bitbucket_stats(self):
        """
        Mock the api to return predefined values and have them asserted 
        """
        pass

    def test_aggregated_stats(self):
        """
        Assert for aggregated results from both bitbucket and github
        """
        pass

    def test_get_requests(self):
        """
        Test scenarios where get requests pass and fail to see if all the scenarios are handled properly
        """
        pass


    def test_return_value(self):
        """
        Test that given a response, the correct array of Repo object is returned
        """
        pass

    def test_schema(self):
        """
        Test that schemas hold to the right stuctures
        """
        pass


if __name__ == '__main__':
    unittest.main()