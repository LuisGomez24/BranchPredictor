# Copyright 2022 - Luis Fernando Gomez Sanchez - luis.gomez20@ucr.ac.cr
import argparse
import linecache
from predictors import BimodalPredictor
from predictors import GlobalPredictor

def start_bimodal_prediction(index_size) -> dict:
    simulation_result = {
        'branches':            0,
        'correctly_taken':     0,
        'incorrectly_taken':   0,
        'correctly_untaken':   0,
        'incorrectly_untaken': 0,
    }
    
    predictor = BimodalPredictor(index_size)
    chunk = 1
    while True:
        trace_line = get_PC_address(chunk)
        if not trace_line:
            break
        
        branch_data = trace_line.split()
        pc_address = int(branch_data[0])
        taken = True if branch_data[1] == "T" else False
        
        simulation_result = predictor.predict_branch(simulation_result,
                                                     pc_address,
                                                     taken)
        chunk += 1
    
    return simulation_result

def start_global_prediction(index_size, global_size) -> dict:
    simulation_result = {
        'branches':            0,
        'correctly_taken':     0,
        'incorrectly_taken':   0,
        'correctly_untaken':   0,
        'incorrectly_untaken': 0,
    }
    
    predictor = GlobalPredictor(index_size, global_size)
    chunk = 1
    while True:
        trace_line = get_PC_address(chunk)
        if not trace_line:
            break
        
        branch_data = trace_line.split()
        pc_address = int(branch_data[0])
        taken = True if branch_data[1] == "T" else False
        
        simulation_result = predictor.predict_branch(simulation_result,
                                                     pc_address,
                                                     taken)
        chunk += 1
    
    return simulation_result

def get_PC_address(index) -> str:
    return linecache.getline('../trace/trace.txt', index)

def print_predictor_params(predictor_type, predictor_params) -> None:
    print("Parámetros del predictor:")
    print(f"\tTipo de predictor: {predictor_type}")
    print(f"\tEntradas en el predictor: {2 ** predictor_params.IndexSize}")
    if (predictor_type == "Global"):
        print(f"\tTamaño de los registros de historia global: {predictor_params.GlobalHistory}")

def print_simulation_result(simulation_result) -> None:
    prediction_percent = ((simulation_result['correctly_taken'] + 
                          simulation_result['correctly_untaken']) / 
                          simulation_result['branches'])
    prediction_percent = round(prediction_percent * 100, 4)
    
    print("Resultados de la simulación:")
    print(f"\t# branches: {simulation_result['branches']}")
    print('\t# branches tomados predichos correctamente: '      +
        str(simulation_result['correctly_taken']))
    print('\t# branches tomados predichos incorrectamente: '    +
        str(simulation_result['incorrectly_taken']))
    print('\t# branches no tomados predichos correctamente: '   +
        str(simulation_result['correctly_untaken']))
    print('\t# branches no tomados predichos incorrectamente: ' +
        str(simulation_result['incorrectly_untaken']))
    print(f'\t% predicciones correctas: {prediction_percent}%')


def main() -> None:
    description = "Predictor de Saltos hecho por Luis Gomez - C03309"
    parser = argparse.ArgumentParser(description = description)

    parser.add_argument("-s", "--IndexSize",
        help = "Cantidad de Bits para Indexar.", type=int, required=True)
    parser.add_argument("-bp", "--BranchPredictor",
        help = "Tipo de Predictor. Opciones: 0: Bimodal 2 bits \
        / 1: Global 2 Niveles",
        default=0, type=int, choices=range(0,2), required=True)
    parser.add_argument("-gh", "--GlobalHistory",
        help = "Tamaño de Registro de Historia Global.", default=0, type=int)

    args = parser.parse_args()
    
    if (args.BranchPredictor == 0):
        print_predictor_params("Bimodal", args)
        simulation_result = start_bimodal_prediction(args.IndexSize)
    elif args.BranchPredictor == 1 and args.GlobalHistory == 0:
        print("usage: main.py [-h] -s INDEXSIZE -bp {0,1} [-gh GLOBALHISTORY]")
        print("main.py: error: the following arguments are required: -gh/--GlobalHistory")
        exit(0)
    elif args.BranchPredictor == 1:
        print_predictor_params("Global", args)
        if args.IndexSize < args.GlobalHistory:
            simulation_result = start_global_prediction(args.IndexSize, 
                                                        args.IndexSize)
        else:
            simulation_result = start_global_prediction(args.IndexSize,
                                                        args.GlobalHistory)
        
    print_simulation_result(simulation_result)

if __name__ == '__main__':
    main()
