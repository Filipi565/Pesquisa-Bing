from util.window import Window

def main():
    window = Window()
    try:
        window.mainloop()
    except BaseException:
        window.should_stop = True

    window.should_stop = True