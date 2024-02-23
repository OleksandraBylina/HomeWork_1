from FigureReader import FigureReader
pust=[]
pusty=[]
if __name__ == "__main__":
    for file in ['input01.txt', 'input02.txt', 'input03.txt', 'input.txt']:
        reader = FigureReader(file)
        figures = reader.read()
        for figure in figures:
            try:
                print(figure, "Perimeter = ", figure.perimeter(), "Square = ", figure.square())
            except AttributeError:

                print(figure, "Square = ", figure.square())
        for figure in figures:
            bonk=figure.square()
            pust.append(bonk)
            try:
                bam=figure.perimeter()
                pusty.append(bam)
            except AttributeError:
                pass
        maxAttributes = [0, 0]  # відповідно ні проща, ні периметер не можуть бути менші за 0
        maxFigure = figures[0]
        for figure in figures:
            try:
                if figure.square() > maxAttributes[0]:
                    maxAttributes = [figure.square()]
                    maxFigure = figure
            except (AttributeError, TypeError):
                continue

        print("The biggest square has", maxFigure, "It's area =", (max(pust)))
        maxfun = [0, 0]  # відповідно ні проща, ні периметер не можуть бути менші за 0
        maxmi = figures[0]
        for figure in figures:
            try:
                if figure.perimeter() > maxfun[0]:
                    maxfun = [figure.square()]
                    maxmi = figure
            except (AttributeError, TypeError):
                continue

        print("The biggest perimeter or length has", maxmi, "It's perimeter(length) =", (max(pusty)))



