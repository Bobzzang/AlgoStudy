# https://www.acmicpc.net/problem/14569
import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    Lesson = []
    for _ in range(N):
        TempLesson = list(map(int, input().split()))
        TempLessonTime = 0
        for i, les in enumerate(TempLesson):
            if i != 0:
                TempLessonTime |= 1 << les
        Lesson.append(TempLessonTime)

    M = int(input())
    RemainTime_Student = []
    for _ in range(M):
        TempStudent = list(map(int, input().split()))
        TempRemainTime = 0
        for i, t in enumerate(TempStudent):
            if i != 0:
                TempRemainTime |= 1 << t
        RemainTime_Student.append(TempRemainTime)

    for RemainTime in RemainTime_Student:
        cnt = 0
        for LessonTime in Lesson:
            if RemainTime & LessonTime == LessonTime:
                cnt += 1
        print(cnt)

    return


if __name__ == "__main__":
    solve()
