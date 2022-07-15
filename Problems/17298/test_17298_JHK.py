import io
from ans_17298_JHK import solve


def test_17298_1(monkeypatch, capsys):
    InStr = "7\n" + "4 3 2 1 2 3 4\n"
    OutStr = "-1 4 3 2 3 4 -1\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_17298_2(monkeypatch, capsys):
    InStr = "11\n" + "1 3 2 9 5 4 8 3 5 2 10\n"
    OutStr = "3 9 9 10 8 8 10 5 10 10 -1\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr
