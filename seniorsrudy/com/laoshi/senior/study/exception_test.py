# try:
#     监控异常
# except Exception[,reason]
#     异常处理
# finally:
#     最终执行

# year = int(input('输入年份'))
# try:
#     # a = 10/0
#     year = int(input('输入年份'))
# except ValueError:
#     print("请输入数字")
# except ZeroDivisionError:
#     print("代码异常")
# except Exception as e:
#     print(e)
try:
    a = 10 / 0
    year = int(input('输入年份'))
except (ValueError, ZeroDivisionError) as e:
    print('异常为%s' % e)
except Exception as e:
    print(e)
