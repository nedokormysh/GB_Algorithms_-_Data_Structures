import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]
    return _fib_list(n)

# test_fib(fib_list)

# "Lesson4_Code5.fib_list(10)"
# 1000 loops, best of 5: 12.5 usec per loop

# "Lesson4_Code5.fib_list(20)"
# 1000 loops, best of 5: 18.8 usec per loop
#
# "Lesson4_Code5.fib_list(100)"
# 1000 loops, best of 5: 60.1 usec per loop

#  "Lesson4_Code5.fib_list(200)"
# 1000 loops, best of 5: 91.3 usec per loop

# "Lesson4_Code5.fib_list(500)"
# 1000 loops, best of 5: 271 usec per loop

# cProfile.run('fib_list(10)')
#
# 23 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4_Code5.py:10(fib_list)
#      19/1    0.000    0.000    0.000    0.000 Lesson4_Code5.py:14(_fib_list)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('fib_list(20)')
# 43 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4_Code5.py:10(fib_list)
#      39/1    0.000    0.000    0.000    0.000 Lesson4_Code5.py:14(_fib_list)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('fib_list(100)')
# 203 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4_Code5.py:10(fib_list)
#     199/1    0.000    0.000    0.000    0.000 Lesson4_Code5.py:14(_fib_list)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run('fib_list(200)')
# 403 function calls (5 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 Lesson4_Code5.py:10(fib_list)
#     399/1    0.001    0.000    0.001    0.001 Lesson4_Code5.py:14(_fib_list)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('fib_list(500)')
# 1003 function calls (5 primitive calls) in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 Lesson4_Code5.py:10(fib_list)
#     999/1    0.003    0.000    0.003    0.003 Lesson4_Code5.py:14(_fib_list)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}