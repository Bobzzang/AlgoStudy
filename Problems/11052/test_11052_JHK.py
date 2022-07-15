import io
from ans_11052_JHK import solve


def test_11052_01(monkeypatch, capsys):
    # Greedy 로 안풀리는 케이스
    InStr = "6\n" + "1 1 1 12 14\n"
    OutStr = "15\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr


def test_11052_02(monkeypatch, capsys):
    InStr = "10\n" + "1 1 2 3 5 8 13 21 34 55\n"
    OutStr = "55\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(InStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == OutStr
