"""WordpressSalts."""

import json
import random
import sublime
import sublime_plugin

VALID_CHARACTERS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
MINIMUM_SALT_LENGTH = 64
WORDPRESS_SALTS = [
    "AUTH_KEY",
    "SECURE_AUTH_KEY",
    "LOGGED_IN_KEY",
    "NONCE_KEY",
    "AUTH_SALT",
    "SECURE_AUTH_SALT",
    "LOGGED_IN_SALT",
    "NONCE_SALT"
]


class WordpressSaltsCommand(sublime_plugin.TextCommand):
    """WordpressSalts command."""

    def run(self, edit):
        """Run the WordpressSalts command."""
        salt_length_setting = self.load_settings("salt_length") or MINIMUM_SALT_LENGTH
        salt_length = salt_length_setting \
            if isinstance(salt_length_setting, int) and salt_length_setting >= MINIMUM_SALT_LENGTH \
            else MINIMUM_SALT_LENGTH

        scope = self.view.scope_name(self.view.sel()[0].a)
        max_length = len(max(WORDPRESS_SALTS, key=len)) + 1
        wordpress_salts = ""

        if "source.json" in scope:
            salts_dictionary = {}

        for i, wordpress_salt in enumerate(WORDPRESS_SALTS):
            if "source.php" in scope:
                wordpress_salts += self.create_php_line(wordpress_salt, salt_length, max_length)
            elif "source.yaml" in scope:
                wordpress_salts += self.create_yaml_line(wordpress_salt, salt_length)
            elif "source.env" in scope:
                wordpress_salts += self.create_env_line(wordpress_salt, salt_length)
            elif "source.json" in scope:
                salts_dictionary.update(self.create_json_attribute(wordpress_salt, salt_length))
            else:
                if self.load_settings("error_message") is True:
                    sublime.error_message(("WordPress Salts\n\nUnsupported document type {}, aborting").format(scope))
                else:
                    sublime.status_message("WordPress Salts: Unsupported document type")

        if "source.json" in scope:
            indent = self.load_settings("indent") or 2
            wordpress_salts = json.dumps(salts_dictionary, indent=indent)

        for r in self.view.sel():
            self.view.erase(edit, r)
            self.view.insert(edit, r.begin(), wordpress_salts)

    def create_php_line(self, key, salt_length, max_length):
        """Generate PHP line for key and salt."""
        prettify = self.load_settings("prettify")

        separator = " " \
            if prettify is not True \
            else " ".ljust(max_length - len(key))

        random_string = self.get_random_string(salt_length)

        result = "define('{}',{}'{}');\n".format(key, separator, random_string)

        return result

    def create_yaml_line(self, key, salt_length):
        """Generate YAML line for key and salt."""
        random_string = self.get_random_string(salt_length)
        result = "{}: \"{}\"\n".format(key.lower(), random_string)

        return result

    def create_env_line(self, key, salt_length):
        """Generate DotEnv line for key and salt."""
        random_string = self.get_random_string(salt_length)
        result = "{}='{}'\n".format(key, random_string)

        return result

    def create_json_attribute(self, key, salt_length):
        """Generate JSON attribute for key and salt."""
        random_string = self.get_random_string(salt_length)
        result = {key: random_string}

        return result

    def get_random_string(self, salt_length):
        """Generate random string at specified length."""
        result = "".join(random.SystemRandom().choice(VALID_CHARACTERS) for _ in range(salt_length))

        return result

    def load_settings(self, key):
        """Load package settings."""
        return sublime.load_settings("WordPress Salts.sublime-settings").get(key)
