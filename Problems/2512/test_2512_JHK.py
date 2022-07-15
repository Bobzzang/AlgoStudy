import io
from ans_2512_JHK import solve


def test_2512_1(monkeypatch, capsys):
    InStr = "4\n" + "120 110 140 150\n" + "485\n"
    OutStr = "127\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_2512_2(monkeypatch, capsys):
    InStr = "5\n" + "70 80 30 40 100\n" + "450\n"
    OutStr = "100\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_2512_3(monkeypatch, capsys):
    InStr = "3\n" + "1 1 1\n" + "100\n"
    OutStr = "1\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr
