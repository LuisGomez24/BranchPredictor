# Copyright 2022 - Luis Fernando Gomez Sanchez - luis.gomez20@ucr.ac.cr
import argparse

def LocalPredictor():
    pass

def GlobalPredictor():
    pass

def BimodalPredictor():
    pass

def main() -> None:
    msg = "Predictor de Saltos hecho por Luis Gomez - C03309"
    parser = argparse.ArgumentParser(description = msg)

    parser.add_argument("-bp", "--BranchPredictor",
        help = "Tipo de Predictor. Opciones: 0: Bimodal 2 bits / 1: Global 2 Niveles / 2:Local 2 Niveles / 3: Torneo",
        default=0, type=int, choices=range(0,4))

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
