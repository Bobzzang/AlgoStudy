import io
from ans_12865_JHK import solve


def test_12865_1(monkeypatch, capsys):
    inStr = "4 7\n" + "6 13\n" + "4 8\n" + "3 6\n" + "5 12\n"
    outStr = "14\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(inStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == outStr
