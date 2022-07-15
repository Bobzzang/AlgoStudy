import io
from ans_1181_JHK import solve


def test_1181_1(monkeypatch, capsys):
    inpStr = (
        "13\n"
        + "but\n"
        + "i\n"
        + "wont\n"
        + "hesitate\n"
        + "no\n"
        + "more\n"
        + "no\n"
        + "more\n"
        + "it\n"
        + "cannot\n"
        + "wait\n"
        + "im\n"
        + "yours\n"
    )
    monkeypatch.setattr("sys.stdin", io.StringIO(inpStr))
    solve()
    capture = capsys.readouterr()
    outStr = (
        "i\n"
        + "im\n"
        + "it\n"
        + "no\n"
        + "but\n"
        + "more\n"
        + "wait\n"
        + "wont\n"
        + "yours\n"
        + "cannot\n"
        + "hesitate\n"
    )
    assert capture.out == outStr
