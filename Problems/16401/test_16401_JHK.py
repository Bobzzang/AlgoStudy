import io
from ans_16401_JHK import solve


def test_16401_01(monkeypatch, capsys):
    InStr = "4 3\n" + "10 10 15\n"
    OutStr = "7\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_16401_02(monkeypatch, capsys):
    InStr = "3 10\n" + "1 2 3 4 5 6 7 8 9 10\n"
    OutStr = "8\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_16401_03(monkeypatch, capsys):
    InStr = "3 9\n" + "1 2 3 4 5 6 7 9 10\n"
    OutStr = "7\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_16401_04(monkeypatch, capsys):
    InStr = "1 9\n" + "1 2 3 4 5 6 7 9 10\n"
    OutStr = "10\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr
