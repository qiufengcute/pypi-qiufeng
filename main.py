from pyfiglet import Figlet, FigletFont

def greeting(font="larry3d"):
    f = Figlet(font=font)
    print('beta')
    print(f.renderText('QIUFENG'))

def get_fonts():
    """
    show all fonts
    :return:
    """
    all_fonts = FigletFont().getFonts()
    return all_fonts
