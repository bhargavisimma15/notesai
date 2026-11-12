import unittest

from app import app, analyze_text
from cleaner import clean_text
from organizer import detect_bullet_points, detect_disadvantages


class SmartNotesTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_clean_text_removes_outer_whitespace_and_blank_lines(self):
        self.assertEqual(clean_text("  One. \n\n  Two.  "), "One.\n\nTwo.")

    def test_detect_bullet_points_handles_numbered_items(self):
        notes = "- First\n* Second\n1. Third\nNot a bullet."
        self.assertEqual(
            detect_bullet_points(notes),
            ["- First", "* Second", "1. Third"],
        )

    def test_disadvantages_are_not_included_in_advantages(self):
        notes = "Advantages:\nEasy to use.\n\nDisadvantages:\nCosts money."
        result = analyze_text(notes)
        self.assertEqual(result["advantages"], ["Easy to use."])
        self.assertEqual(detect_disadvantages(notes), ["Costs money."])

    def test_homepage_displays_analysis_after_submission(self):
        response = self.client.post("/", data={"text": "Python is easy to learn."})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Python is easy to learn.", response.data)
        self.assertIn(b"Analysis", response.data)

    def test_empty_submission_shows_helpful_message(self):
        response = self.client.post("/", data={"text": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Enter some notes", response.data)


if __name__ == "__main__":
    unittest.main()
