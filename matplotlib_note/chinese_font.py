import matplotlib.font_manager

a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])  # 显示matplotlib已有所有字体
for i in a:
    print(i)

# import shutil
# import matplotlib
#
# shutil.rmtree(matplotlib.get_cachedir())

