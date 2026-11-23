import unittest

from utils.commands.command_parser import parse_command


class ParseCommandTests(unittest.TestCase):
    def test_parses_a_single_argument(self):
        self.assertEqual(parse_command("!player Steve"), ("!player", "Steve"))

    def test_accepts_repeated_whitespace(self):
        self.assertEqual(
            parse_command("  !domain   play.example.com  "),
            ("!domain", "play.example.com"),
        )

    def test_accepts_tabs_between_tokens(self):
        self.assertEqual(parse_command("!ipinfo\t127.0.0.1"), ("!ipinfo", "127.0.0.1"))

    def test_missing_argument_returns_none(self):
        self.assertEqual(parse_command("!player"), ("!player", None))

    def test_extra_arguments_are_rejected(self):
        self.assertEqual(parse_command("!server play.example.com extra"), ("!server", None))

    def test_empty_message_returns_no_command(self):
        self.assertEqual(parse_command("   "), (None, None))

    def test_no_argument_command_is_preserved(self):
        self.assertEqual(parse_command("!help"), ("!help", None))


if __name__ == "__main__":
    unittest.main()
