import io
from ans_2343_JHK import solve


def test_2343_01(monkeypatch, capsys):
    InStr = "9 3\n" + "1 2 3 4 5 6 7 8 9\n"
    OutStr = "17\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_2343_02(monkeypatch, capsys):
    InStr = "9 3\n" + "1 2 3 1 2 3 1 2 3\n"
    OutStr = "6\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_2343_03(monkeypatch, capsys):
    InStr = "1 1\n" + "5\n"
    OutStr = "5\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_2343_04(monkeypatch, capsys):
    InStr = "3 1\n" + "1 2 5\n"
    OutStr = "8\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_2343_05(monkeypatch, capsys):
    InStr = "6 2\n" + "1 2 9 2 1 3\n"
    OutStr = "12\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_2343_06(monkeypatch, capsys):
    InStr = "6 6\n" + "1 1 1 1 1 1\n"
    OutStr = "1\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_2343_07(monkeypatch, capsys):
    InStr = "6 6\n" + "1 1 10 1 1 1\n"
    OutStr = "10\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr
