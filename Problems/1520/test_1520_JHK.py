import io
from ans_1520_JHK import solve


def test_1520_1(monkeypatch, capsys):
    inpStr = (
        "4 5\n"
        + "50 45 37 32 30\n"
        + "35 50 40 20 25\n"
        + "30 30 25 17 28\n"
        + "27 24 22 15 10\n"
    )
    outStr = "3\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(inpStr))
    solve()
    capture = capsys.readouterr()
    assert capture.out == outStr
