# Copyright 2022 - Luis Fernando Gomez Sanchez - luis.gomez20@ucr.ac.cr
import argparse

def BimodalPredictor(branch_options) -> dict:
    simulation_result = {
        'branches':            1,
        'correctly_taken':     0,
        'incorrectly_taken':   0,
        'correctly_untaken':   0,
        'incorrectly_untaken': 0,
    }
    
    return simulation_result


def LocalPredictor(branch_options) -> dict:
    simulation_result = {
        'branches':            1,
        'correctly_taken':     0,
        'incorrectly_taken':   0,
        'correctly_untaken':   0,
        'incorrectly_untaken': 0,
    }
    
    return simulation_result


def GlobalPredictor(branch_options) -> dict:
    simulation_result = {
        'branches':            1,
        'correctly_taken':     0,
        'incorrectly_taken':   0,
        'correctly_untaken':   0,
        'incorrectly_untaken': 0,
    }
    
    return simulation_result


def TournamentPredictor(branch_options) -> dict:
    simulation_result = {
        'branches':            1,
        'correctly_taken':     0,
        'incorrectly_taken':   0,
        'correctly_untaken':   0,
        'incorrectly_untaken': 0,
    }
    
    return simulation_result


def print_simulation_result(simulation_result) -> None:
    prediction_percent = ((simulation_result["correctly_taken"] + 
                          simulation_result["correctly_untaken"]) / 
                          simulation_result["branches"])
    
    print(f'# branches: {simulation_result["branches"]}')
    print('# branches tomados predichos correctamente: '      +
        str(simulation_result["correctly_taken"]))
    print('# branches tomados predichos incorrectamente: '    +
        str(simulation_result["incorrectly_taken"]))
    print('# branches no tomados predichos correctamente: '   +
        str(simulation_result["correctly_untaken"]))
    print('# branches no tomados predichos incorrectamente: ' +
        str(simulation_result["incorrectly_untaken"]))
    print(f'% predicciones correctas: {prediction_percent}')


def main() -> None:
    description = "Predictor de Saltos hecho por Luis Gomez - C03309"
    parser = argparse.ArgumentParser(description = description)

    parser.add_argument("-s", "--IndexSize",
        help = "Cantidad de Bits para Indexar.", type=int, required=True)
    parser.add_argument("-bp", "--BranchPredictor",
        help = "Tipo de Predictor. Opciones: 0: Bimodal 2 bits \
        / 1: Global 2 Niveles / 2:Local 2 Niveles / 3: Torneo",
        default=0, type=int, choices=range(0,4))
    parser.add_argument("-gh", "--GlobalHistory",
        help = "Tamaño de Registro de Historia Global.", default=0, type=int)
    parser.add_argument("-lh", "--LocalHistory",
        help = "Tamaño de Registro de Historia Local.", default=0, type=int)

    args = parser.parse_args()
    if args.BranchPredictor == 0:
        simulation_result = BimodalPredictor(args)
    elif args.BranchPredictor == 1:
        simulation_result = GlobalPredictor(args)
    elif args.BranchPredictor == 2:
        simulation_result = LocalPredictor(args)
    else:
        simulation_result = TournamentPredictor(args)
    
    print_simulation_result(simulation_result)

if __name__ == '__main__':
    main()
