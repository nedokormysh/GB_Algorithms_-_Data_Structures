import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]
    return _fib_dict(n)

# test_fib(fib_dict)

# "Lesson4_Code4.fib_dict(10)"
# 1000 loops, best of 5: 8.72 usec per loop


# "Lesson4_Code4.fib_dict(15)"
# 1000 loops, best of 5: 5.97 usec per loop


# "Lesson4_Code4.fib_dict(20)"
# 1000 loops, best of 5: 8.07 usec per loop

# "Lesson4_Code4.fib_dict(100)"
# 1000 loops, best of 5: 61.6 usec per loop

# "Lesson4_Code4.fib_dict(200)"
# 1000 loops, best of 5: 91.5 usec per loop

#  "Lesson4_Code4.fib_dict(500)"
# 1000 loops, best of 5: 330 usec per loop




# cProfile.run('fib_dict(10)')
# 23 function calls (5 primitive calls) in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4_Code4.py:10(fib_dict)
#      19/1    0.000    0.000    0.000    0.000 Lesson4_Code4.py:13(_fib_dict)
#         1    0.002    0.002    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('fib_dict(15)')

# 33 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4_Code4.py:10(fib_dict)
#      29/1    0.000    0.000    0.000    0.000 Lesson4_Code4.py:13(_fib_dict)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('fib_dict(20)')
#
#
#
# 43 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4_Code4.py:10(fib_dict)
#      39/1    0.000    0.000    0.000    0.000 Lesson4_Code4.py:13(_fib_dict)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('fib_dict(100)')
# 203 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4_Code4.py:10(fib_dict)
#     199/1    0.000    0.000    0.000    0.000 Lesson4_Code4.py:13(_fib_dict)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('fib_dict(500)')
#
#
# 1003 function calls (5 primitive calls) in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.002    0.002 Lesson4_Code4.py:10(fib_dict)
#     999/1    0.002    0.000    0.002    0.002 Lesson4_Code4.py:13(_fib_dict)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}