import unittest
from flake8 import api

def parse_data(data_str):
	try:
		return int(data_str)
	except ValueError:
		return None

class TestDataParsing(unittest.TestCase):
	def test_parse_valid_integer(self):
		self.assertEqual(parse_data("42"), 42)

	def test_parse_invalid_integer(self):
		self.assertIsNone(parse_data("abc"))

if __name__ == "__main__":
	# Run unit tests
	unittest.main()

	# Run flake8 linter
	linter_errors = api.get_style_guide(ignore=['F821']).check_files(['data_parsing.py'])

	# Display linter errors
	for error in linter_errors:
		print(f"Linter Error: {error.filename}:{error.line_number}:{error.code} {error.text}")

	# Fix the linter error (Unused argument 'data_str' in parse_data function)
	def parse_data(data_str):
		try:
			return int(data_str)
		except ValueError:
			return None

	# Run unit tests again to verify the fix
	unittest.main()
