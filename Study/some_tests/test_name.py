from to_be_tested import AnonymousSurvey
import unittest


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survery = AnonymousSurvey(question)
        self.responses = ['English', 'Korean', 'Spanish']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""

        self.my_survery.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survery.responses)

    def test_store_three_responses(self):
        """Test that a single response is stored properly."""
        for response in self.responses:
            self.my_survery.store_response(response)

        for respnse in self.responses:
            self.assertIn(response, self.my_survery.responses)


if __name__ == "__main__":
    unittest.main()

'''
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_suvery = AnonymousSurvey(question)
        my_suvery.store_response('English')
        self.assertIn('English', my_suvery.responses)

    def test_store_three_responses(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_suvery = AnonymousSurvey(question)
        responses = ['English', 'Korean', 'Spanish']
        for response in responses:
            my_suvery.store_response(response)

        for respnse in responses:
            self.assertIn(response, my_suvery.responses)


if __name__ == "__main__":
    unittest.main()


question = "What language do you first learn to speak?"
mysurvey = AnonymousSurvey(question)

mysurvey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    # if response != '':
    mysurvey.store_response(response)

print("\Thank you to everyone who participated in the survey!")
mysurvey.show_results()


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()



print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formattted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formattted_name}")
'''
