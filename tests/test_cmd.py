from llm.plugins import load_plugins, pm
from llm_cmd import strip_thinking


def test_plugin_is_installed():
    load_plugins()
    names = [mod.__name__ for mod in pm.get_plugins()]
    assert "llm_cmd" in names


def test_strip_thinking():
    # Response shape from https://github.com/simonw/llm-cmd/issues/27
    text = "<think>\nOkay, the user wants to show their bash history.\n</think>\n\n  history\n"
    assert strip_thinking(text) == "history"


def test_strip_thinking_no_block():
    assert strip_thinking("ls -la") == "ls -la"
