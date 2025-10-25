import sys

sys.dont_write_bytecode = True

def main():
    import updater
    updater.main()

    import program
    program.main()

if __name__ == "__main__":
    main()